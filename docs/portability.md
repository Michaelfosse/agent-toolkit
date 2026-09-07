# Claude Code and OpenCode Portability

This guide reflects Microsoft APM v0.29.0.

## Target Matrix

| Primitive | Claude Code | OpenCode | Recommendation |
|---|---|---|---|
| Skills | `.claude/skills/` | `.agents/skills/` | Preferred for portable workflows |
| Instructions | `.claude/rules/` and compile context | Compiled into `AGENTS.md` | Use for concise automatic rules |
| Named agents | `.claude/agents/` | `.opencode/agents/` | Keep frontmatter valid for both |
| Commands | `.claude/commands/` | `.opencode/commands/` | Suitable when explicit invocation is valuable |
| MCP | Client configuration | `opencode.json` integration | Declare only reviewed servers |
| APM hooks | Supported | Not supported | Requires an OpenCode plugin adapter |
| OpenCode plugins | Not supported | `.opencode/plugins/` | Target-specific executable code |

## Skills

Skills are the default abstraction for cross-client behavior. Keep the source under `.apm/skills/` and let APM choose each target's destination.

Do not author the same skill independently under `.claude/skills/` and `.opencode/skills/`. Current OpenCode project placement is the converged `.agents/skills/` path.

## Instructions and Root Context

APM compiles instructions for the selected targets:

```bash
apm compile --target claude,opencode
```

Claude Code can use `CLAUDE.md` and native `.claude/rules/`. OpenCode consumes compiled instructions from `AGENTS.md` because APM does not deploy a native OpenCode instructions primitive.

Compilation may deduplicate Claude instructions from `CLAUDE.md` when equivalent `.claude/rules/` files exist. Treat `.apm/instructions/` as the source instead of depending on a specific generated shape.

## Named Agents

OpenCode has stricter shared frontmatter requirements:

- `tools` must be a mapping of tool names to booleans, not a list.
- `color` must be a supported theme name or a hex color.
- Model names must make sense in both environments or be omitted.

Prefer skills when a persona is not required. Skills have wider portability and simpler tool inheritance.

## Commands

One `.apm/prompts/<name>.prompt.md` source can become commands on Claude Code and OpenCode. Command metadata is transformed per target, so keep frontmatter to fields supported by both clients when cross-client parity matters.

## Hooks and Plugins

APM hooks do not reach OpenCode. OpenCode's JavaScript/TypeScript plugin API is a separate runtime extension surface.

For equivalent automatic behavior:

1. Put the validation or notification logic in a shared script.
2. Add a Claude hook descriptor that invokes the script.
3. Add an OpenCode plugin that invokes the same script for the closest equivalent event.
4. Document semantic differences between events.
5. Keep an authoritative CI or Git-level check when behavior must be guaranteed.

See `runtime-adapters.md` for the proposed repository shape.

## plugin.json

Do not use a hand-written `plugin.json` as this repository's primary source manifest. APM package identity and dependencies live in `apm.yml`. `apm pack` can export standard plugin artifacts, including `plugin.json`, for supported plugin ecosystems.
