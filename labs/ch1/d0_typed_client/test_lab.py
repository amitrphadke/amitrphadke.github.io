import asyncio, pytest
from common import has_key
from lab import ask, ask_async, top_level_keys
pytestmark = pytest.mark.skipif(not has_key(), reason="ANTHROPIC_API_KEY not set")

def test_ask_returns_message_with_usage():
    m = ask("Reply with the single word: pong", max_tokens=20)
    assert m.role == "assistant" and m.type == "message"
    assert m.stop_reason == "end_turn"
    assert m.usage.input_tokens > 0 and m.usage.output_tokens > 0
    assert "pong" in m.content[0].text.lower()

def test_max_tokens_caps_output():
    m = ask("Write 300 words about clouds.", max_tokens=15)
    assert m.stop_reason == "max_tokens"

def test_system_prompt_applied():
    m = ask("What is your name?", system="You are Zed. Always begin your reply with the word ZED.", max_tokens=30)
    assert m.content[0].text.strip().upper().startswith("ZED")

def test_async_version():
    m = asyncio.run(ask_async("Reply with the single word: pong", max_tokens=20))
    assert "pong" in m.content[0].text.lower()

def test_top_level_keys():
    m = ask("hi", max_tokens=5)
    keys = top_level_keys(m)
    for k in ["id", "type", "role", "model", "content", "stop_reason", "stop_sequence", "usage"]:
        assert k in keys
