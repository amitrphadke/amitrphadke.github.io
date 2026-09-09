# Lab 2.0 — Your first tool loop

**Pairs with:** Introducing tool use → Sending tool results

## Task
1. `TOOLS` — a list with one tool `get_time` (`input_schema` with a `timezone` string, e.g. `Asia/Kolkata`).
2. `run_tool(name, args) -> str` — implement `get_time` with `zoneinfo`.
3. `run_tool_loop(prompt) -> (final_text, rounds)` — loop: call the model; if `stop_reason == "tool_use"`, run every `tool_use` block, append the assistant message and a user message of `tool_result` blocks (`tool_use_id` matching), and continue; stop on `end_turn`. `rounds` = number of tool round-trips.

## Exam angles
- `stop_reason: "tool_use"` means *you* must act; the assistant turn is appended **unchanged** and the results go in the next **user** turn.
- A `tool_result` must reference `tool_use_id`; every `tool_use` needs a result before the next call, or you get a 400.
