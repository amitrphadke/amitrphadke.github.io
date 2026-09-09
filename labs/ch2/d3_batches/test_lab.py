import pytest
from common import has_key
from lab import submit, wait, collect
pytestmark = pytest.mark.skipif(not has_key(), reason="ANTHROPIC_API_KEY not set")

def test_batch_roundtrip():
    prompts = [f"What is {i} times 3? Reply with the number only." for i in range(20)]
    b = submit(prompts)
    assert b.startswith("msgbatch_")
    wait(b, timeout=1500)
    res = collect(b)
    assert len(res) == 20 and all(f"q{i}" in res for i in range(20))
    assert "21" in (res["q7"] or "")
    assert collect.counts["succeeded"] >= 18
