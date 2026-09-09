# Lab 4.5 — Guards: max turns, cost budget, approval

**Pairs with:** Quiz on agents and workflows · Using subagents effectively

## Task
Build `GuardedAgent` around the tool loop:
- tools: `read_note(name)`, `delete_note(name)` (in-memory dict `NOTES`).
- `max_turns` and `budget_usd` (use `cost_usd` from `common`); stop with `stopped = "max_turns" | "budget" | "done"`.
- `delete_note` is **destructive**: it must not run unless `approve(name) -> bool` returns True; the default approver denies and the tool result says so (`is_error`).
- Detect a loop: the same tool called with the same input 3× in a row → `stopped = "loop"`.

## Exam angles
- Failure modes the exam names: infinite loops, runaway cost, hallucinated tools, lost context, destructive actions without a human.
- Human-in-the-loop for irreversible actions; least privilege on tools.
