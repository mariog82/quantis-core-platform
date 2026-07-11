from core.event import (
    KafkaEventBus,
    KafkaEventBusFactory,
)


def test_kafka_factory_creates_bus():
    assert isinstance(
        KafkaEventBusFactory.create(),
        KafkaEventBus,
    )
