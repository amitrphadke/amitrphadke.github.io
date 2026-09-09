import pytest
from common import has_key
from lab import orchestrator
pytestmark = pytest.mark.skipif(not has_key(), reason="ANTHROPIC_API_KEY not set")

def test_delegates_and_answers():
    r = orchestrator("Produce a two-line release note: line 1 = one benefit of prompt caching, line 2 = one benefit of the Batches API. Delegate each line to a worker, then combine.")
    assert len(r["delegations"]) >= 2 and r["turns"] >= 1
    assert "cach" in r["answer"].lower() and "batch" in r["answer"].lower()

def test_max_turns_enforced():
    r = orchestrator("Delegate one subtask at a time, ten separate times, each 'count to N' for N=1..10, never combining. Only stop after all ten.", max_turns=2)
    assert r["turns"] <= 2 and r.get("stopped") == "max_turns"
