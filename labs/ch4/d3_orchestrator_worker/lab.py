from common import MODEL, client

WORKER_MODEL = "claude-haiku-4-5"
ORCH_MODEL = MODEL

DELEGATE = {"name": "delegate", "description": "Hand a self-contained subtask to a worker and get its result.",
            "input_schema": {"type": "object", "properties": {"subtask": {"type": "string"}}, "required": ["subtask"]}}

def worker(subtask: str) -> str:
    # TODO: Haiku call, system="You are a focused worker. Answer the subtask completely and concisely."
    raise NotImplementedError

def orchestrator(task: str, max_turns: int = 4) -> dict:
    out = {"answer": "", "delegations": [], "turns": 0}
    # TODO: tool loop with DELEGATE; stop on end_turn or when turns == max_turns (set out["stopped"]="max_turns")
    raise NotImplementedError
