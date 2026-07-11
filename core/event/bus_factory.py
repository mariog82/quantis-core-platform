from core.event.bus import InMemoryEventBus
from core.event.deadletter import DeadLetterQueue
from core.event.retry import RetryPolicy


class EventBusFactory:
    @staticmethod
    def create(
        name: str = "memory",
        dead_letter_queue: DeadLetterQueue | None = None,
        retry_policy: RetryPolicy | None = None,
    ) -> InMemoryEventBus:
        if name != "memory":
            raise ValueError(f"Unsupported event bus backend: {name}")

        return InMemoryEventBus(
            dead_letter_queue=dead_letter_queue,
            retry_policy=retry_policy,
        )
