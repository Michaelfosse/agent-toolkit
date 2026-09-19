# Power BI Developer Profile

An APM profile for AI-assisted Power BI development in Claude Code and OpenCode.
It installs Microsoft's focused Power BI authoring plugin, registers local and
remote Power BI MCP servers, and adds a quality loop for rendered report review.

## Included

- Microsoft's focused Power BI authoring plugin for report planning, design,
  PBIR/PBIP operations, report management, and semantic-model authoring. Its
  deployed skill names follow the current upstream package.
- `powerbi-modeling-mcp` for local semantic-model inspection, model changes,
  DAX validation, and PBIP/TMDL workflows.
- `powerbi-remote` for querying published semantic models and inspecting
  published report metadata.
- `powerbi-quality-loop` for screenshot review, visualization standards, and
  evidence-based report QA.
- `powerbi-developer-setup` for native Windows and WSL-plus-Windows environment
  detection, Desktop-bound tooling checks, and WSL wrapper guidance.
- `powerbi-deploy-screenshot-loop` for opt-in deployment, refresh, published
  PNG export, service-rendered review, guarded iteration, and pull-request handoff
  in an approved development workspace.
- `check-powerbi-published-validation` command for a read-only prerequisite
  check before service validation.
- `check-powerbi-environment` command for Windows and WSL readiness checks.

## Not Included

- General Fabric, SQL endpoint, Spark, warehouse, or FabricIQ skills.
- Power BI Desktop itself, Node.js, or global Power BI CLIs.
- Credentials, tenant IDs, workspace IDs, semantic model IDs, or report data.

## Install

From the Power BI workspace, install the public package for Claude Code and
OpenCode:

```bash
apm install Michaelfosse/agent-toolkit/packages/powerbi-developer -t claude,opencode
apm compile --target claude,opencode
apm audit
```

With no `#ref`, APM resolves the repository's default branch. Commit the
generated `apm.lock.yaml` to preserve the exact resolved commits. Use
`apm install --frozen` for routine installs.

While developing this package locally, install it by path from a separate
consuming project:

```bash
apm install /path/to/agent-toolkit/packages/powerbi-developer --target claude,opencode
apm compile --target claude,opencode
```

## Prerequisites

The Power BI report authoring loop requires a Windows machine with Power BI
Desktop and Node.js 20 or later. Enable Power BI Desktop's preview feature
`Enable external tool access to Power BI Desktop through secure local APIs`.

The profile runs local authoring tools through Windows `npx.cmd`, which downloads
and caches them automatically on first use. To smoke-test them manually:

```powershell
npx.cmd -y @microsoft/powerbi-report-authoring-cli@latest --version
npx.cmd -y @microsoft/powerbi-desktop-bridge-cli@latest --version
```

`powerbi-modeling-mcp` runs through `npx`; it requires Node.js when the MCP
client starts it. The remote MCP requires the tenant preview setting for the
Power BI MCP endpoint, semantic model Build permission, and client-supported
Microsoft Entra authentication.

Published PNG validation additionally requires Fabric CLI, an approved
development workspace on Fabric, Premium, or Embedded capacity, and the tenant
setting that allows image export. The human provides workspace, report, and
semantic-model names; the skill uses `fab` to resolve their IDs before actions.
For validate-before-commit work, it uses a repository-approved, narrowly scoped
`fab deploy` configuration with unpublish disabled. It verifies the workspace's
Git connection and branch before deployment, then reconciles the workspace to
the final pushed commit before creating a pull request.

See `docs/setup.md` for the local and remote workflows and `docs/maintenance.md`
for controlled updates.
