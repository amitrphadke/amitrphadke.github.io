from datetime import datetime
from zoneinfo import ZoneInfo
from common import MODEL, client

RATES = {("USD", "INR"): 84.0, ("INR", "USD"): 1 / 84.0, ("EUR", "INR"): 91.0}

TOOLS = [
    {"name": "get_time", "description": "Current local time in an IANA timezone.",
     "input_schema": {"type": "object", "properties": {"timezone": {"type": "string"}}, "required": ["timezone"]}},
    {"name": "convert", "description": "Convert an amount between currencies using today's rate.",
     "input_schema": {"type": "object", "properties": {"amount": {"type": "number"}, "from_currency": {"type": "string"}, "to_currency": {"type": "string"}},
                      "required": ["amount", "from_currency", "to_currency"]}},
]

class Agent:
    def __init__(self, model: str = MODEL):
        self.model, self.log = model, []

    def run_tool(self, name: str, args: dict) -> str:
        if name == "get_time":
            return datetime.now(ZoneInfo(args["timezone"])).strftime("%H:%M")
        if name == "convert":
            key = (args["from_currency"].upper(), args["to_currency"].upper())
            if key not in RATES: raise ValueError(f"no rate for {key[0]}->{key[1]}")
            return f"{args['amount'] * RATES[key]:.2f} {key[1]}"
        raise ValueError(f"unknown tool {name}")

    def run(self, prompt: str, max_rounds: int = 6) -> str:
        # TODO: loop; for each tool_use block try/except -> tool_result (is_error on exception); append to self.log
        raise NotImplementedError

if __name__ == "__main__":
    a = Agent(); print(a.run("Time in Asia/Kolkata and 100 USD in INR, please.")); print(a.log)
