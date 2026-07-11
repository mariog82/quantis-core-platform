from dataclasses import dataclass, field

from core.event import (
    Event,
    EventType,
    InMemoryKafkaClient,
    KafkaConfig,
    KafkaEventBus,
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
        client = InMemoryKafkaClient()
        bus = KafkaEventBus(
            client=client,
            config=KafkaConfig(topic_prefix="doctor"),
        )

        received: list[str] = []
        bus.subscribe(
            "event.doctor",
            lambda envelope: received.append(envelope.event_id),
            subscriber_name="event-doctor",
        )

        event = Event(
            EventType("event.doctor"),
            {"transport": "kafka"},
        )
        bus.publish(event)
        records = bus.read_topic("event.doctor")

        if received != [event.event_id.value]:
            report.issues.append(
                EventDoctorIssue(
                    "KAFKA_DELIVERY_FAILED",
                    "Kafka adapter did not invoke the subscriber.",
                )
            )

        if len(records) != 1 or records[0].event_id != event.event_id.value:
            report.issues.append(
                EventDoctorIssue(
                    "KAFKA_PERSISTENCE_FAILED",
                    "Kafka adapter did not preserve the serialized event.",
                )
            )
    except Exception as exc:
        report.issues.append(
            EventDoctorIssue("KAFKA_CHECK_FAILED", str(exc))
        )

    return report
