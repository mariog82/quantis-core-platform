from pathlib import Path
import platform
import subprocess
import sys

def _read_version() -> str:
    return Path("VERSION").read_text(encoding="utf-8").strip()

def _git_commit() -> str:
    try:
        result = subprocess.run(["git", "rev-parse", "--short", "HEAD"], check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"

def version_command() -> int:
    print("Quantis Core Platform™")
    print()
    print(f"Version        : {_read_version()}")
    print("Milestone      : M7")
    print("Work Package   : WP1")
    print("Pull Request   : PR5")
    print("Codename       : Knowledge Graph Engine")
    print(f"Git Commit     : {_git_commit()}")
    print(f"Python         : {platform.python_version()}")
    print(f"Platform       : {platform.system()}")
    return 0

def main(argv: list[str] | None = None) -> int:
    arguments = list(sys.argv[1:] if argv is None else argv)
    if arguments == ["version"]:
        return version_command()
    print("Usage: python -m quantis version")
    return 2
