# Lab 2.4 — Errors, retries and backoff

**Pairs with:** no video — Library digests *Errors* and *Rate limits*. Runs fully offline.

## Task
1. `classify(status: int) -> str` returning who fixes it: `"client"` (400, 401, 403, 404, 413), `"retry"` (429, 500, 529), `"unknown"` otherwise.
2. `with_backoff(fn, max_attempts=4, base=0.01)` — call `fn()`; on `anthropic.RateLimitError`, `anthropic.InternalServerError` or `anthropic.APIConnectionError` sleep `base * 2**attempt` (honour a `retry-after` header if the error has one) and retry; re-raise other errors immediately; raise the last error after `max_attempts`.
3. `client_with_retries(n)` — an `anthropic.Anthropic(max_retries=n, timeout=...)` — the SDK already retries 429/5xx twice by default.

## Exam angles
- 429 = rate limit (RPM / ITPM / OTPM), read `retry-after`; 529 = overloaded (retry); 500 = Anthropic's fault (retry); 400/401/403 are **yours**.
- `anthropic-ratelimit-*` headers tell you your remaining budget.
