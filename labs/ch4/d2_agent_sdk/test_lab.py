import shutil, pytest
from pathlib import Path
pytest.importorskip("claude_agent_sdk")
pytestmark = pytest.mark.skipif(not shutil.which("claude"), reason="Claude Code CLI not installed / logged in")
from lab import summarise_repo, tools_used, WHAT_SDK_ADDS
LABS = str(Path(__file__).resolve().parents[2])

def test_summary():
    s = summarise_repo(LABS)
    assert len(s) > 40

def test_restricted_tools_only():
    used = tools_used(LABS)
    assert used and used <= {"Read", "Glob", "Grep"}

def test_notes():
    assert len(WHAT_SDK_ADDS) == 3 and all(len(x) > 10 for x in WHAT_SDK_ADDS)
