# Lab 4.3 — Orchestrator–workers

**Pairs with:** Agents and tools · Workflows vs agents · Introduction to subagents (whole course)

## Task
1. `worker(subtask) -> str` — a Haiku call with its own system prompt (fresh context, no shared history).
2. `orchestrator(task, max_turns=4) -> dict` — Sonnet with **one** tool `delegate(subtask)`; loop until `end_turn` or `max_turns`; every delegation goes to `worker`; return `{"answer", "delegations": [...], "turns"}`.
3. Enforce `max_turns`: when hit, stop and set `"stopped": "max_turns"`.

## Exam angles
- Orchestrator decides *dynamically* what subtasks exist (vs. parallelisation where they are fixed).
- Subagents get **isolated context** — cheaper and less confused; you must pass them everything they need.
- Always cap turns and budget; agents fail by looping.
