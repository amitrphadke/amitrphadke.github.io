import pytest
from common import has_key
from lab import stream_text, stream_with_events
pytestmark = pytest.mark.skipif(not has_key(), reason="ANTHROPIC_API_KEY not set")

def test_stream_yields_multiple_chunks():
    chunks = list(stream_text("Count from one to twenty in words, comma separated."))
    assert len(chunks) > 3
    assert "twenty" in "".join(chunks).lower()

def test_event_sequence_and_final_usage():
    types, final = stream_with_events("Say hello.", max_tokens=30)
    assert types[0] == "message_start" and types[-1] == "message_stop"
    assert "content_block_start" in types and "content_block_delta" in types and "message_delta" in types
    assert types.index("content_block_start") < types.index("content_block_delta") < types.index("content_block_stop") < types.index("message_delta")
    assert final.usage.output_tokens > 0 and final.stop_reason == "end_turn"
