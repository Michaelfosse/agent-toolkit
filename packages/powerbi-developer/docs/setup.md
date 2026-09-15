# Setup

## MCP Servers

The profile configures two complementary MCP servers:

| Server | Use | Scope |
| --- | --- | --- |
| `powerbi-modeling-mcp` | Read and modify models, inspect TMDL/PBIP, and validate DAX | Local process; Desktop, PBIP, or Fabric model |
| `powerbi-remote` | Query published semantic models and inspect report metadata | Fabric-hosted Power BI service |

The local Modeling MCP has write capability. Keep its confirmation prompts
enabled and use a backup or Git baseline before model edits. The remote MCP is
read-oriented; it does not modify PBIR or report canvases.

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
