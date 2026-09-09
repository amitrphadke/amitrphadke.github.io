# Lab 1.1 — Multi-turn chat that keeps history

**Pairs with:** Multi-turn conversations · System prompts

## Task
Implement class `Chat`:
- `Chat(system="")`, `.history` (list of `{role, content}` dicts), `.send(text) -> str` appends the user turn, calls the API with the **whole** history, appends the assistant turn, returns the text.
- `.usage_log` — list of `(input_tokens, output_tokens)` per call.
- `.total_input_tokens()`.

## Exam angles
- The API is stateless: **you** resend the history every turn — that is why input tokens grow.
- Roles must alternate user/assistant and the first must be user.
- Assistant history entries can be the content-block list straight from the response.
