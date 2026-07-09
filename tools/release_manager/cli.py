from pathlib import Path
from tools.release_manager.checks import run_release_manager_checks


def main() -> int:
    issues = run_release_manager_checks(Path.cwd())
    report = Path("docs/reports/release-manager-report.md")
    report.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Release Manager Report", "", f"Status: `{'PASS' if not issues else 'FAIL'}`", ""]
    lines.extend(f"- {item}" for item in issues)
    report.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
