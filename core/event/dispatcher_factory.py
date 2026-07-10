from core.event.dispatcher import InMemoryEventDispatcher
from core.event.subscriber import EventSubscriber


class DispatcherFactory:
    @staticmethod
    def create(
        name: str = "memory",
        subscriber: EventSubscriber | None = None,
    ) -> InMemoryEventDispatcher:
        if name != "memory":
            raise ValueError(f"Unsupported dispatcher backend: {name}")

        return InMemoryEventDispatcher(subscriber=subscriber)
