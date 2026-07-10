from pathlib import Path

from tools.event_doctor.checks import run_event_doctor_checks


def main() -> int:
    report = run_event_doctor_checks()
    output = Path("docs/reports/event-doctor-report.md")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report.to_markdown(), encoding="utf-8")
    print(report.to_markdown())
    return 0 if report.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
