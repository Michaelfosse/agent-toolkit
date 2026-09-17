# Execution Modes

| Component | Windows mode | WSL plus Windows mode |
| --- | --- | --- |
| Agent and project | Windows | WSL |
| APM skills | Windows project | WSL project |
| Modeling MCP | Windows process | Windows process launched through `cmd.exe` |
| Desktop Bridge and report CLI | Windows | Windows through a project wrapper |
| Power BI Desktop | Windows | Windows |
| Fabric CLI and Azure CLI | Agent environment | WSL |

Do not run Desktop Bridge with WSL Node.js. Windows named pipes are local to the
Windows process environment. Do not assume Windows Node.js can execute scripts
from a WSL UNC working directory; change to a Windows directory before invoking
npm-installed commands.

Use Windows `npx.cmd` to run the Modeling MCP, Desktop Bridge CLI, and report
authoring CLI. It downloads and caches the selected package on first use, so the
profile does not require global npm installations or an APM lifecycle script.

For PBIP/TMDL paths in WSL, translate paths with `wslpath -w`. Verify that the
target command accepts the resulting UNC path. Do not silently copy report or
model sources into Windows because that creates a competing source of truth.

Direct Lake models may not appear through Desktop's local Analysis Services
port. Use the Windows-hosted Modeling MCP and connect it to the Fabric semantic
model; keep corresponding TMDL source synchronized before any model reload.
