# Lab 3.1 — Cost calculator and token counting

**Pairs with:** no video — Library digests *Pricing* and *Token counting*

## Task
1. `estimate(model, input_tokens, output_tokens, cache_read=0, cache_write=0) -> float` USD, using `PRICES` (per-million: `in`, `out`; cache read = 0.1 × in, cache write (5-min) = 1.25 × in).
2. `count(messages, system=None, model=MODEL) -> int` via `client.messages.count_tokens` (free, no output).
3. `scenarios()` — return the four rows of the table: baseline Sonnet, Sonnet + caching (90 % of input cached), Haiku, Haiku + caching, for a 10 000-in / 500-out request × 1 000 calls.

## Exam angles
- Optimisation order that dominates cost: **model choice → caching → prompt length → output length**; Batches then halves whatever is left.
- `count_tokens` supports tools, system, images and PDFs — use it to check a prompt before sending.
