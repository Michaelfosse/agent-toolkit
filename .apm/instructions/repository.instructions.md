---
description: Authoring and security rules for the agent-toolkit APM package.
---

- Treat `.apm/` as the authoritative source for package primitives.
- Do not hand-edit or commit generated target files unless a documented packaging workflow requires them.
- Keep skills focused on one coherent capability with a recognizable user trigger.
- Put optional detail in directly linked `references/` files instead of expanding `SKILL.md` indefinitely.
- Preserve compatibility with both Claude Code and OpenCode unless a file is explicitly documented as a target-specific adapter.
- Do not copy credentials, personal data, internal identifiers, endpoint values, proprietary schemas, or business-specific examples from source projects.
- Use synthetic examples when extracting a reusable work pattern.
- Review `docs/portability.md` before adding instructions, agents, commands, hooks, plugins, or MCP servers.
- Run APM validation, audit, and dry-run placement checks before considering a package change complete.
