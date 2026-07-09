from pathlib import Path
<<<<<<< HEAD
from tools.repository_recovery.checks import run_repository_recovery


def main() -> int:
    removed = run_repository_recovery(Path.cwd())
    report = Path("docs/reports/repository-recovery-cleanup-report.md")
    report.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Repository Recovery Cleanup Report", "", f"Removed directories: `{len(removed)}`", ""]
    lines.extend(f"- `{item}`" for item in removed)
    report.write_text("\n".join(lines), encoding="utf-8")
=======

from tools.repository_recovery.cleanup import remove_pycache_only_directories


def main() -> int:
    result = remove_pycache_only_directories(Path.cwd())
    output = Path("docs/reports/repository-recovery-cleanup-report.md")
    output.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Repository Recovery Cleanup Report",
        "",
        f"Removed directories: `{result.count}`",
        "",
    ]
    for path in result.removed:
        lines.append(f"- `{path}`")
    output.write_text("\n".join(lines), encoding="utf-8")
>>>>>>> origin/develop
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
