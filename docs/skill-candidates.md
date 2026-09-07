# Skill Candidate Review Queue

This is an assessment backlog, not approved package scope. No candidate should be copied directly from a source project.

## Selection Criteria

Prioritize a candidate when it is:

- Reused across more than one project or expected to recur.
- Difficult enough that generic model knowledge is insufficient.
- Stable enough to maintain as a workflow.
- Safe to describe without exposing project data or business logic.
- Triggerable from a recognizable user request.

## Priority 1: Review Next

### metadata-first-fabric-sql

Purpose: discover repository and live Fabric metadata before writing SQL or assuming schemas.

Example triggers:

- "Find the correct Fabric table and schema before writing this query."
- "Compare declared table metadata with the live SQL endpoint."
- "Diagnose this schema mismatch without guessing column names."

Why it is promising: the procedure is reusable and directly aligned with Fabric analytics work.

Boundary: exclude internal schemas, table names, endpoints, workspace aliases, sample rows, and join keys.

### thin-notebook-shared-library

Purpose: move reusable Fabric or Databricks notebook logic into a testable Python package while keeping operational notebook entrypoints thin.

Example triggers:

- "Move reusable logic out of this notebook."
- "Create a thin notebook backed by a tested Python package."
- "Wire a wheel-backed notebook into an Asset Bundle job."

Why it is promising: the same architecture appears across Fabric and Databricks work.

Boundary: use synthetic package, job, and notebook names.

### structured-agent-issue-lifecycle

Purpose: maintain problem, plan, implementation notes, verification evidence, and review as separate artifacts for substantial agent work.

Example triggers:

- "Create a structured issue and investigate the root cause."
- "Plan this feature with exact files, risks, and verification."
- "Review the implementation against the problem and plan."

Why it is promising: it is generic, already used in a work project, and has low extraction risk.

Boundary: avoid hard-coded project paths and obsolete template links.

## Priority 2: Strong Engineering Candidates

### immutable-python-wheel-promotion

Enforce explicit versions, reproducible wheel builds, metadata inspection, content hashing, and immutable artifact reuse.

### risk-based-data-app-testing

Choose the narrowest test that addresses material risk and distinguish mocked evidence from real platform evidence.

### dependency-guided-runtime-retirement

Map runtime, deployment, package, configuration, and test dependencies before classifying legacy code as keep, migrate, or remove.

### non-destructive-workbook-migration

Audit and convert selected workbooks with read-only sources, fail-closed mappings, preservation checks, and durable reports.

This candidate needs careful sanitization because current examples encode business headers and workbook content.

## Priority 3: Private or Specialized Candidates

These are useful but likely belong in a private work package because their present workflows depend on internal infrastructure or business behavior:

- `fabric-runtime-inventory-sync`
- `metadata-driven-data-orchestrator`
- `semantic-report-validation-materializer`
- `databricks-app-bundle-release`
- `scoped-approval-publish-operator`
- `canonical-field-registry`
- `hybrid-cloud-data-devcontainer`

Extract only after defining a private package boundary and replacing all environment-specific values with configuration contracts.

## Existing Personal Tooling to Review Separately

These may be useful globally but are not part of the initial work-focused package:

- `windows-search`
- `worktrees`
- `codebase-memory`
- Completion notifications
- Parameterized tmux agent-session bootstrap

Review them based on actual cross-project use before inclusion. In particular, `codebase-memory` requires the corresponding MCP server, and `worktrees` assumes a specific treekanga bare-repository workflow.

## Explicit Exclusions

- Personal-finance taxonomy, reporting, bank integration, and review workflows.
- Project-specific business fields, report definitions, schedules, workspaces, and deployment identities.
- Existing credentials, environment files, raw records, and operational secrets.
