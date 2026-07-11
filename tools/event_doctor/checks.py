from dataclasses import dataclass, field

from core.event import (
    Event,
    EventType,
    InMemoryRabbitMQClient,
    RabbitMQConfig,
    RabbitMQEventBus,
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
        client = InMemoryRabbitMQClient()
        bus = RabbitMQEventBus(
            client=client,
            config=RabbitMQConfig(
                exchange="doctor.events",
                queue_prefix="doctor",
            ),
        )

        received: list[str] = []
        bus.subscribe(
            "event.doctor",
            lambda envelope: received.append(envelope.event_id),
            subscriber_name="event-doctor",
        )

        event = Event(
            EventType("event.doctor"),
            {"transport": "rabbitmq"},
        )
        bus.publish(event)
        records = bus.read_queue(
            "event.doctor",
            subscriber_name="event-doctor",
        )

        if received != [event.event_id.value]:
            report.issues.append(
                EventDoctorIssue(
                    "RABBITMQ_DELIVERY_FAILED",
                    "RabbitMQ adapter did not invoke the subscriber.",
                )
            )

        if len(records) != 1 or records[0].event_id != event.event_id.value:
            report.issues.append(
                EventDoctorIssue(
                    "RABBITMQ_PERSISTENCE_FAILED",
                    "RabbitMQ adapter did not preserve the serialized event.",
                )
            )
    except Exception as exc:
        report.issues.append(
            EventDoctorIssue("RABBITMQ_CHECK_FAILED", str(exc))
        )

    return report
