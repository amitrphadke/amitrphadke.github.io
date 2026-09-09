# CCDV-F hands-on labs

One small lab per study day of the [CCDV-F study tracker](https://www.amitphadke.com/learning/ccdv-f/tracker/), each paired with the Claude Academy video(s) for that day. Every lab is a `lab.py` starter with `TODO`s and a `test_lab.py` that checks the behaviour the exam asks about. When the tests pass, `check.py` ticks the lab in the tracker automatically.

## Setup (once)

```bash
cd labs
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then fill in ANTHROPIC_API_KEY and GH_TOKEN
```

- `ANTHROPIC_API_KEY` — from console.anthropic.com (personal account). Labs default to `claude-haiku-4-5`; the whole set costs well under $5.
- `GH_TOKEN` — the fine-grained GitHub token (Contents read/write on `amitrphadke/amitrphadke.github.io`) so `check.py` can tick the tracker.
- Chapter 4.2, 6.x labs use your Claude Code login (Max) instead of the API key.

## Daily loop

1. Open the day in the tracker → watch the lessons → click **open lab ↗**.
2. Read `README.md`, fill the `TODO`s in `lab.py`, run it with `python lab.py`.
3. `python check.py ch1/d0` — green means the tracker ticks itself. `python check.py ch1` runs a chapter, `all` runs everything.

## Labs

| Day | Lab | Pairs with | Needs |
|---|---|---|---|
| 1.0 | [A typed ask() — sync and async](ch1/d0_typed_client/) | Building with the Claude API → Accessing the API · Getting an API key · Making a request | API key |
| 1.1 | [Multi-turn chat that keeps history](ch1/d1_chat_history/) | Multi-turn conversations · System prompts | API key |
| 1.2 | [Streaming — print token by token](ch1/d2_streaming/) | Response streaming | API key |
| 1.3 | [Validated JSON with retry](ch1/d3_structured_output/) | Structured data | API key |
| 1.4 | [Image and PDF content blocks](ch1/d4_vision_pdf/) | Image support · PDF support · Citations | API key |
| 2.0 | [Your first tool loop](ch2/d0_first_tool/) | Introducing tool use · Tool functions · Tool schemas · Handling message blocks · Sending tool results | API key |
| 2.1 | [Multiple tools, parallel calls, is_error](ch2/d1_multi_tool/) | Multi-turn conversations with tools · Implementing multiple turns · Using multiple tools · Fine grained tool calling | API key |
| 2.2 | [Prompt caching — see cache_read_input_tokens > 0](ch2/d2_prompt_caching/) | Prompt caching · Rules of prompt caching · Prompt caching in action | API key |
| 2.3 | [Message Batches — 20 prompts, matched by custom_id](ch2/d3_batches/) | (docs) Message Batches API — see Library | API key |
| 2.4 | [Errors, retries and backoff (no API needed)](ch2/d4_errors_backoff/) | (docs) Errors and rate limits — see Library | offline / Claude Code login |
| 3.0 | [One task on three models — latency, tokens, cost](ch3/d0_model_compare/) | Claude Platform 101 → Choosing the right model | API key |
| 3.1 | [Cost calculator + token counting](ch3/d1_cost_calculator/) | (docs) Pricing · Token counting — see Library | API key |
| 3.2 | [Rewrite a weak prompt three ways and score them](ch3/d2_prompt_rewrite/) | Prompt engineering · Being clear and direct · Being specific · Structure with XML tags · Providing examples | API key |
| 3.3 | [Extended thinking on vs off](ch3/d3_extended_thinking/) | Extended thinking | API key |
| 3.4 | [Auto-summarise a long conversation](ch3/d4_context_summary/) | Claude Platform 101 → Context management | API key |
| 4.0 | [A 3-step prompt chain with a gate](ch4/d0_prompt_chain/) | Agents and workflows · Chaining workflows | API key |
| 4.1 | [Routing and parallelisation](ch4/d1_router_parallel/) | Routing workflows · Parallelization workflows | API key |
| 4.2 | [Agent SDK quickstart with a restricted tool set](ch4/d2_agent_sdk/) | Claude Platform 101 → The agent loop explained · Built-in tools | offline / Claude Code login |
| 4.3 | [Orchestrator + worker with max_turns](ch4/d3_orchestrator_worker/) | Agents and tools · Workflows vs agents · Introduction to subagents | API key |
| 4.4 | [Server-side web search with citations](ch4/d4_web_search_tool/) | Claude Platform 101 → Built-in tools | API key |
| 4.5 | [Loop, budget and destructive-action guards](ch4/d5_agent_guards/) | Quiz on agents and workflows · Using subagents effectively | API key |
| 5.1 | [An MCP server with a tool, a resource and a prompt](ch5/d1_mcp_server/) | Introducing MCP · MCP clients · Defining tools with MCP · Defining resources · Defining prompts | offline / Claude Code login |
| 5.4 | [Calling a remote MCP server through the API](ch5/d4_mcp_connector/) | MCP: Advanced Topics → The StreamableHTTP transport · StreamableHTTP in depth | API key |
| 5.5 | [Allow-lists and validation on your MCP server](ch5/d5_mcp_hardening/) | MCP Advanced Topics → Roots · Roots walkthrough | offline / Claude Code login |
| 6.0 | [A real CLAUDE.md with imports](ch6/d0_claude_md/) | Claude Code 101 → The CLAUDE.md file · Claude Code in Action → A CLAUDE.md that follows | offline / Claude Code login |
| 6.1 | [A slash command and a skill](ch6/d1_commands_skills/) | Claude Code 101 → Skills · Introduction to agent skills (whole course) | offline / Claude Code login |
| 6.2 | [Hooks: lint after every edit, block dangerous commands](ch6/d2_hooks/) | Claude Code 101 → Hooks · Claude Code in Action → Hooks · Permission modes | offline / Claude Code login |
| 6.3 | [A reviewer subagent with a restricted tool set](ch6/d3_subagent/) | Claude Code 101 → Subagents · Introduction to subagents | offline / Claude Code login |
| 6.4 | [Headless: claude -p with JSON output](ch6/d4_headless/) | Claude Code in Action → Routines and headless · GitHub Actions and Code Review | offline / Claude Code login |
| 7.1 | [Prompt-injection defences and an approval gate](ch7/d1_injection_defences/) | AI-Native SDLC Playbook → Hooks as approval gates · Give Claude a feedback loop | API key |
| 7.2 | [A Haiku moderation pre-check](ch7/d2_moderation/) | Building with the Claude API → (Prompt evaluation module) · docs: Usage policy | API key |
| 7.3 | [An eval harness that catches a regression](ch7/d3_evals/) | Prompt evaluation · A typical eval workflow · Generating test datasets · Running the eval · Model based grading · Code based grading | API key |
| 7.4 | [Diagnose failures from logs alone (offline)](ch7/d4_debug_from_logs/) | Building with the Claude API → Running the eval (debugging habits) · docs: stop reasons | offline / Claude Code login |
