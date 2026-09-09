import pytest
from common import has_key
from lab import ask_cached, cache_report
pytestmark = pytest.mark.skipif(not has_key(), reason="ANTHROPIC_API_KEY not set")

def test_second_call_reads_cache():
    r1 = cache_report(ask_cached("What is the refund window? One sentence."))
    r2 = cache_report(ask_cached("Who approves discounts over 20%? One sentence."))
    assert r1["cache_creation_input_tokens"] > 0 or r1["cache_read_input_tokens"] > 0
    assert r2["cache_read_input_tokens"] > 1000, r2
    assert r2["input_tokens"] < 200   # only the question is uncached
