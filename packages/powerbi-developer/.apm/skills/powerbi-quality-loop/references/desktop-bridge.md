# Desktop Bridge Workflow

Power BI Desktop Bridge is a local Windows named-pipe API, not an MCP server.
It reloads PBIR files and captures rendered screenshots from a running Power BI
Desktop instance. It cannot run remotely from WSL or validate user interactions.

On native Windows, run `powerbi-desktop` directly. When the agent runs in WSL,
use the wrapper described by `powerbi-developer-setup`; WSL Node.js cannot access
the Windows named pipe. Translate WSL input and output paths with `wslpath -w`.

1. Enable `Enable external tool access to Power BI Desktop through secure local APIs` in Power BI Desktop Preview Features.
2. Open the development PBIP and save any pending Desktop edits.
3. Identify the intended process and inspect its available preview operations:

```powershell
powerbi-desktop status
$desktopPid = 12345
powerbi-desktop manifest --pid $desktopPid
```

4. After a scoped PBIR edit, validate, reload, and capture sequentially:

```powershell
powerbi-report-author validate ".\Sales.Report"
powerbi-desktop reload --pid $desktopPid
powerbi-desktop screenshot-all --pid $desktopPid --output-dir ".\qa\run-001"
```

5. Open and inspect the images with a vision-capable model. File creation is
not evidence that review occurred.

Record the report commit, page, filter state, refresh state, viewport, zoom,
and Desktop/tool versions with each capture. Store sensitive screenshots only
in approved locations.
