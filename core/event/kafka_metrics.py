from dataclasses import dataclass


@dataclass
class KafkaMetrics:
    messages_produced: int = 0
    messages_consumed: int = 0
    produce_failures: int = 0
    consume_failures: int = 0
    active_subscriptions: int = 0
