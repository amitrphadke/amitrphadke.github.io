import pytest
from common import has_key
from lab import evaluate, GOOD_PROMPT, BAD_PROMPT, grade_exact, grade_llm
pytestmark = pytest.mark.skipif(not has_key(), reason="ANTHROPIC_API_KEY not set")

def test_exact_grader():
    assert grade_exact("₹ 1,234.50", "1234.50") and not grade_exact("1234", "1234.50")

def test_detects_regression():
    assert "TODO" not in GOOD_PROMPT
    good, bad = evaluate(GOOD_PROMPT)["score"], evaluate(BAD_PROMPT)["score"]
    assert good >= 0.9 and good > bad, (good, bad)

def test_llm_judge():
    assert grade_llm("The total due is 1234.50", "1234.50") is True
    assert grade_llm("The total due is 99.00", "1234.50") is False
