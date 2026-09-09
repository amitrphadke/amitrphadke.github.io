# Lab 2.3 — Message Batches

**Pairs with:** no video — Library digest *Message Batches API*

## Task
1. `submit(prompts: list[str]) -> batch_id` — `client.messages.batches.create(requests=[{custom_id, params}])`.
2. `wait(batch_id, timeout=900)` — poll `retrieve()` until `processing_status == "ended"`.
3. `collect(batch_id) -> dict[custom_id, str|None]` — iterate `client.messages.batches.results(batch_id)`; text for `succeeded`, `None` otherwise; also return the counts of the four result types in `collect.counts`.

## Exam angles
- 50 % cheaper, completes within 24 h (usually minutes), up to 100 000 requests / 256 MB per batch.
- Result types: `succeeded`, `errored`, `canceled`, `expired`. Results are **not** in submission order — match by `custom_id`.
- Results are available for 29 days.
