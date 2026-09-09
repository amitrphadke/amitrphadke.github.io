from datetime import datetime
from zoneinfo import ZoneInfo
from common import MODEL, client

TOOLS = [
    {"name": "get_time", "description": "Current local time in an IANA timezone.",
     "input_schema": {"type": "object", "properties": {"timezone": {"type": "string", "description": "IANA name, e.g. Asia/Kolkata"}}, "required": ["timezone"]}},
]

def run_tool(name: str, args: dict) -> str:
    if name == "get_time":
        return datetime.now(ZoneInfo(args["timezone"])).strftime("%H:%M on %A")
    raise ValueError(f"unknown tool {name}")

def run_tool_loop(prompt: str, max_rounds: int = 5):
    messages = [{"role": "user", "content": prompt}]
    rounds = 0
    # TODO: loop as described in the README
    raise NotImplementedError

if __name__ == "__main__":
    print(run_tool_loop("What time is it in Kolkata right now? Answer in one sentence."))
