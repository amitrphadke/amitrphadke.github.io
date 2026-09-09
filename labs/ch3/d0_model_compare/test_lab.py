import pytest
from common import has_key
from lab import compare
pytestmark = pytest.mark.skipif(not has_key(), reason="ANTHROPIC_API_KEY not set")

def test_compare_two_tiers():
    rows = compare("Reply with the single word: ready", ["claude-haiku-4-5", "claude-sonnet-4-5"], max_tokens=10)
    ok = [r for r in rows if "error" not in r]
    assert len(ok) == 2
    for r in ok:
        assert r["latency_s"] > 0 and r["input_tokens"] > 0 and r["cost_usd"] > 0 and "ready" in r["answer"].lower()
    haiku, sonnet = ok
    assert haiku["cost_usd"] < sonnet["cost_usd"]
