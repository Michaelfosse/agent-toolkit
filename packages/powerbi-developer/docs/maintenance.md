# Maintenance

This profile uses mutable upstream references for the Microsoft Power BI plugin
and npm MCP/CLI packages. The lockfile is the tested version set.

1. Create an update branch.
2. Run `apm update` in a representative consuming project.
3. Review upstream Microsoft Power BI plugin changes and the resulting lockfile.
4. Confirm both MCP registrations and run a representative PBIP smoke test:
   model inspection, one report validation, Desktop reload, screenshot capture,
   and visual review.
5. Commit the updated lockfile only when the smoke test passes.

Run routine consuming-project installs with `apm install --frozen`. Treat
preview-tool changes as an explicit update, not an unattended production change.
