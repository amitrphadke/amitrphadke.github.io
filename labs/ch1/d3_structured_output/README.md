# Lab 1.3 — Validated JSON with retry

**Pairs with:** Structured data

## Task
Implement `extract_person(text) -> Person` (pydantic model: `name: str`, `age: int`, `city: str`) three ways and make `extract_person` use the most reliable:
1. `via_instruction(text)` — ask for JSON only, `json.loads`, validate, **retry once** appending the validation error.
2. `via_tool(text)` — define a tool `record_person` whose `input_schema` is `Person.model_json_schema()` and force it with `tool_choice={"type":"tool","name":"record_person"}`; parse `block.input`.
3. `extract_person` = tool route.

Count attempts in `extract_person.attempts` (module-level counter is fine) so the test can see retries.

## Exam angles
- Reliability order: plain instruction < prefill (legacy) < forced tool < structured outputs (`output_config.format`, on models that support it).
- Always validate; treat model output as untrusted input.
