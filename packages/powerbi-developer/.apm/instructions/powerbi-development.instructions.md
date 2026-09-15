---
description: Default safety and verification rules for Power BI developer work.
---

- For report-layer edits, work only from a committed PBIP baseline using enhanced PBIR. Save pending Power BI Desktop changes before editing files.
- Treat semantic-model modifications as a separate, explicitly approved scope from report-layout changes.
- Use `powerbi-modeling-mcp` for local model inspection and DAX validation. Use `powerbi-remote` only for published-model queries and report metadata; it does not author report canvases.
- Do not treat Desktop Bridge as an MCP server. Use its local CLI to reload PBIR and capture screenshots after report changes.
- Do not declare report success until structural validation, relevant numerical checks, and rendered visual review have evidence. Mark unavailable checks `not_run`.
- Never commit screenshots, query outputs, workspace identifiers, tenant identifiers, credentials, or business data unless the consuming project explicitly approves them.
