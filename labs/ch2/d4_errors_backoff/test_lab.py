import httpx, anthropic, pytest
from lab import classify, with_backoff, client_with_retries, RETRYABLE

def _err(cls, status, headers=None):
    req = httpx.Request("POST", "https://api.anthropic.com/v1/messages")
    resp = httpx.Response(status, request=req, headers=headers or {}, json={"error": {"type": "x", "message": "x"}})
    return cls("boom", response=resp, body=None)

def test_classify():
    assert [classify(s) for s in (400, 401, 429, 500, 529, 418)] == ["client", "client", "retry", "retry", "retry", "unknown"]

def test_retries_then_succeeds():
    calls = {"n": 0}
    def flaky():
        calls["n"] += 1
        if calls["n"] < 3: raise _err(anthropic.RateLimitError, 429, {"retry-after": "0"})
        return "ok"
    assert with_backoff(flaky) == "ok" and calls["n"] == 3

def test_client_error_not_retried():
    calls = {"n": 0}
    def bad():
        calls["n"] += 1; raise _err(anthropic.BadRequestError, 400)
    with pytest.raises(anthropic.BadRequestError): with_backoff(bad)
    assert calls["n"] == 1

def test_gives_up_after_max():
    def always(): raise _err(anthropic.InternalServerError, 500)
    with pytest.raises(anthropic.InternalServerError): with_backoff(always, max_attempts=3)

def test_sdk_retry_setting():
    assert client_with_retries(5).max_retries == 5
