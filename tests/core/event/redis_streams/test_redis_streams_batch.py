from core.event import (
    Event,
    EventType,
    InMemoryRedisStreamsClient,
    RedisStreamsEventBus,
)


def test_redis_streams_event_bus_publishes_batch():
    bus = RedisStreamsEventBus(client=InMemoryRedisStreamsClient())

    results = bus.publish_many(
        [
            Event(EventType("metric.recorded"), {"value": 1}),
            Event(EventType("metric.recorded"), {"value": 2}),
        ]
    )

    assert len(results) == 2
    assert len(bus.read_stream("metric.recorded")) == 2
