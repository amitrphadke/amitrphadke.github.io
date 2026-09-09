import json
from pathlib import Path
from common import MODEL, client

CASES = json.loads((Path(__file__).parent / "cases.json").read_text())
LABELS = ["billing", "bug", "feature", "other"]

PROMPT_V1 = "Categorise this email."
PROMPT_V2 = """TODO: clear, direct, specific — allowed labels, output format (the label only), tie-break rule."""
PROMPT_V3 = """TODO: V2 + <instructions>/<examples>/<email> XML structure with 2-3 examples."""

def classify(prompt: str, email: str) -> str:
    # TODO: system=prompt, user=email (wrap in <email> for V3), max_tokens=10; return the label found in the reply (lowercase, first matching LABELS word) or "other"
    raise NotImplementedError

def score(prompt: str) -> float:
    return sum(classify(prompt, c["email"]) == c["category"] for c in CASES) / len(CASES)

if __name__ == "__main__":
    for n, p in [("v1", PROMPT_V1), ("v2", PROMPT_V2), ("v3", PROMPT_V3)]:
        print(n, score(p))
