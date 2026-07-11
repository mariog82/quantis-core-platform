from core.event import Event, EventEnvelope, EventType, InMemoryEventBus
from core.outbox import (
    InMemoryOutboxRepository,
    OutboxMessage,
    OutboxPublisher,
    OutboxStatus,
)


def test_outbox_publishes_pending_messages():
    repository = InMemoryOutboxRepository()
    bus = InMemoryEventBus()
    received = []

    bus.subscribe(
        "invoice.generated",
        lambda envelope: received.append(envelope.event.payload["invoice_id"]),
    )

    message = repository.add(
        OutboxMessage(
            EventEnvelope(
                Event(
                    EventType("invoice.generated"),
                    {"invoice_id": "i1"},
                )
            )
        )
    )

    publisher = OutboxPublisher(repository, bus)

    assert publisher.publish_pending() == 1
    assert received == ["i1"]
    assert repository.pending() == []
    assert repository.mark_published(message.message_id).status == OutboxStatus.PUBLISHED
