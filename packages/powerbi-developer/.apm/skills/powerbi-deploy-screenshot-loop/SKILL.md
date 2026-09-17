---
name: powerbi-deploy-screenshot-loop
description: Use when deploying Power BI PBIP or TMDL changes to an approved development workspace, refreshing a semantic model, exporting published report pages as PNG files, and reviewing the service-rendered result. Require the human to provide workspace, report, and semantic-model names; use Fabric CLI to resolve IDs and stop on ambiguous matches. Do not use for local-only PBIR review or general Fabric work.
---

# Power BI Deploy Screenshot Loop

Use this opt-in release-validation workflow only after the local
`powerbi-quality-loop` passes, unless the human explicitly requests
service-only investigation.

Run `scripts/check_prerequisites.py` before requesting target names. If it
reports a blocking failure, explain the result and wait for the human to approve
the explicit install or authentication action. Never use `--install-fab --yes`
without that approval.

## Required Human Input

Obtain all of the following before discovery:

1. Workspace display name.
2. Report display name.
3. Semantic-model display name, unless the human explicitly asks to use the
   report's current binding.
4. Confirmation that the workspace is an approved non-production target.
5. Whether deployment, model refresh, and export are authorized for this run.

Do not ask the human for GUIDs. Do not persist names or resolved IDs in this
reusable profile. A consuming project may use a local copy of the supplied
template for its own approved configuration.

## Workflow

1. Confirm the local Git commit and inspect the consuming project's approved
   deployment method. Do not invent a deployment command.
2. Use `fab` to list workspaces, items, and their metadata. Resolve the supplied
   workspace, report, and semantic model to exactly one item each. Verify the
   report's model binding when a model was specified.
3. Stop and ask the human if any name is missing, ambiguous, absent, mismatched,
   or appears to be a production target. Present the resolved names, IDs, target
   environment, commit, and intended mutations before proceeding.
4. After explicit approval, deploy the exact committed artifacts using the
   project's approved deployment mechanism. Verify deployment completion.
5. If authorized, refresh the resolved semantic model and wait for successful
   completion. Record the refresh end time; do not accept a screenshot as
   current-data evidence without it.
6. Use `fab api -A powerbi` to create a PNG export job for explicit report pages
   and states, then poll it to a terminal status. Resolve page technical names
   from the published report; display names are not export identifiers.
7. Download the final ZIP or PNG with an approved binary-capable client. `fab
   api` handles the JSON job lifecycle but must not be assumed to save binary
   export content correctly. Extract images to a run-specific QA directory.
8. Open and inspect the rendered PNGs with a vision-capable reviewer. Compare
   approved numerical scenarios separately and record visual defects, stale-data
   signals, and untested behavior.
9. Report every gate as `pass`, `fail`, or `not_run`. Service PNGs do not prove
   interactions, drillthrough, bookmarks, navigation, or RLS behavior; use an
   approved browser session for those checks.

Read these references when needed:

- [Target discovery and safeguards](references/target-discovery.md)
- [Export-to-file workflow](references/export-to-file.md)
- [Published validation template](assets/published-validation.template.yaml)

Completion means the approved deployed version, refresh state, export scenarios,
and screenshot-review findings are recorded with the relevant commit. It does
not mean the report is production-approved unless the consuming project has a
separate release decision.
