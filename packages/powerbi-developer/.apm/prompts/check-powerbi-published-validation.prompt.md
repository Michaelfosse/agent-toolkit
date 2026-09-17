---
description: Check whether the current environment is ready for published Power BI deployment and PNG screenshot validation.
---

Run the prerequisite checker at:

```bash
python3 .agents/skills/powerbi-deploy-screenshot-loop/scripts/check_prerequisites.py
```

Report each result as ready, blocked, or unknown. Do not install, authenticate,
deploy, refresh, or export by default. If Fabric CLI is missing, show the
explicit opt-in command below and wait for approval:

```bash
python3 .agents/skills/powerbi-deploy-screenshot-loop/scripts/check_prerequisites.py --install-fab --yes
```

Explain that workspace, report, semantic-model, capacity, and tenant image-export
checks remain unknown until the human provides approved target names.
