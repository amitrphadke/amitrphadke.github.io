# Lab 2.2 — Prompt caching

**Pairs with:** Prompt caching → Prompt caching in action

## Task
1. `big_system()` — return a system prompt of at least ~5 000 tokens (the folder's `policy.txt` repeated is fine).
2. `ask_cached(question) -> Message` — pass the system prompt as a **list of blocks** with `cache_control: {"type":"ephemeral"}` on the last block.
3. `cache_report(m) -> dict` with `cache_creation_input_tokens`, `cache_read_input_tokens`, `input_tokens`.

## Exam angles
- Minimum cacheable prefix: 1024 tokens (Opus/Sonnet), 2048–4096 on Haiku tiers — under that, the breakpoint is silently ignored.
- Cache order: tools → system → messages; anything *before* a breakpoint is cached, changes before it bust it.
- Writes cost 1.25× (5-min TTL) or 2× (1-hour); reads cost 0.1×. Up to 4 breakpoints.
