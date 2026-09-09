import json, subprocess, sys
from pathlib import Path
from lab import MODES
P = Path(__file__).parent / "project"

def test_settings_hooks():
    s = json.loads((P / ".claude" / "settings.json").read_text())
    hooks = s["hooks"]
    post = [h for h in hooks["PostToolUse"] if "Edit" in h.get("matcher", "")]
    pre = [h for h in hooks["PreToolUse"] if "Bash" in h.get("matcher", "")]
    assert post and pre
    assert any("lint" in c["command"] for h in post for c in h["hooks"])
    assert any("guard" in c["command"] for h in pre for c in h["hooks"])

def _guard(cmd):
    payload = json.dumps({"tool_name": "Bash", "tool_input": {"command": cmd}})
    return subprocess.run([sys.executable, str(P / "hooks" / "guard.py")], input=payload, capture_output=True, text=True)

def test_guard_blocks_and_allows():
    r = _guard("rm -rf /tmp/x"); assert r.returncode == 2 and r.stderr.strip()
    r = _guard("git push --force origin main"); assert r.returncode == 2
    r = _guard("ls -la"); assert r.returncode == 0

def test_modes():
    assert all(v != "TODO" for v in MODES.values())
    assert "read" in MODES["plan"].lower()
