---
description: Detect whether the Power BI developer profile can run on native Windows or WSL with Windows Power BI Desktop.
---

Run the environment checker from the installed setup skill. On WSL use:

```bash
python3 .agents/skills/powerbi-developer-setup/scripts/check_environment.py
```

On native Windows use:

```powershell
py -3 .agents\skills\powerbi-developer-setup\scripts\check_environment.py
```

Report the detected mode and each available, blocked, or unknown capability. Do
not install tools, authenticate, copy wrapper assets, or edit MCP configuration
without explicit human approval. Proactively provide the shortest remediation
plan with exact commands, execution environment, expected changes, and enabled
capabilities. If the human approves, apply only those actions and rerun the
checker.
