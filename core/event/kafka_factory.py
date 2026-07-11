from core.event.kafka import (
    InMemoryKafkaClient,
    KafkaConfig,
    KafkaEventBus,
)


class KafkaEventBusFactory:
    @staticmethod
    def create(
        client: InMemoryKafkaClient | None = None,
        config: KafkaConfig | None = None,
    ) -> KafkaEventBus:
        return KafkaEventBus(
            client=client or InMemoryKafkaClient(),
            config=config,
        )
