import asyncio, time
from collections import Counter
from common import MODEL, client, aclient

LABELS = ["refund", "technical", "sales", "other"]
HANDLERS = {
    "refund": "You are a billing agent. Explain the refund policy (30 days) in two sentences.",
    "technical": "You are a support engineer. Ask for logs and give one likely cause in two sentences.",
    "sales": "You are a sales rep. Offer a demo in two sentences.",
    "other": "You are a receptionist. Politely redirect in one sentence.",
}

def route(ticket: str) -> str:
    # TODO: Haiku, label only
    raise NotImplementedError

def handle(ticket: str):
    label = route(ticket)
    # TODO: reply with HANDLERS[label] as system
    raise NotImplementedError

async def _handle_async(ticket: str):
    # TODO: async versions of route + reply
    raise NotImplementedError

def handle_many(tickets: list[str]) -> list:
    return asyncio.run(asyncio.gather(*[_handle_async(t) for t in tickets]))

def vote(question: str, n: int = 3) -> str:
    # TODO: n parallel calls (asyncio.gather), each answering with one word; return the majority
    raise NotImplementedError
