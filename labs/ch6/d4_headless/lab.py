import json, subprocess

def run_headless(prompt: str, cwd: str) -> dict:
    # TODO
    raise NotImplementedError

def result_text(d: dict) -> str:
    return d.get("result", "")

def cost(d: dict) -> float:
    return float(d.get("total_cost_usd", 0))
