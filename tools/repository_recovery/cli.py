from pathlib import Path
from tools.repository_recovery.checks import run_repository_recovery


def main() -> int:
    removed = run_repository_recovery(Path.cwd())
    report = Path("docs/reports/repository-recovery-cleanup-report.md")
    report.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Repository Recovery Cleanup Report", "", f"Removed directories: `{len(removed)}`", ""]
    lines.extend(f"- `{item}`" for item in removed)
    report.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
