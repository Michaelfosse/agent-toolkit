# WSL Desktop Bridge Wrapper

Copy `assets/wsl-windows/powerbi-desktop` and
`assets/wsl-windows/powerbi-desktop-windows.ps1` into a consuming project's
approved tools directory, then make the shell wrapper executable.

```bash
chmod +x tools/powerbi-desktop
tools/powerbi-desktop status
```

The wrapper requires WSL interoperability and Windows PowerShell. It sets
`NODE_OPTIONS=--use-system-ca` for Windows npm environments that use the Windows
certificate store and changes to the Windows system drive before invoking the
Desktop Bridge package through `npx.cmd`. Windows npm downloads and caches the
CLI automatically on first use; no global npm installation is required.

Always run `status` first, choose the intended PID, and stop if Desktop reports
unsaved changes. Run reload and screenshot operations serially. Translate WSL
output paths before passing them to the Windows CLI:

```bash
tools/powerbi-desktop screenshot <page-id> --pid <pid> \
  --output "$(wslpath -w /tmp/report-page.png)" --scale 2
```
