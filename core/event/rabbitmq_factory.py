from core.event.rabbitmq import (
    InMemoryRabbitMQClient,
    RabbitMQConfig,
    RabbitMQEventBus,
)


class RabbitMQEventBusFactory:
    @staticmethod
    def create(
        client: InMemoryRabbitMQClient | None = None,
        config: RabbitMQConfig | None = None,
    ) -> RabbitMQEventBus:
        return RabbitMQEventBus(
            client=client or InMemoryRabbitMQClient(),
            config=config,
        )
