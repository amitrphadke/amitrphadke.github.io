import pytest
from common import has_key, PRICES
from lab import estimate, count, scenarios

def test_estimate_matches_price_table():
    p = PRICES["claude-sonnet-4-5"]
    assert abs(estimate("claude-sonnet-4-5", 1_000_000, 0) - p["in"]) < 1e-6
    assert abs(estimate("claude-sonnet-4-5", 0, 1_000_000) - p["out"]) < 1e-6
    assert abs(estimate("claude-sonnet-4-5", 0, 0, cache_read=1_000_000) - 0.1 * p["in"]) < 1e-6
    assert abs(estimate("claude-sonnet-4-5", 0, 0, cache_write=1_000_000) - 1.25 * p["in"]) < 1e-6

def test_scenarios_show_caching_and_model_choice_dominate():
    rows = {r["name"]: r["usd"] for r in scenarios()}
    assert len(rows) == 4
    assert rows["sonnet+cache"] < rows["sonnet"] and rows["haiku"] < rows["sonnet"] and rows["haiku+cache"] < rows["haiku"]

@pytest.mark.skipif(not has_key(), reason="ANTHROPIC_API_KEY not set")
def test_count_tokens_endpoint():
    n = count([{"role": "user", "content": "Hello there, how are you today?"}])
    assert 5 < n < 40
