from core.eventbus.contracts import DomainEvent, EventHandler, EventId
from core.eventbus.in_memory import InMemoryEventBus

class EventBusService:
    def __init__(self, bus: InMemoryEventBus | None = None):
        self.bus = bus or InMemoryEventBus()

    def emit(
        self,
        event_type: str,
        aggregate_id: str,
        tenant_id: str | None = None,
        payload: dict | None = None,
        metadata: dict | None = None,
    ) -> DomainEvent:
        event = DomainEvent(
            id=EventId(),
            event_type=event_type,
            aggregate_id=aggregate_id,
            tenant_id=tenant_id,
            payload=payload or {},
            metadata=metadata or {},
        )
        self.bus.publish(event)
        return event

    def on(self, event_type: str, handler: EventHandler) -> None:
        self.bus.subscribe(event_type, handler)
