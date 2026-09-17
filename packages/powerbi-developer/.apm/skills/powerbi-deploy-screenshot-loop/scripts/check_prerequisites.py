#!/usr/bin/env python3
"""Check local prerequisites for published Power BI screenshot validation."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class CommandResult:
    """Capture a completed command without exposing its output by default."""

    return_code: int
    output: str


@dataclass(frozen=True)
class CheckResult:
    """Represent one prerequisite result and its remediation guidance."""

    name: str
    status: str
    detail: str
    next_action: str


def run_command(command: Sequence[str]) -> CommandResult:
    """Run a short local command and capture combined output.

    Args:
        command: Executable and arguments to run.

    Returns:
        Command exit code and combined standard output/error text.
    """
    try:
        completed_process = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired) as exception:
        return CommandResult(return_code=1, output=str(exception))

    return CommandResult(
        return_code=completed_process.returncode,
        output=f"{completed_process.stdout}\n{completed_process.stderr}".strip(),
    )


def get_command_version(command_name: str) -> str:
    """Return the first non-empty version output line for an installed command.

    Args:
        command_name: Command to query with ``--version``.

    Returns:
        A concise version string or ``installed`` when output is unavailable.
    """
    result = run_command([command_name, "--version"])
    if result.return_code != 0:
        return "installed"

    for line in result.output.splitlines():
        if line.strip():
            return line.strip()
    return "installed"


def check_fabric_cli() -> CheckResult:
    """Check whether Fabric CLI is available on PATH.

    Returns:
        Fabric CLI installation status and next action.
    """
    if shutil.which("fab") is None:
        return CheckResult(
            name="Fabric CLI",
            status="FAIL",
            detail="fab was not found on PATH.",
            next_action="Run this script with --install-fab --yes, or use the active Python interpreter to install ms-fabric-cli.",
        )

    return CheckResult(
        name="Fabric CLI",
        status="PASS",
        detail=get_command_version("fab"),
        next_action="None.",
    )


def check_fabric_authentication(fabric_cli_available: bool) -> CheckResult:
    """Check Fabric CLI authentication without printing account information.

    Args:
        fabric_cli_available: Whether Fabric CLI is installed.

    Returns:
        Authentication status and next action.
    """
    if not fabric_cli_available:
        return CheckResult(
            name="Fabric authentication",
            status="UNKNOWN",
            detail="Fabric CLI is unavailable.",
            next_action="Install Fabric CLI first.",
        )

    result = run_command(["fab", "auth", "status"])
    authentication_active = "logged in: true" in result.output.lower()
    if result.return_code != 0 or not authentication_active:
        return CheckResult(
            name="Fabric authentication",
            status="FAIL",
            detail="fab auth status did not report an active session.",
            next_action="Run fab auth login in this environment.",
        )

    return CheckResult(
        name="Fabric authentication",
        status="PASS",
        detail="Active session detected.",
        next_action="None.",
    )


def check_azure_cli() -> CheckResult:
    """Check Azure CLI availability for binary export download support.

    Returns:
        Azure CLI status and next action. This is a warning because another
        approved binary-capable client can download the final export.
    """
    if shutil.which("az") is None:
        return CheckResult(
            name="Azure CLI",
            status="WARN",
            detail="az was not found on PATH.",
            next_action="Install Azure CLI or configure another approved binary-capable export downloader.",
        )

    account_result = run_command(["az", "account", "show", "--output", "none"])
    if account_result.return_code != 0:
        return CheckResult(
            name="Azure CLI",
            status="WARN",
            detail="Azure CLI is installed but no active account was confirmed.",
            next_action="Run az login if Azure CLI will download the export artifact.",
        )

    return CheckResult(
        name="Azure CLI",
        status="PASS",
        detail=get_command_version("az"),
        next_action="None.",
    )


def get_target_checks() -> list[CheckResult]:
    """Return checks that require human-provided target names.

    Returns:
        Deferred checks for workspace, report, model, capacity, and tenant
        settings that cannot be validated safely during a generic local check.
    """
    return [
        CheckResult(
            name="Target resolution",
            status="UNKNOWN",
            detail="Workspace, report, and semantic-model names were not supplied.",
            next_action="Provide approved target names to the deploy screenshot loop.",
        ),
        CheckResult(
            name="Capacity and image export",
            status="UNKNOWN",
            detail="Requires the resolved published report and tenant permissions.",
            next_action="Verify Fabric/Premium/Embedded capacity and image export tenant setting after target resolution.",
        ),
    ]


def install_fabric_cli() -> int:
    """Install Fabric CLI with the active Python interpreter.

    Returns:
        The pip command exit code.
    """
    return subprocess.run(
        [sys.executable, "-m", "pip", "install", "ms-fabric-cli"],
        check=False,
    ).returncode


def print_results(results: Sequence[CheckResult]) -> None:
    """Print a concise, token-free prerequisite report.

    Args:
        results: Prerequisite results to display.
    """
    print("Power BI published screenshot validation readiness\n")
    for result in results:
        print(f"[{result.status}] {result.name}: {result.detail}")
        if result.next_action != "None.":
            print(f"       Next: {result.next_action}")


def parse_arguments() -> argparse.Namespace:
    """Parse explicit prerequisite-check and installation options.

    Returns:
        Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Check prerequisites for published Power BI screenshot validation."
    )
    parser.add_argument(
        "--install-fab",
        action="store_true",
        help="Install Fabric CLI using the active Python interpreter.",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Confirm the --install-fab action without an interactive prompt.",
    )
    return parser.parse_args()


def main() -> int:
    """Run the read-only checks and optional explicitly approved installation.

    Returns:
        Zero when Fabric CLI and its authentication are ready; one when a
        blocking prerequisite is absent; two for an unconfirmed install request.
    """
    arguments = parse_arguments()
    if arguments.install_fab and not arguments.yes:
        print("Would run: python -m pip install ms-fabric-cli")
        print("Re-run with --install-fab --yes to approve this installation.")
        return 2

    if arguments.install_fab:
        install_return_code = install_fabric_cli()
        if install_return_code != 0:
            print("Fabric CLI installation failed. Resolve the pip error and rerun this check.")
            return install_return_code

    fabric_cli_result = check_fabric_cli()
    results = [
        fabric_cli_result,
        check_fabric_authentication(fabric_cli_result.status == "PASS"),
        check_azure_cli(),
        *get_target_checks(),
    ]
    print_results(results)
    return 1 if any(result.status == "FAIL" for result in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
