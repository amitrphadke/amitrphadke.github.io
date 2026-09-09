from common import MODEL, client

def solve(question: str, thinking: bool, budget: int = 2048):
    # TODO: kwargs; if thinking: kwargs["thinking"]={"type":"enabled","budget_tokens":budget}; max_tokens=budget+800
    # return (answer_text, thinking_text or None, usage)
    raise NotImplementedError

def compare(question: str) -> dict:
    a_off, _, u_off = solve(question, False)
    a_on, th, u_on = solve(question, True)
    return {"off": a_off, "on": a_on, "thinking_chars": len(th or ""), "out_off": u_off.output_tokens, "out_on": u_on.output_tokens}

if __name__ == "__main__":
    from puzzles import PUZZLES
    for q, a in PUZZLES: print(a, compare(q))
