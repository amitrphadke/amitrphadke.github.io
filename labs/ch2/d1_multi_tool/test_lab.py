import pytest
from common import has_key
from lab import Agent
pytestmark = pytest.mark.skipif(not has_key(), reason="ANTHROPIC_API_KEY not set")

def test_two_tools_in_one_prompt_are_logged():
    a = Agent()
    out = a.run("Use tools: what time is it in Asia/Kolkata, and what is 100 USD in INR? Reply in one sentence.")
    names = {e["name"] for e in a.log}
    assert names == {"get_time", "convert"}
    assert "8400" in out.replace(",", "")

def test_is_error_recovery():
    a = Agent()
    out = a.run("Convert 10 ZZZ to INR with the convert tool and tell me plainly if it fails.")
    assert any(e["is_error"] for e in a.log)
    assert any(w in out.lower() for w in ["unable", "not", "fail", "cannot", "can't", "unknown", "no rate", "doesn't", "unsupported"])
