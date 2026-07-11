from dataclasses import dataclass


@dataclass
class RabbitMQMetrics:
    exchanges_declared: int = 0
    queues_declared: int = 0
    bindings_created: int = 0
    messages_published: int = 0
    messages_consumed: int = 0
    publish_failures: int = 0
    consume_failures: int = 0
