from core.event.subscriber import InMemoryEventSubscriber


class SubscriberFactory:
    @staticmethod
    def create(name: str = "memory") -> InMemoryEventSubscriber:
        if name != "memory":
            raise ValueError(f"Unsupported subscriber backend: {name}")
        return InMemoryEventSubscriber()
