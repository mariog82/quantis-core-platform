from core.event.deadletter import InMemoryDeadLetterQueue


class DeadLetterQueueFactory:
    @staticmethod
    def create(name: str = "memory") -> InMemoryDeadLetterQueue:
        if name != "memory":
            raise ValueError(f"Unsupported dead letter queue backend: {name}")
        return InMemoryDeadLetterQueue()
