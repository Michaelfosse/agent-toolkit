#!/usr/bin/env python3
"""Check native Windows or WSL-plus-Windows Power BI developer readiness."""

from __future__ import annotations

import os
import platform
import shutil
import subprocess
from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class CheckResult:
    """Represent one environment check."""

    status: str
    name: str
    detail: str
    next_action: str | None = None


def run_command(command: Sequence[str], timeout: int = 30) -> int:
    """Run a command without exposing captured output.

    Args:
        command: Executable and arguments.
        timeout: Maximum execution time in seconds.

    Returns:
        Command exit code, or one for launch and timeout failures.
    """
    try:
        result = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except (OSError, subprocess.TimeoutExpired):
        return 1
    return result.returncode


def detect_mode() -> str:
    """Detect the supported Power BI execution mode.

    Returns:
        ``windows``, ``wsl-windows``, or ``unsupported``.
    """
    if platform.system() == "Windows":
        return "windows"
    if platform.system() == "Linux" and (
        "WSL_DISTRO_NAME" in os.environ or "microsoft" in platform.release().lower()
    ):
        return "wsl-windows"
    return "unsupported"


def check_command(name: str, command: Sequence[str], next_action: str) -> CheckResult:
    """Check whether a required command can run.

    Args:
        name: Human-readable check name.
        command: Probe command.
        next_action: Remediation when the probe fails.

    Returns:
        Check result.
    """
    if run_command(command) == 0:
        return CheckResult("PASS", name, "Available.")
    return CheckResult("FAIL", name, "Unavailable.", next_action)


def check_agent_tools() -> list[CheckResult]:
    """Check web-service tools in the agent environment.

    Returns:
        Fabric and Azure CLI readiness checks.
    """
    results: list[CheckResult] = []
    if shutil.which("fab"):
        results.append(CheckResult("PASS", "Fabric CLI", "Available in agent environment."))
    else:
        results.append(
            CheckResult(
                "WARN",
                "Fabric CLI",
                "Unavailable in agent environment.",
                "Install only if published validation is needed, using the active Python interpreter: -m pip install ms-fabric-cli",
            )
        )
    if shutil.which("az"):
        results.append(CheckResult("PASS", "Azure CLI", "Available in agent environment."))
    else:
        results.append(
            CheckResult(
                "WARN",
                "Azure CLI",
                "Unavailable in agent environment.",
                "Install Azure CLI or configure another approved binary downloader.",
            )
        )
    return results


def check_windows_tools(mode: str) -> list[CheckResult]:
    """Check Windows interoperability and Desktop-bound tools.

    Args:
        mode: Detected execution mode.

    Returns:
        Windows process and Power BI CLI checks.
    """
    if mode == "unsupported":
        return [
            CheckResult(
                "FAIL",
                "Windows host",
                "Power BI Desktop integration requires native Windows or WSL on Windows.",
            )
        ]

    shell = ["cmd.exe", "/d", "/s", "/c"] if mode == "wsl-windows" else ["cmd.exe", "/d", "/s", "/c"]
    windows_runtime = check_command(
        "Windows Node.js and npx",
        [*shell, "node.exe --version && npx.cmd --version"],
        "Install maintained Node.js on Windows and ensure node.exe and npx.cmd are on Windows PATH.",
    )
    on_demand_status = "PASS" if windows_runtime.status == "PASS" else "FAIL"
    on_demand_detail = (
        "Available on demand through Windows npx; the package is cached on first use."
        if on_demand_status == "PASS"
        else "Blocked because Windows npx is unavailable."
    )
    return [
        check_command(
            "Windows interoperability",
            [*shell, "ver"],
            "Enable WSL interoperability or run the agent on Windows.",
        ),
        windows_runtime,
        CheckResult(
            on_demand_status,
            "Desktop Bridge CLI",
            on_demand_detail,
            None if on_demand_status == "PASS" else "Install maintained Node.js on Windows.",
        ),
        CheckResult(
            on_demand_status,
            "Report authoring CLI",
            on_demand_detail,
            None if on_demand_status == "PASS" else "Install maintained Node.js on Windows.",
        ),
    ]


def main() -> int:
    """Print capability-oriented setup results.

    Returns:
        Zero when Desktop-bound required checks pass; one when blocked.
    """
    mode = detect_mode()
    results = [*check_windows_tools(mode), *check_agent_tools()]
    print(f"Detected mode: {mode}\n")
    for result in results:
        print(f"[{result.status}] {result.name}: {result.detail}")
        if result.next_action:
            print(f"       Next: {result.next_action}")
    print("[UNKNOWN] Power BI Desktop preview feature: Verify in a running Desktop instance.")
    print("[UNKNOWN] Tenant, capacity, and permissions: Verify against a human-approved target.")
    return 1 if any(result.status == "FAIL" for result in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
