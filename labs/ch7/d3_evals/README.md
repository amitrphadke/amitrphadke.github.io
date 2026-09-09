# Lab 7.3 — Evals

**Pairs with:** Prompt evaluation → Code based grading. `cases.json` = 10 cases (`input`, `expected`) for a "extract the invoice total" task.

## Task
1. `run_case(prompt, case) -> str`; `grade_exact(out, expected) -> bool` (normalise whitespace/currency symbols).
2. `grade_llm(out, expected) -> bool` — Haiku as judge, forced tool with `pass: bool`.
3. `evaluate(prompt, grader) -> dict(score, failures)`.
4. `GOOD_PROMPT` scores ≥ 0.9; `BAD_PROMPT` (given — asks for a sentence instead of a number) scores lower — the harness must **detect the regression** (`evaluate(GOOD) > evaluate(BAD)`).

## Exam angles
- Workflow: dataset → run → grade (code-based when possible; model-based for open-ended) → track over time; evals gate prompt/model changes in CI.
- Keep graders deterministic where you can; LLM judges need a rubric and spot-checks.
