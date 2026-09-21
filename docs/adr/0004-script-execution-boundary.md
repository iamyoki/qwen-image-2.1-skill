# 0004. Script Execution Boundary

We decided to establish an explicit script execution boundary: helper scripts such as `scripts/validate_prompt.py` are strictly offline testing and CI utilities, and autonomous agents are explicitly forbidden from executing them during interactive prompt generation dialogues.

## Context
When autonomous coding agents (e.g. Claude Code, Antigravity, Cursor) load a skill package containing a `scripts/` directory, they often aggressively attempt to run validation scripts via shell/terminal execution before responding to the user. In the case of `validate_prompt.py`, this had cascading negative side-effects:
1. It required the agent to construct an artificial JSON payload (since `validate_prompt.py` takes JSON), which in turn caused the agent to output redundant JSON in chat.
2. It added several seconds of subprocess spawning latency to simple prompt generation requests.
3. It created fragility across different operating systems (Windows encoding, PowerShell argument escaping, python path resolution).

## Consequences
- Interactive conversations remain pure and instantaneous, reasoning through rules in-memory without background shell executions.
- `scripts/validate_prompt.py` remains available for developers running `--test` or automated GitHub Actions CI.
- The boundary is codified explicitly in `SKILL.md` under `## Tool & Script Execution Policy`.
