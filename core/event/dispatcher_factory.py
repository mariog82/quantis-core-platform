from core.event.deadletter import DeadLetterQueue
from core.event.dispatcher import InMemoryEventDispatcher
from core.event.retry import RetryPolicy
from core.event.subscriber import EventSubscriber


class DispatcherFactory:
    @staticmethod
    def create(
        name: str = "memory",
        subscriber: EventSubscriber | None = None,
        dead_letter_queue: DeadLetterQueue | None = None,
        retry_policy: RetryPolicy | None = None,
    ) -> InMemoryEventDispatcher:
        if name != "memory":
            raise ValueError(f"Unsupported dispatcher backend: {name}")

        return InMemoryEventDispatcher(
            subscriber=subscriber,
            dead_letter_queue=dead_letter_queue,
            retry_policy=retry_policy,
        )
