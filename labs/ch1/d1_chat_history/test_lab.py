import pytest
from common import has_key
from lab import Chat
pytestmark = pytest.mark.skipif(not has_key(), reason="ANTHROPIC_API_KEY not set")

def test_history_alternates_and_remembers():
    c = Chat("Answer in one short sentence.")
    c.send("My favourite colour is teal. Just acknowledge.")
    c.send("My dog is called Bolt. Just acknowledge.")
    a = c.send("What is my favourite colour and my dog's name?")
    assert "teal" in a.lower() and "bolt" in a.lower()
    roles = [m["role"] for m in c.history]
    assert roles == ["user", "assistant"] * 3

def test_input_tokens_grow_each_turn():
    c = Chat()
    for i in range(3): c.send(f"Turn {i}: reply with one word.", max_tokens=10)
    ins = [i for i, _ in c.usage_log]
    assert ins[0] < ins[1] < ins[2], ins
