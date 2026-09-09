import time
import anthropic
from common import MODEL

def classify(status: int) -> str:
    # TODO
    raise NotImplementedError

RETRYABLE = (anthropic.RateLimitError, anthropic.InternalServerError, anthropic.APIConnectionError)

def with_backoff(fn, max_attempts: int = 4, base: float = 0.01):
    # TODO: for attempt in range(max_attempts): try fn(); except RETRYABLE as e: ...sleep...; raise last
    raise NotImplementedError

def client_with_retries(n: int = 3, timeout: float = 30.0) -> anthropic.Anthropic:
    return anthropic.Anthropic(api_key="dummy", max_retries=n, timeout=timeout)
