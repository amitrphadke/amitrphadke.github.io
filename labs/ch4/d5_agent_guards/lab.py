from common import MODEL, client, cost_usd

NOTES = {"todo": "buy milk", "secret": "do not delete"}

TOOLS = [
    {"name": "read_note", "description": "Read a note by name.", "input_schema": {"type": "object", "properties": {"name": {"type": "string"}}, "required": ["name"]}},
    {"name": "delete_note", "description": "Delete a note by name. Irreversible.", "input_schema": {"type": "object", "properties": {"name": {"type": "string"}}, "required": ["name"]}},
]

class GuardedAgent:
    def __init__(self, max_turns: int = 5, budget_usd: float = 0.01, approve=lambda name: False, model: str = MODEL):
        self.max_turns, self.budget, self.approve, self.model = max_turns, budget_usd, approve, model
        self.spent, self.turns, self.stopped, self.calls = 0.0, 0, None, []

    def run_tool(self, name, args):
        if name == "read_note": return NOTES.get(args["name"], "(no such note)")
        if name == "delete_note":
            if not self.approve(args["name"]): raise PermissionError("delete_note requires human approval — denied")
            NOTES.pop(args["name"], None); return "deleted"
        raise ValueError("unknown tool")

    def run(self, prompt: str) -> str:
        # TODO: loop with guards; append (name, json.dumps(input)) to self.calls; loop detection on last 3 calls
        raise NotImplementedError
