# Lab 7.2 — Moderation pre-check with Haiku

**Pairs with:** docs *Usage policy* / *Content moderation* (Library). `inputs.json` has 10 test inputs with expected verdicts.

## Task
1. `moderate(text) -> dict` — Haiku, forced tool `verdict` with `allowed: bool`, `category: str` (`ok|harassment|self_harm|pii|other`), `reason: str`.
2. `guarded_answer(text)` — if not allowed, return a polite refusal string without calling the main model; else answer normally.
3. Handle a model **refusal** gracefully: if `stop_reason == "refusal"`, return a fixed message.

## Exam angles
- Cheap model first as a gate = cost + safety. `stop_reason: "refusal"` exists (Claude 4+) — handle it like any other stop reason.
- PII: don't store, redact before logging, minimise what you send.
