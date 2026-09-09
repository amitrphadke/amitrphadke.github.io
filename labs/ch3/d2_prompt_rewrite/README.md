# Lab 3.2 — Rewrite a weak prompt three ways

**Pairs with:** Prompt engineering → Providing examples

## Task
`cases.json` holds 8 support emails and the expected `category` (`billing|bug|feature|other`).
1. `PROMPT_V1` — the weak prompt (given).
2. `PROMPT_V2` — clear + direct + specific: state the allowed labels, the output format (label only), and what to do when unsure.
3. `PROMPT_V3` — V2 plus XML structure and 2–3 examples.
4. `classify(prompt, email) -> str`; `score(prompt) -> float` accuracy over the cases.

The test requires V3 ≥ V2 ≥ V1 - 0.13 and V3 ≥ 0.85.

## Exam angles
- Anthropic's technique order: be clear and direct → use examples (multishot) → let Claude think (CoT) → XML tags → system prompt role → prefill → chain prompts → long-context tips.
- Put long documents **above** the question; put instructions and examples in the system prompt; use XML tags to separate data from instructions.
