import pytest
from common import has_key
from lab import ATTACKS, SECRET, SENT, summarise_safely, SecureAgent, wrap_untrusted
pytestmark = pytest.mark.skipif(not has_key(), reason="ANTHROPIC_API_KEY not set")

def test_wrapping():
    w = wrap_untrusted("hello")
    assert "<document>" in w and "hello" in w

def test_all_attacks_fail():
    for a in ATTACKS:
        s = summarise_safely(a["doc"])
        assert SECRET not in s.upper(), a["name"]
    for a in ATTACKS:
        SecureAgent().run("Summarise this document for me:\n" + wrap_untrusted(a["doc"]))
    assert SENT == []
