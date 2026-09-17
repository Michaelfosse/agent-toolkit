---
description: Default safety and verification rules for Power BI developer work.
---

- For report-layer edits, work only from a committed PBIP baseline using enhanced PBIR. Save pending Power BI Desktop changes before editing files.
- Treat semantic-model modifications as a separate, explicitly approved scope from report-layout changes.
- Require human approval before the first semantic-model write in a run; do not rely on preview MCP confirmation behavior as the approval boundary.
- Use `powerbi-modeling-mcp` for local model inspection and DAX validation. Use `powerbi-remote` only for published-model queries and report metadata; it does not author report canvases.
- Do not treat Desktop Bridge as an MCP server. Use its local CLI to reload PBIR and capture screenshots after report changes.
- For deployed screenshot validation, require workspace, report, and semantic-model names from the human, then use Fabric CLI to resolve one unambiguous target before any mutation. Never infer a production target.
- Do not declare report success until structural validation, relevant numerical checks, and rendered visual review have evidence. Mark unavailable checks `not_run`.
- Never commit screenshots, query outputs, workspace identifiers, tenant identifiers, credentials, or business data unless the consuming project explicitly approves them.
