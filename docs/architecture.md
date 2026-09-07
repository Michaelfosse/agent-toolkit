# Architecture

## Package Shape

`agent-toolkit` is a single APM package. It is not currently a marketplace, profile aggregator, or multi-package monorepo.

The package has three layers:

1. Portable source primitives under `.apm/`.
2. Human-facing governance and design documentation under `docs/`.
3. Generated target output created by APM in a consuming project or user configuration.

## Source and Output Boundary

Author here:

```text
.apm/instructions/
.apm/skills/
.apm/agents/
.apm/prompts/
.apm/hooks/
```

APM may deploy or compile to locations such as:

```text
CLAUDE.md
AGENTS.md
.claude/
.agents/
.opencode/
```

Generated files should be inspected during tests but are not the primary source. This prevents target-specific copies from drifting apart.

## Current Primitives

### Instructions

`repository.instructions.md` governs maintenance of this package. It is unconditional because repository security and portability rules apply to all files.

### Skills

`create-skill` is the first packaged capability. It demonstrates progressive disclosure with one optional final-review checklist.

## Growth Path

Add individual skills while they share one audience, trust boundary, and release cadence.

Split into multiple packages when one of these becomes true:

- Public-safe and private work content need independent access control.
- A specialist bundle should be installable without the base toolkit.
- Dependencies or MCP servers differ materially by role.
- Skills need independent versioning or release approval.
- Target-specific executable adapters become large enough to maintain separately.

A likely later shape is:

```text
agent-toolkit/
|-- apm.yml                    # optional marketplace or aggregate profile
`-- packages/
    |-- core/
    |-- data-engineering/
    |-- fabric-private/
    `-- runtime-adapters/
```

Do not migrate to this shape until at least two packages have a concrete independent consumer or access boundary.

## Trust Model

Skills and instructions are portable guidance. Hooks, plugins, scripts, and MCP servers can execute or expose capabilities and therefore need stronger review.

Agent callbacks provide fast feedback but should not be the sole enforcement mechanism for formatting, tests, secret detection, or release policy. Put authoritative checks in CI, Git hooks, pre-commit, or platform policy.
