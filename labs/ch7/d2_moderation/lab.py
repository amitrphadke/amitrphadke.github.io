import json
from pathlib import Path
from common import client

INPUTS = json.loads((Path(__file__).parent / "inputs.json").read_text())
VERDICT = {"name": "verdict", "description": "Moderation verdict.", "input_schema": {"type": "object", "properties": {
    "allowed": {"type": "boolean"}, "category": {"type": "string", "enum": ["ok", "harassment", "self_harm", "pii", "other"]}, "reason": {"type": "string"}}, "required": ["allowed", "category", "reason"]}}

def moderate(text: str) -> dict:
    # TODO: claude-haiku-4-5, tools=[VERDICT], tool_choice forced; return block.input
    raise NotImplementedError

def guarded_answer(text: str) -> str:
    # TODO
    raise NotImplementedError
