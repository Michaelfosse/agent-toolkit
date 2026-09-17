[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$BridgeArguments
)

$ErrorActionPreference = "Stop"
$env:NODE_OPTIONS = "--use-system-ca"

# Windows npm launchers cannot use a WSL UNC path as their working directory.
Set-Location $env:SystemDrive
& npx.cmd -y "@microsoft/powerbi-desktop-bridge-cli@latest" @BridgeArguments
exit $LASTEXITCODE
