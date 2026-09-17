# Target Discovery and Safeguards

Start with read-only Fabric CLI discovery. The human supplies display names;
the agent resolves IDs and verifies uniqueness.

```bash
fab ls
fab ls "<workspace name>.Workspace"
```

Identify the Report and SemanticModel items in the selected workspace. Use
`fab api -A powerbi` where report metadata or model binding requires the Power
BI REST API. Do not continue if a name resolves to zero or multiple items.

Before any deployment, refresh, or export request, present:

- Workspace, report, and semantic-model display names and IDs.
- Current Git commit and deployment source path.
- Target environment classification.
- Whether the report binding matches the supplied semantic model.
- Exact planned mutations and export pages/states.

Require renewed human authorization when the target, commit, report binding, or
requested mutation changes. Refuse production-like names until the human makes
an explicit override. Never infer a workspace from a similarly named one.

The consuming project owns its deployment mechanism. It may use Fabric CLI,
Fabric Git integration, a deployment pipeline, or an approved CI workflow. The
agent must inspect that project configuration and use its documented command;
this profile must not guess how to deploy a PBIP or TMDL artifact.
