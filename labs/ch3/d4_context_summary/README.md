# Lab 3.4 — Context engineering: summarise past N tokens

**Pairs with:** Claude Platform 101 → Context management

## Task
Extend `Chat` from lab 1.1:
- `Chat(system, budget_tokens=1500)`.
- Before each call, if `count_tokens` of the current history exceeds `budget_tokens`, replace all but the last 2 turns with a single user message `"<summary>…</summary>"` produced by a separate Haiku call, followed by an assistant `"Understood."` (roles must still alternate).
- `.compactions` counts how many times this happened; the summary must keep facts the user stated.

## Exam angles
- The context window is a hard limit; nearing it degrades quality before it errors.
- Techniques: summarise, truncate oldest, retrieve on demand (RAG), move stable content to the cached system prompt, put long docs first.
