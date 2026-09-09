import json
from pathlib import Path
from common import MODEL, client

ATTACKS = json.loads((Path(__file__).parent / "attacks.json").read_text())
SECRET = "PINEAPPLE"
SENT = []

def wrap_untrusted(text: str) -> str:
    # TODO
    raise NotImplementedError

def summarise_safely(doc: str) -> str:
    # TODO
    raise NotImplementedError

TOOLS = [{"name": "send_email", "description": "Send an email.", "input_schema": {"type": "object", "properties": {"to": {"type": "string"}, "body": {"type": "string"}}, "required": ["to", "body"]}}]

class SecureAgent:
    def __init__(self, approve=lambda to: False):
        self.approve = approve
    def run_tool(self, name, args):
        if name == "send_email":
            if not self.approve(args["to"]): raise PermissionError("email requires approval — denied")
            SENT.append(args); return "sent"
        raise ValueError("unknown tool")
    def run(self, prompt: str) -> str:
        # TODO: tool loop; system rule as in summarise_safely; the document must be passed wrapped
        raise NotImplementedError
