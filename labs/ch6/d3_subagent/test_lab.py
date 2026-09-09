import re
from pathlib import Path
P = Path(__file__).parent / "project" / ".claude" / "agents" / "reviewer.md"

def test_subagent_file():
    md = P.read_text()
    fm = re.match(r"^---\n(.*?)\n---\n(.*)$", md, re.S)
    assert fm
    head, body = fm.groups()
    assert re.search(r"^name:\s*reviewer", head, re.M)
    assert re.search(r"^description:\s*.{20,}", head, re.M)
    tools = re.search(r"^tools:\s*(.+)$", head, re.M).group(1)
    assert set(t.strip() for t in tools.split(",")) <= {"Read", "Grep", "Glob"}
    assert len([l for l in body.splitlines() if l.strip().startswith(("-", "*", "1", "2", "3", "4", "5"))]) >= 5
