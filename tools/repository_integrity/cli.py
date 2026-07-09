from pathlib import Path
from tools.repository_integrity.checks import run_repository_integrity_checks


def main() -> int:
    missing = run_repository_integrity_checks(Path.cwd())
    report = Path("docs/reports/repository-integrity-report.md")
    report.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Repository Integrity Report", "", f"Status: `{'PASS' if not missing else 'FAIL'}`", ""]
    lines.extend(f"- Missing `{item}`" for item in missing)
    report.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    return 0 if not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
