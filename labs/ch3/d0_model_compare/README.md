# Lab 3.0 — One task, three models

**Pairs with:** Claude Platform 101 → Choosing the right model

## Task
`compare(task, models) -> list[dict]` — for each model run the task once and record `model`, `latency_s`, `input_tokens`, `output_tokens`, `cost_usd` (use `PRICES` from `common`), `answer`. Print it as a table in `__main__`.

Models to use: `claude-haiku-4-5`, `claude-sonnet-4-5` and whichever Opus your key can access (`OPUS` in `common`; the test only requires two rows to succeed).

## Exam angles
- Haiku: fastest/cheapest — classification, extraction, routing, moderation. Sonnet: default workhorse. Opus: hardest reasoning, agentic coding, long-horizon planning.
- Same request ≈ same tokens; **price per token** and latency are what change. Choose the cheapest model that passes your eval.
