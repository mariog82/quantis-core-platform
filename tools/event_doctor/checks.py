from dataclasses import dataclass, field

from core.event import EventType, SubscriberFactory


@dataclass(frozen=True)
class EventDoctorIssue:
    code: str
    message: str


@dataclass
class EventDoctorReport:
    issues: list[EventDoctorIssue] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.issues

    def to_markdown(self) -> str:
        lines = [
            "# Event Doctor Report",
            "",
            f"Status: `{'PASS' if self.passed else 'FAIL'}`",
            "",
        ]
        for issue in self.issues:
            lines.append(f"- `{issue.code}` — {issue.message}")
        return "\n".join(lines)


EventDoctorIssue.__test__ = False
EventDoctorReport.__test__ = False


def run_event_doctor_checks() -> EventDoctorReport:
    report = EventDoctorReport()

    try:
        EventType("event.doctor")
    except ValueError as exc:
        report.issues.append(EventDoctorIssue("EVENT_TYPE_INVALID", str(exc)))

    try:
        SubscriberFactory.create("memory")
    except Exception as exc:
        report.issues.append(EventDoctorIssue("SUBSCRIBER_FACTORY_FAILED", str(exc)))

    return report
