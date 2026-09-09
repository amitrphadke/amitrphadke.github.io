import json, re
from pathlib import Path
from common import MODEL, client

CASES = json.loads((Path(__file__).parent / "cases.json").read_text())
BAD_PROMPT = "Read the invoice text and write a friendly sentence about how much is due."
GOOD_PROMPT = "TODO: extract the grand total; reply with the number only, no currency symbol, two decimals."

def run_case(prompt: str, case: dict) -> str:
    # TODO
    raise NotImplementedError

def grade_exact(out: str, expected: str) -> bool:
    norm = lambda s: re.sub(r"[^0-9.]", "", s)
    return norm(out) == norm(expected)

def grade_llm(out: str, expected: str) -> bool:
    # TODO: Haiku judge with forced tool {"pass": bool}
    raise NotImplementedError

def evaluate(prompt: str, grader=grade_exact) -> dict:
    fails = [c for c in CASES if not grader(run_case(prompt, c), c["expected"])]
    return {"score": 1 - len(fails) / len(CASES), "failures": fails}
