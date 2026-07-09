from dataclasses import dataclass, field

from core.event.contracts import EventEnvelope


@dataclass
class EventTopic:
    name: str
    envelopes: list[EventEnvelope] = field(default_factory=list)

    def append(self, envelope: EventEnvelope) -> None:
        self.envelopes.append(envelope)


@dataclass
class EventQueue:
    name: str
    envelopes: list[EventEnvelope] = field(default_factory=list)

    def push(self, envelope: EventEnvelope) -> None:
        self.envelopes.append(envelope)

    def pop(self) -> EventEnvelope | None:
        if not self.envelopes:
            return None
        return self.envelopes.pop(0)
