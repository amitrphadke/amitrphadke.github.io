from pathlib import Path
from lab import PRECEDENCE
P = Path(__file__).parent / "project"

def test_claude_md_structure():
    md = (P / "CLAUDE.md").read_text()
    for h in ["Stack", "Commands", "Conventions", "Review checklist"]:
        assert h.lower() in md.lower(), h
    assert "@docs/style.md" in md
    assert len((P / "docs" / "style.md").read_text().strip().splitlines()) >= 5

def test_local_override_ignored():
    assert "CLAUDE.local.md" in (P / ".gitignore").read_text()

def test_precedence():
    assert len(PRECEDENCE) == 4
    joined = " > ".join(PRECEDENCE).lower()
    assert joined.index("managed") < joined.index("user") < joined.index("project") < joined.index("local")
