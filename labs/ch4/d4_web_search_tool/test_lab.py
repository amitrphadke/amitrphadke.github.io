import pytest
from common import has_key
from lab import search_answer, SERVER_VS_CLIENT
pytestmark = pytest.mark.skipif(not has_key(), reason="ANTHROPIC_API_KEY not set")

def test_search_has_citations():
    text, cites = search_answer("What is the current pass score for the Claude Certified Developer Foundations exam? Cite the source.")
    assert len(text) > 20 and len(cites) >= 1
    assert all(getattr(c, "url", None) for c in cites)

def test_definitions_written():
    assert "TODO" not in SERVER_VS_CLIENT["client_tool"] + SERVER_VS_CLIENT["server_tool"]
