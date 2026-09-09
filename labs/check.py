#!/usr/bin/env python3
"""Run a lab's tests; when they pass, tick the lab in the study tracker on amitphadke.com.

  python check.py ch1/d0        # one lab (folder prefix is enough)
  python check.py ch2           # every lab in a chapter
  python check.py all           # everything
  python check.py ch1/d0 --no-tick

Ticks are written to learning/ccdv-f/tracker/progress.json in the site repo through the GitHub API,
using GH_TOKEN from labs/.env (fine-grained token, Contents read/write on the site repo)."""
import base64, json, os, re, subprocess, sys, urllib.request, xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from dotenv import load_dotenv; load_dotenv(HERE / ".env")
LABS = json.loads((HERE / "labs.json").read_text())
GH = {"owner": "amitrphadke", "repo": "amitrphadke.github.io", "branch": "master", "path": "learning/ccdv-f/tracker/progress.json"}
API = f"https://api.github.com/repos/{GH['owner']}/{GH['repo']}/contents/{GH['path']}"

def select(arg):
    if arg == "all": return LABS
    return [l for l in LABS if l["path"].startswith(arg.rstrip("/"))]

def run_lab(l):
    d = HERE / l["path"]; junit = d / ".junit.xml"
    env = dict(os.environ, PYTHONPATH=str(HERE) + os.pathsep + str(d))
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--tb=short", "-rs", f"--junitxml={junit}", str(d)],
                       env=env, cwd=d, capture_output=True, text=True)
    passed = failed = skipped = 0
    if junit.exists():
        root = ET.parse(junit).getroot(); suite = root if root.tag == "testsuite" else root.find("testsuite")
        tests, failed, errors, skipped = (int(suite.get(k, 0)) for k in ("tests", "failures", "errors", "skipped"))
        failed += errors; passed = tests - failed - skipped
        junit.unlink()
    ok = r.returncode == 0 and failed == 0 and passed > 0 and (skipped == 0 or not l["api"])
    return ok, passed, failed, skipped, r.stdout + r.stderr

def gh(method, url, token, data=None):
    req = urllib.request.Request(url, method=method, data=json.dumps(data).encode() if data else None,
        headers={"Authorization": "Bearer " + token, "Accept": "application/vnd.github+json", "Content-Type": "application/json", "User-Agent": "ccdvf-labs"})
    with urllib.request.urlopen(req) as resp: return json.loads(resp.read())

def tick(ids):
    token = os.getenv("GH_TOKEN")
    if not token: print("  (GH_TOKEN not set in labs/.env — tracker not updated)"); return
    for attempt in range(2):
        cur = gh("GET", API + f"?ref={GH['branch']}", token)
        data = json.loads(base64.b64decode(cur["content"]).decode() or "{}"); data.setdefault("state", {})
        new = [i for i in ids if not data["state"].get(i)]
        if not new: print("  tracker already up to date"); return
        for i in new: data["state"][i] = True
        data["savedAt"] = datetime.now(timezone.utc).isoformat()
        body = {"message": f"tracker: lab passed — {', '.join(new)}", "branch": GH["branch"], "sha": cur["sha"],
                "content": base64.b64encode(json.dumps(data, indent=1).encode()).decode()}
        try:
            gh("PUT", API, token, body); print(f"  ✓ ticked in tracker: {', '.join(new)}"); return
        except urllib.error.HTTPError as e:
            if e.code in (409, 422) and attempt == 0: continue
            print(f"  tracker update failed: HTTP {e.code}"); return

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args: print(__doc__); sys.exit(2)
    labs = select(args[0])
    if not labs: print(f"no lab matches {args[0]}"); sys.exit(2)
    passed_ids, any_fail = [], False
    for l in labs:
        ok, p, f, s, out = run_lab(l)
        mark = "PASS" if ok else ("SKIP" if p == 0 and f == 0 else "FAIL")
        print(f"{mark:4} {l['path']:34} {l['title']}   ({p} passed, {f} failed, {s} skipped)")
        if ok: passed_ids.append(l["id"])
        else:
            any_fail = True
            if f or "--verbose" in sys.argv: print(textwrap_indent(out))
            elif s and l["api"]: print("      needs ANTHROPIC_API_KEY (or Claude Code login) — see README")
    if passed_ids and "--no-tick" not in sys.argv: tick(passed_ids)
    sys.exit(1 if any_fail else 0)

def textwrap_indent(s): return "\n".join("      " + line for line in s.strip().splitlines()[-40:])

if __name__ == "__main__": main()
