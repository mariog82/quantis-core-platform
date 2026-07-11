from dataclasses import dataclass


@dataclass
class RedisStreamsMetrics:
    messages_published: int = 0
    messages_read: int = 0
    publish_failures: int = 0
    read_failures: int = 0
    active_subscriptions: int = 0
