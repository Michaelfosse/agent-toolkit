# Power BI Developer Profile

An APM profile for AI-assisted Power BI development in Claude Code and OpenCode.
It installs Microsoft's focused Power BI authoring plugin, registers local and
remote Power BI MCP servers, and adds a quality loop for rendered report review.

## Included

- Microsoft Power BI skills for report planning, design, PBIR/PBIP authoring,
  report management, and semantic-model authoring.
- `powerbi-modeling-mcp` for local semantic-model inspection, model changes,
  DAX validation, and PBIP/TMDL workflows.
- `powerbi-remote` for querying published semantic models and inspecting
  published report metadata.
- `powerbi-quality-loop` for screenshot review, visualization standards, and
  evidence-based report QA.

## Not Included

- General Fabric, SQL endpoint, Spark, warehouse, or FabricIQ skills.
- Power BI Desktop itself, Node.js, or global Power BI CLIs.
- Credentials, tenant IDs, workspace IDs, semantic model IDs, or report data.

## Install

From a consuming project, install this profile by local path while developing:

```bash
apm install /path/to/agent-toolkit/packages/powerbi-developer --target claude,opencode
apm compile --target claude,opencode
```

After publishing this profile, install its pinned Git reference instead. Commit
the generated `apm.lock.yaml`; use `apm install --frozen` for routine installs.

## Prerequisites

The Power BI report authoring loop requires a Windows machine with Power BI
Desktop and Node.js 20 or later. Enable Power BI Desktop's preview feature
`Enable external tool access to Power BI Desktop through secure local APIs`.

Install the local authoring tools on the Windows machine:

```powershell
npm install -g @microsoft/powerbi-report-authoring-cli@latest @microsoft/powerbi-desktop-bridge-cli@latest
powerbi-report-author --version
powerbi-desktop --version
```

`powerbi-modeling-mcp` runs through `npx`; it requires Node.js when the MCP
client starts it. The remote MCP requires the tenant preview setting for the
Power BI MCP endpoint, semantic model Build permission, and client-supported
Microsoft Entra authentication.

See `docs/setup.md` for the local and remote workflows and `docs/maintenance.md`
for controlled updates.
