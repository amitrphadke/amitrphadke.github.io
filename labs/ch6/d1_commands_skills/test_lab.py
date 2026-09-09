import re
from pathlib import Path
from lab import COMPARISON
P = Path(__file__).parent / "project" / ".claude"

def test_command():
    md = (P / "commands" / "test.md").read_text()
    assert "$ARGUMENTS" in md

def test_skill_frontmatter():
    md = (P / "skills" / "python-standard" / "SKILL.md").read_text()
    m = re.match(r"^---\n(.*?)\n---", md, re.S)
    assert m, "front-matter missing"
    fm = m.group(1)
    assert re.search(r"^name:\s*python-standard", fm, re.M)
    assert re.search(r"^description:\s*.{20,}", fm, re.M)
    assert any(w in fm.lower() for w in ["use when", "when ", "whenever"])

def test_comparison():
    assert all(v != "TODO" and len(v) > 15 for v in COMPARISON.values())
    assert "user" in COMPARISON["command"].lower() and "model" in COMPARISON["skill"].lower()
