from core.event import (
    RedisStreamsEventBus,
    RedisStreamsEventBusFactory,
)


def test_redis_streams_factory_creates_bus():
    assert isinstance(
        RedisStreamsEventBusFactory.create(),
        RedisStreamsEventBus,
    )
