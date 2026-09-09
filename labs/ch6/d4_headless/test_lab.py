import shutil, pytest
from pathlib import Path
HERE = Path(__file__).parent

def test_workflow_file():
    y = (HERE / "workflow.yml").read_text()
    assert "pull_request" in y and "claude -p" in y and "ANTHROPIC_API_KEY" in y and "secrets." in y

@pytest.mark.skipif(not shutil.which("claude"), reason="Claude Code CLI not installed / logged in")
def test_headless_json():
    from lab import run_headless, result_text
    d = run_headless("In one sentence, what is in README.md here?", str(HERE))
    assert d.get("type") == "result" and len(result_text(d)) > 10
