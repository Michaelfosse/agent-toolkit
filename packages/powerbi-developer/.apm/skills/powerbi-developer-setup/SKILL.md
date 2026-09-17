---
name: powerbi-developer-setup
description: Use when installing, checking, configuring, or troubleshooting the Power BI developer profile on native Windows or WSL with Power BI Desktop on Windows; when Power BI Modeling MCP or Desktop Bridge cannot connect; or when deciding where Node.js, Fabric CLI, Azure CLI, and Power BI tools must run.
---

# Power BI Developer Setup

Support two modes:

- `windows`: agent, MCP, CLIs, and Power BI Desktop run on Windows.
- `wsl-windows`: agent and project run in WSL; Desktop-bound MCP and Bridge
  tools run as Windows processes through WSL interoperability.

Run `scripts/check_environment.py` before changing setup. Report available,
blocked, and unknown capabilities. Do not install tools, authenticate, or edit
consumer configuration without explicit human approval.

After the check, proactively propose the shortest mode-specific remediation
plan. Show the exact commands, where each command runs (Windows or WSL), what it
changes, and which capability it enables. Ask once for approval before executing
approved setup commands, then rerun the checker and report remaining blockers.
Do not require the human to diagnose the environment or assemble commands.

The profile deliberately launches `powerbi-modeling-mcp` through Windows
`cmd.exe` in both supported modes. In WSL, this lets the MCP process reach
Power BI Desktop's Windows-local services. Translate WSL project paths with
`wslpath -w` before passing them to Windows processes.

For Desktop Bridge from WSL, copy the wrapper assets into the consuming project
and keep them project-owned. The wrapper runs Windows PowerShell, changes away
from the WSL UNC working directory, and invokes the Windows-installed CLI.

Read these references when needed:

- [Execution modes](references/execution-modes.md)
- [WSL Desktop Bridge wrapper](references/wsl-desktop-bridge.md)

Completion means the detected mode is supported and the requested capability's
checks pass, or every blocker has an actionable remediation. Tenant, capacity,
Power BI permissions, and Desktop preview-feature state can remain `UNKNOWN`
until a live target is available.
