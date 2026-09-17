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
6. Whether commit, push, and pull-request creation are authorized after the
   validation gates pass.

Do not ask the human for GUIDs. Do not persist names or resolved IDs in this
reusable profile. A consuming project may use a local copy of the supplied
template for its own approved configuration.

## Workflow

1. Inspect local Git status, branch, upstream, remote repository, and starting
   commit. Preserve unrelated changes and do not begin from a detached HEAD.
2. Use `fab` to list workspaces, items, and their metadata. Resolve the supplied
   workspace, report, and semantic model to exactly one item each. Verify the
   report's model binding when a model was specified.
3. Inspect the workspace Git connection and detailed status. Require the same
   provider, repository, directory, and branch as the local checkout. If only
   the branch differs, follow the guarded reconnection procedure; never discard
   workspace changes or choose a conflict preference automatically.
4. Select one deployment mode from the project configuration. Use scoped local
   `fab deploy` for an edit-before-commit loop. Use Fabric `updateFromGit` only
   for commits already pushed to the connected branch. Do not mix the modes or
   invent deployment configuration.
5. Stop and ask the human if any target is ambiguous, mismatched, production-like,
   dirty, conflicted, or unsafe. Present resolved IDs, branch alignment, starting
   commit, deployment mode, scope, and intended mutations before proceeding.
6. After approval, iterate: edit local PBIR/TMDL, run local validation, deploy
   only the approved report/model scope, and verify item existence and report
   binding. If the model changed and refresh is authorized and applicable,
   refresh it to a terminal success state and record its end time.
7. Use `fab api -A powerbi` to create a PNG export job for explicit report pages
   and states, then poll it to a terminal status. Resolve page technical names
   from the published report; display names are not export identifiers.
8. Download the final ZIP or PNG with an approved binary-capable client. `fab
   api` handles the JSON job lifecycle but must not be assumed to save binary
   export content correctly. Extract images to a run-specific QA directory.
9. Open and inspect the rendered PNGs with a vision-capable reviewer. Compare
   approved numerical scenarios separately and record visual defects, stale-data
   signals, and untested behavior. Fix material defects and repeat from step 6;
   stop on a blocker or after three visual rounds unless the human extends the
   limit.
10. Report every gate as `pass`, `fail`, or `not_run`. Service PNGs do not prove
   interactions, drillthrough, bookmarks, navigation, or RLS behavior; use an
   approved browser session for those checks.
11. After all required gates pass, review the diff and commit only intended
    source files. Push the local branch, reconcile the workspace Git status to
    that exact remote commit, verify no workspace changes or conflicts remain,
    then create the pull request using the repository's normal base branch and
    contribution conventions. Do not commit exported images or sensitive QA
    evidence unless the project explicitly requires it.

Read these references when needed:

- [Target discovery and safeguards](references/target-discovery.md)
- [Workspace Git safety](references/workspace-git-safety.md)
- [Deployment, iteration, and release](references/deployment-iteration-release.md)
- [Export-to-file workflow](references/export-to-file.md)
- [Published validation template](assets/published-validation.template.yaml)

Completion means the approved deployed version, refresh state, export scenarios,
and findings are tied to the final pushed commit; the workspace is clean and
aligned to that commit; and the requested pull request exists. It does not mean
the report is production-approved without a separate release decision.
