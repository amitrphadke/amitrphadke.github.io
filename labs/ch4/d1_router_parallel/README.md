# Lab 4.1 — Routing and parallelisation

**Pairs with:** Routing workflows · Parallelization workflows

## Task
1. `route(ticket) -> str` — Haiku classifies into `refund|technical|sales|other` (label only).
2. `HANDLERS` — a dict label → specialised system prompt; `handle(ticket) -> (label, reply)`.
3. `handle_many(tickets) -> list` — run all tickets **concurrently** with `asyncio.gather` and the async client; must be faster than serial (test compares wall-time against `len(tickets) * 0.5 s`).
4. `vote(question, n=3) -> str` — sectioning/voting: ask n times in parallel, majority answer.

## Exam angles
- Routing: cheap classifier first, specialised prompt/model second — the classic cost/quality trick.
- Parallelisation: *sectioning* (independent subtasks) vs *voting* (same task n times).
