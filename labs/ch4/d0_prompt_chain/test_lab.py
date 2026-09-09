import pytest
from common import has_key
from lab import chain, ok_outline
pytestmark = pytest.mark.skipif(not has_key(), reason="ANTHROPIC_API_KEY not set")

def test_gate():
    assert ok_outline("- a\n- b\n- c") and not ok_outline("- a\n- b") and not ok_outline("1. a\n2. b\n3. c")

def test_chain_runs():
    r = chain("why DevOps teams adopt GitOps")
    assert ok_outline(r["outline"])
    assert 40 <= len(r["final"].split()) <= 160
    assert "!" not in r["final"]
