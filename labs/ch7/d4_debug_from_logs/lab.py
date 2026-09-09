import json
from pathlib import Path

DIAGNOSTIC_CHECKLIST = [
    # TODO: 6 questions in order
]

def diagnose(record: dict) -> str:
    # TODO
    raise NotImplementedError

def load_logs() -> list[dict]:
    return [json.loads(p.read_text()) for p in sorted((Path(__file__).parent / "logs").glob("*.json"))]
