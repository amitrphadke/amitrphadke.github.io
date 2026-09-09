import pytest
from common import has_key
from lab import solve
from puzzles import PUZZLES
pytestmark = pytest.mark.skipif(not has_key(), reason="ANTHROPIC_API_KEY not set")

def test_thinking_block_present_and_answer_correct():
    q, ans = PUZZLES[0]
    text, thinking, usage = solve(q + " Give only the final number at the end after the words FINAL ANSWER:", True)
    assert thinking and len(thinking) > 50
    assert ans in text.split("FINAL ANSWER")[-1]
    assert usage.output_tokens > 100
