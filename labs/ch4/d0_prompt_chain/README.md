# Lab 4.0 — Prompt chaining with a programmatic gate

**Pairs with:** Agents and workflows · Chaining workflows

## Task
`chain(topic) -> dict` with steps:
1. `outline(topic)` → 3 bullet points.
2. **gate** `ok_outline(text) -> bool` — exactly 3 lines starting with `-`; if it fails, re-run step 1 once (count in `chain.retries`).
3. `draft(outline)` → a ~80-word paragraph.
4. `polish(draft)` → same paragraph, British spelling, no exclamation marks.
Return `{"outline", "draft", "final"}`.

## Exam angles
- Chaining trades latency for accuracy: each step is small and checkable; **gates** between steps are code, not the model.
- Workflow = predefined code paths; agent = the model decides the path. Prefer the simplest thing that works.
