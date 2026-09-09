# Lab 3.3 — Extended thinking on vs off

**Pairs with:** Extended thinking

## Task
1. `solve(question, thinking: bool)` — when `thinking` is true pass `thinking={"type":"enabled","budget_tokens":2048}` and `max_tokens` **greater** than the budget; return `(answer_text, thinking_text_or_None, usage)`.
2. `compare(question)` → dict with both runs' answers and output tokens.

`puzzles.py` has three multi-step puzzles with answers.

## Exam angles
- `budget_tokens` ≥ 1024 and `< max_tokens`; thinking tokens are billed as output.
- Thinking is incompatible with temperature/top_k, forced `tool_choice`, and prefill.
- On Claude 4.6+ prefer `thinking={"type":"adaptive"}` (+ `output_config.effort`); manual budgets are legacy there.
- Use it for maths, multi-step planning, hard code; skip it for lookups, extraction, classification.
