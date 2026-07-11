from dataclasses import dataclass


@dataclass
class EventBusMetrics:
    published: int = 0
    dispatched: int = 0
    failed: int = 0
    subscribers: int = 0
    batches: int = 0
