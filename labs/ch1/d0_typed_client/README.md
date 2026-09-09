# Lab 1.0 — A typed `ask()`, sync and async

**Pairs with:** Accessing the API · Getting an API key · Making a request
**Time:** 30 min · **Done when:** `python check.py ch1/d0` is green.

## Task
1. Implement `ask(prompt, system="", model=MODEL, max_tokens=300)` that returns the full `Message` object (not just text).
2. Implement `ask_async(...)` with `anthropic.AsyncAnthropic()`.
3. Implement `top_level_keys(message)` returning the sorted list of top-level keys of `message.model_dump()` — you should be able to name every one of them from memory afterwards.

## Exam angles
- `max_tokens` is required and caps **output** only.
- `system` is a top-level parameter, not a message role.
- `stop_reason` is `end_turn` for a normal finish; `max_tokens` means you cut it off.
