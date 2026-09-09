# Lab 7.4 — Diagnose from logs (offline)

**Pairs with:** docs *Stop reasons*, *Errors*, *Tool use* — the debugging checklist. `logs/` has 6 JSON request/response captures.

## Task
`diagnose(record: dict) -> str` returning one of:
`truncated` (stop_reason max_tokens), `unanswered_tool` (assistant tool_use with no following tool_result), `role_order` (two same-role messages in a row / first not user), `rate_limited` (429), `cache_miss` (cache_control present but `cache_read_input_tokens == 0` on a repeat call flagged `repeat: true`), `ok`.
Then `DIAGNOSTIC_CHECKLIST` — 6 questions you ask first, in order.

## Exam angles
- First look at `stop_reason` and `usage`, then the message list, then headers. Most "the model is broken" reports are `max_tokens`, a missing `tool_result`, or role order.
