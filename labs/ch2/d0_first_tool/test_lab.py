import pytest
from common import has_key
from lab import run_tool_loop, TOOLS
pytestmark = pytest.mark.skipif(not has_key(), reason="ANTHROPIC_API_KEY not set")

def test_schema_shape():
    t = TOOLS[0]
    assert t["name"] == "get_time" and t["input_schema"]["type"] == "object" and "timezone" in t["input_schema"]["required"]

def test_loop_calls_tool_then_answers():
    text, rounds = run_tool_loop("What time is it right now in Asia/Kolkata? Use the tool. One sentence.")
    assert rounds >= 1
    assert any(w in text.lower() for w in ["kolkata", ":", "am", "pm", "o'clock"])

def test_no_tool_needed():
    text, rounds = run_tool_loop("What is 2 + 2? Reply with just the number.")
    assert rounds == 0 and "4" in text
