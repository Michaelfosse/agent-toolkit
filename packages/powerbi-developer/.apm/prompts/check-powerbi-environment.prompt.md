---
description: Detect whether the Power BI developer profile can run on native Windows or WSL with Windows Power BI Desktop.
---

Locate and run `scripts/check_environment.py` inside the installed
`powerbi-developer-setup` skill. For OpenCode, the skill is normally under
`.agents/skills/`; for Claude Code, it is normally under `.claude/skills/`.
Use `python3` on WSL and `py -3` on native Windows.

Report the detected mode and each available, blocked, or unknown capability. Do
not install tools, authenticate, copy wrapper assets, or edit MCP configuration
without explicit human approval. Proactively provide the shortest remediation
plan with exact commands, execution environment, expected changes, and enabled
capabilities. If the human approves, apply only those actions and rerun the
checker.
