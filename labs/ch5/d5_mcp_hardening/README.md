# Lab 5.5 — Harden the MCP server

**Pairs with:** MCP Advanced Topics → Roots. Runs offline.

## Task
Copy your 5.1 server here and add:
1. `ALLOWED_ROOTS` — list of directories the `git_log` tool may read; any path outside (after `Path.resolve()`) → raise `ValueError("path not allowed")`.
2. Validate `n` (1–50) and reject `path` values containing `..` or shell metacharacters.
3. tool `read_file(rel_path)` — only inside the first allowed root, only `.md`/`.txt`, max 20 kB.
4. Injection test: `read_file` returns the file contents wrapped in `<untrusted_file>` tags so the host model sees them as data.

## Exam angles
- Tool results are **untrusted input** — the classic injection vector is a document/tool result telling the model to do something.
- Least privilege, allow-lists, size caps, and no shell interpolation.
