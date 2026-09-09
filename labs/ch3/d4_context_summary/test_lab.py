import pytest
from common import has_key
from lab import Chat
pytestmark = pytest.mark.skipif(not has_key(), reason="ANTHROPIC_API_KEY not set")

def test_compaction_keeps_facts():
    c = Chat("Be brief.", budget_tokens=900)
    c.send("Remember: my project codename is FALCON-7. Acknowledge in three words.")
    filler = "Here is some text to read, just acknowledge it briefly: " + ("lorem ipsum dolor sit amet " * 60)
    for _ in range(4): c.send(filler, max_tokens=20)
    assert c.compactions >= 1
    a = c.send("What is my project codename?")
    assert "FALCON" in a.upper()
    roles = [m["role"] for m in c.history]
    assert all(roles[i] != roles[i + 1] for i in range(len(roles) - 1)) and roles[0] == "user"
