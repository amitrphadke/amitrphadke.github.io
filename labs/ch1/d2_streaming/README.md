# Lab 1.2 — Streaming

**Pairs with:** Response streaming

## Task
1. `stream_text(prompt) -> Iterator[str]` yields text deltas as they arrive (`client.messages.stream(...)` + `.text_stream`).
2. `stream_with_events(prompt) -> (event_types: list[str], final_message)` collects the **type of every raw event** in order and returns the final assembled message (`stream.get_final_message()`).

## Exam angles
- Event order: `message_start → content_block_start → content_block_delta* → content_block_stop → message_delta → message_stop`.
- `usage.output_tokens` is only final in `message_delta`; `message_start` carries the input tokens.
- Streaming doesn't change cost — it changes time-to-first-token.
