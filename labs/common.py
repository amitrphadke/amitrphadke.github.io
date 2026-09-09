"""Shared helpers for every lab. Loads labs/.env (ANTHROPIC_API_KEY, GH_TOKEN, CCDVF_MODEL)."""
import os
from pathlib import Path
from dotenv import load_dotenv
import anthropic

load_dotenv(Path(__file__).resolve().parent / ".env")

MODEL = os.getenv("CCDVF_MODEL", "claude-haiku-4-5")      # cheapest tier; override per lab where the README says so
OPUS = os.getenv("CCDVF_OPUS", "claude-opus-4-5")

# USD per million tokens — check https://docs.claude.com/en/docs/about-claude/pricing before quoting in notes
PRICES = {
    "claude-haiku-4-5":  {"in": 1.0,  "out": 5.0},
    "claude-sonnet-4-5": {"in": 3.0,  "out": 15.0},
    "claude-sonnet-4-6": {"in": 3.0,  "out": 15.0},
    "claude-opus-4-1":   {"in": 15.0, "out": 75.0},
    "claude-opus-4-5":   {"in": 5.0,  "out": 25.0},
    "claude-opus-4-6":   {"in": 5.0,  "out": 25.0},
}

def has_key() -> bool:
    return bool(os.getenv("ANTHROPIC_API_KEY"))

def client() -> anthropic.Anthropic:
    return anthropic.Anthropic()

def aclient() -> anthropic.AsyncAnthropic:
    return anthropic.AsyncAnthropic()

def cost_usd(model: str, usage) -> float:
    p = PRICES.get(model) or PRICES.get(model.rsplit("-", 1)[0]) or PRICES["claude-sonnet-4-5"]
    cr = getattr(usage, "cache_read_input_tokens", 0) or 0
    cw = getattr(usage, "cache_creation_input_tokens", 0) or 0
    return (usage.input_tokens * p["in"] + usage.output_tokens * p["out"] + cr * p["in"] * 0.1 + cw * p["in"] * 1.25) / 1e6
