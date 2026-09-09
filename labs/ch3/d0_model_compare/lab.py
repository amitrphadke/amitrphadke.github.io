import time
from common import client, PRICES, cost_usd, OPUS

def compare(task: str, models: list[str], max_tokens: int = 150) -> list[dict]:
    rows = []
    for m in models:
        try:
            # TODO: time the call, fill the row (use cost_usd(model, usage))
            raise NotImplementedError
        except NotImplementedError: raise
        except Exception as e:
            rows.append({"model": m, "error": str(e)[:80]})
    return rows

if __name__ == "__main__":
    for r in compare("Explain idempotency in one sentence.", ["claude-haiku-4-5", "claude-sonnet-4-5", OPUS]):
        print(r)
