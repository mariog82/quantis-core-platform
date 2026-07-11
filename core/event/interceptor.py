from dataclasses import dataclass, field

from core.event.contracts import EventEnvelope


@dataclass
class RecordingInterceptor:
    before: list[str] = field(default_factory=list)
    after: list[str] = field(default_factory=list)

    def before_dispatch(self, envelope: EventEnvelope) -> None:
        self.before.append(envelope.event_id)

    def after_dispatch(self, envelope: EventEnvelope) -> None:
        self.after.append(envelope.event_id)
