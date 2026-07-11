from core.event import EventBus
from core.outbox.repository import OutboxRepository


class OutboxPublisher:
    def __init__(
        self,
        repository: OutboxRepository,
        event_bus: EventBus,
    ) -> None:
        self.repository = repository
        self.event_bus = event_bus

    def publish_pending(self, limit: int = 100) -> int:
        published = 0

        for message in self.repository.pending(limit):
            try:
                self.event_bus.publish(message.envelope.event)
                self.repository.mark_published(message.message_id)
                published += 1
            except Exception as exc:
                self.repository.mark_failed(message.message_id, str(exc))

        return published
