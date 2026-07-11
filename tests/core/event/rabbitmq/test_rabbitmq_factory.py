from core.event import (
    RabbitMQEventBus,
    RabbitMQEventBusFactory,
)


def test_rabbitmq_factory_creates_bus():
    assert isinstance(
        RabbitMQEventBusFactory.create(),
        RabbitMQEventBus,
    )
