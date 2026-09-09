import time, pytest
from common import has_key
from lab import route, handle_many, vote
pytestmark = pytest.mark.skipif(not has_key(), reason="ANTHROPIC_API_KEY not set")
TICKETS = ["I was charged twice, I want my money back.", "The app crashes when I upload a PDF.",
           "Can we get pricing for 50 seats?", "What are your office hours?"]

def test_route():
    assert [route(t) for t in TICKETS] == ["refund", "technical", "sales", "other"]

def test_parallel_is_fast():
    t0 = time.time(); out = handle_many(TICKETS); dt = time.time() - t0
    assert len(out) == 4 and all(len(r[1]) > 10 for r in out)
    assert dt < 12, f"took {dt:.1f}s — are the calls really concurrent?"

def test_vote():
    assert vote("Is water wet? Answer yes or no.").strip().lower().startswith("yes")
