# Agent Toolkit

A work-focused [Agent Package Manager (APM)](https://github.com/microsoft/apm) package for sharing skills and agent instructions across Claude Code and OpenCode.

The repository starts deliberately small. Version 0.1.0 contains one reviewed skill and the documentation needed to add more without mixing portable guidance with project-specific business context.

For the team-sharing proposal, open [`docs/agent-capability-sharing.html`](docs/agent-capability-sharing.html) in a browser. It explains the proposed package model, role profiles, onboarding, versioning, contribution workflow, governance, and pilot scope.

## Current Scope

Included:

- `create-skill`: designs, creates, and reviews focused Agent Skills.
- Repository instructions for maintaining this package safely.
- A Claude Code and OpenCode compatibility guide.
- A review queue of skill candidates identified from existing work projects.

Not included:

- Personal-finance workflows or data.
- Employer-specific workspace IDs, endpoints, credentials, schemas, business rules, or operational runbooks.
- Runtime hooks or OpenCode plugins. Their adapter design is documented, but version 0.1.0 does not install executable callbacks.
- A marketplace, multiple profiles, or public release automation.

## Why One Package First

APM supports single packages, marketplaces, and monorepos containing many packages. A single package is the smallest useful starting point for this repository:

- One manifest controls the supported clients.
- Skills remain independently triggerable inside the package.
- The structure can become a multi-package repository later without committing to that complexity now.
- Private work-focused content can be reviewed before any public extraction.

## Repository Layout

```text
agent-toolkit/
|-- apm.yml
|-- .apm/
|   |-- instructions/
|   |   `-- repository.instructions.md
|   `-- skills/
|       `-- create-skill/
|           |-- SKILL.md
|           `-- references/
|               `-- quality-checklist.md
|-- docs/
|   |-- architecture.md
|   |-- portability.md
|   |-- runtime-adapters.md
|   `-- skill-candidates.md
|-- CONTRIBUTING.md
`-- SECURITY.md
```

`.apm/` is the authoritative package source. Generated `.claude/`, `.agents/`, `.opencode/`, `CLAUDE.md`, and `AGENTS.md` files are deployment outputs, not authoring locations.

## Prerequisites

Install APM on WSL/Linux:

```bash
curl -sSL https://aka.ms/apm-unix | sh
apm --version
```

The package format was based on Microsoft APM v0.29.0. Review upstream release notes before adopting a newer major format.

## Local Development

Validate instructions without writing generated files:

```bash
apm compile --validate
```

Preview target placement:

```bash
apm install --dry-run --target claude,opencode
apm compile --dry-run --target claude,opencode
```

Run package security and consistency checks:

```bash
apm audit
```

Build a distributable package:

```bash
apm pack
```

## Test a Local Install

From a separate scratch project, install this checkout by local path:

```bash
apm install /path/to/agent-toolkit --target claude,opencode
apm compile --target claude,opencode
```

Expected skill locations:

| Target | Project skill location |
|---|---|
| Claude Code | `.claude/skills/create-skill/SKILL.md` |
| OpenCode | `.agents/skills/create-skill/SKILL.md` |

APM compiles unconditional instructions into target root context. Claude Code uses `CLAUDE.md` or `.claude/rules/`; OpenCode uses `AGENTS.md`.

## Future Remote Installation

No remote is configured yet. After this repository is created and tagged on GitHub, installation will use a pinned reference such as:

```bash
apm install Michaelfosse/agent-toolkit#v0.1.0 --target claude,opencode
apm compile --target claude,opencode
```

For a private GitHub repository, authenticate separately with `gh auth login` or a read-only `GITHUB_APM_PAT`. Never place a token in `apm.yml`.

## Adding Skills

Use the bundled `create-skill` skill and follow `CONTRIBUTING.md`. A candidate must have:

- One coherent capability and recognizable trigger.
- Generic examples or approved private examples.
- No copied credentials, identifiers, client data, or internal business rules.
- Manual trigger and non-trigger examples.
- A clear completion condition.

See `docs/skill-candidates.md` for the initial review queue.

## Portability

Skills are the most portable primitive and should carry most workflows. Instructions, named agents, commands, hooks, and MCP declarations have different target reach. See `docs/portability.md` before adding a new primitive.

Runtime callbacks are not portable through APM to OpenCode. Use shared validation logic with thin target-specific adapters as described in `docs/runtime-adapters.md`.

## Status

This repository is local-only and has no license or public support commitment. Decide the private/public boundary before creating a remote or copying content from another project.
