from pathlib import Path
from tools.repository_audit.checks import run_repository_audit


def main() -> int:
    data = run_repository_audit(Path.cwd())
    report = Path("docs/reports/repository-audit-report.md")
    report.parent.mkdir(parents=True, exist_ok=True)
    text = f"# Repository Audit Report\n\nStatus: `PASS`\n\n- Files: `{data['files']}`\n- Python files: `{data['python_files']}`\n"
    report.write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
