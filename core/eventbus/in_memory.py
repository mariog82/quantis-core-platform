from collections import defaultdict
from core.eventbus.contracts import DomainEvent, EventHandler, EventPublisher, EventSubscriber

class InMemoryEventBus(EventPublisher, EventSubscriber):
    def __init__(self):
        self.handlers: dict[str, list[EventHandler]] = defaultdict(list)
        self.published: list[DomainEvent] = []

    def subscribe(self, event_type: str, handler: EventHandler) -> None:
        self.handlers[event_type].append(handler)

    def publish(self, event: DomainEvent) -> None:
        self.published.append(event)
        for handler in self.handlers.get(event.event_type, []):
            handler(event)
        for handler in self.handlers.get("*", []):
            handler(event)
