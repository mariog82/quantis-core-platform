from core.event.redis_streams import (
    InMemoryRedisStreamsClient,
    RedisStreamsConfig,
    RedisStreamsEventBus,
)


class RedisStreamsEventBusFactory:
    @staticmethod
    def create(
        client: InMemoryRedisStreamsClient | None = None,
        config: RedisStreamsConfig | None = None,
    ) -> RedisStreamsEventBus:
        return RedisStreamsEventBus(
            client=client or InMemoryRedisStreamsClient(),
            config=config,
        )
