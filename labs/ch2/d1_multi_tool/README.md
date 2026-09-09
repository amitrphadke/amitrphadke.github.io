# Lab 2.1 — Multiple tools, parallel calls and `is_error`

**Pairs with:** Multi-turn conversations with tools → Fine grained tool calling

## Task
Extend the loop from 2.0 into `Agent`:
- tools `get_time(timezone)` and `convert(amount, from_currency, to_currency)` (use a fixed rate table; **raise** on an unknown currency).
- Every tool round-trip is appended to `self.log` as `{"name", "input", "output", "is_error"}`.
- Exceptions inside a tool become a `tool_result` with `is_error: True` and the error text — the model should recover and tell the user.
- Parallel calls: when one assistant turn has two `tool_use` blocks, both results go in **one** user message.
- `run(prompt) -> str`.

## Exam angles
- `is_error` lets the model recover; a Python exception that escapes kills the loop.
- `tool_choice`: `auto` (default) · `any` (must use one) · `tool` (this one) · `none`; `disable_parallel_tool_use: true` forces one at a time.
