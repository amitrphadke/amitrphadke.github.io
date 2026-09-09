import pytest
from common import has_key
from lab import mcp_request, DECISION_RULE
pytestmark = pytest.mark.skipif(not has_key(), reason="ANTHROPIC_API_KEY not set")

def test_remote_mcp_tool_was_used():
    m = mcp_request("Using the deepwiki tools, what does the GitHub repo anthropics/anthropic-sdk-python provide? One sentence.")
    types = [getattr(b, "type", "") for b in m.content]
    assert any(t.startswith("mcp_tool_use") for t in types), types
    assert any(t == "text" for t in types)

def test_rule_written():
    assert "TODO" not in DECISION_RULE and len(DECISION_RULE) > 80
