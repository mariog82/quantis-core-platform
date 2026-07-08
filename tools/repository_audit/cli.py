from pathlib import Path

from tools.repository_audit.audit import run_repository_audit


def main() -> int:
    report = run_repository_audit(Path.cwd())
    output_path = Path("docs/reports/repository-audit-report.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report.to_markdown(), encoding="utf-8")

    print(report.to_markdown())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
