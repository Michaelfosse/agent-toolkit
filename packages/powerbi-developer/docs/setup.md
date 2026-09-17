# Setup

## Execution Mode

The profile supports native Windows and WSL with Power BI Desktop on Windows.
Run `check-powerbi-environment` after installation. The Modeling MCP is launched
as a Windows process through `cmd.exe` in both modes so it can reach Windows-local
Power BI Desktop services. In WSL, keep Fabric CLI and Azure CLI beside the agent,
and use the setup skill's project wrapper for Windows Desktop Bridge commands.
The Microsoft Modeling MCP, Desktop Bridge CLI, and report authoring CLI run
through Windows `npx.cmd`; they download and cache automatically on first use
instead of requiring global npm installation.

The setup command is diagnostic and advisory by default. It detects the mode,
runs read-only checks, and proactively proposes exact Windows or WSL commands.
It executes setup actions only after the human approves them, then verifies the
result by rerunning the checks.

## MCP Servers

The profile configures two complementary MCP servers:

| Server | Use | Scope |
| --- | --- | --- |
| `powerbi-modeling-mcp` | Read and modify models, inspect TMDL/PBIP, and validate DAX | Local process; Desktop, PBIP, or Fabric model |
| `powerbi-remote` | Query published semantic models and inspect report metadata | Fabric-hosted Power BI service |

The local Modeling MCP has write capability. Require human approval and use a
backup or Git baseline before model edits; preview releases can change their
confirmation behavior. The remote MCP is read-oriented; it does not modify PBIR
or report canvases.

The remote MCP requires a Power BI administrator to enable `Users can use the
Power BI Model Context Protocol server endpoint (preview)`. It authenticates as
the current user through the MCP host and observes that user's Power BI access.
Confirm that the installed OpenCode or Claude version supports its Microsoft
Entra authentication before relying on it.

## Report Authoring

Report-layer authoring works only with PBIP/PBIR files on disk. Use Power BI
Desktop Bridge on Windows to reload those files and capture page images. It is
not a remote Power BI service API and cannot replace published-report interaction
testing.

For service-level behavior tests, publish to an approved development workspace,
then use an approved browser session. Test row-level security using the intended
identity or role.

## Published Screenshot Validation

`powerbi-deploy-screenshot-loop` is the opt-in service-validation capability.
The human supplies a development workspace name, report name, semantic-model
name, and authorization to deploy, refresh, or export. The agent uses `fab` to
resolve and verify the target IDs; it stops on ambiguous results and never
infers a production target.

Install and authenticate Fabric CLI in the environment where the agent runs:

```bash
pip install ms-fabric-cli
fab auth login
fab --version
```

Fabric CLI manages discovery and the JSON ExportToFile job lifecycle. The final
PNG export download requires a binary-capable client because `fab api` is not a
binary artifact downloader. See the skill's published-validation template for
the project-local configuration shape.

Use `check-powerbi-published-validation` before requesting a service-validation
run. It checks Fabric CLI, Fabric authentication, and Azure CLI readiness without
installing or authenticating. When Fabric CLI is missing, it provides an explicit
opt-in installation command; it never installs it automatically.
