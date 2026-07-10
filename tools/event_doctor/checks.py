from dataclasses import dataclass, field

from core.event import (
    DispatcherFactory,
    Event,
    EventEnvelope,
    EventType,
    InMemoryEventSubscriber,
)


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
        subscriber = InMemoryEventSubscriber()
        received: list[str] = []
        subscriber.subscribe(
            "event.doctor",
            lambda envelope: received.append(envelope.event_id),
        )

        dispatcher = DispatcherFactory.create(subscriber=subscriber)
        envelope = EventEnvelope(Event(EventType("event.doctor"), {}))
        dispatched = dispatcher.dispatch(envelope)

        if not received or received[0] != envelope.event_id:
            report.issues.append(
                EventDoctorIssue(
                    "DISPATCHER_DELIVERY_FAILED",
                    "Dispatcher did not deliver the envelope to the registered handler.",
                )
            )

        if dispatched.event_id != envelope.event_id:
            report.issues.append(
                EventDoctorIssue(
                    "DISPATCHER_IDENTITY_CHANGED",
                    "Dispatcher changed the event identity.",
                )
            )
    except Exception as exc:
        report.issues.append(EventDoctorIssue("DISPATCHER_CHECK_FAILED", str(exc)))

    return report
