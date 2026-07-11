from dataclasses import dataclass


@dataclass
class SubscriberMetrics:
    subscriptions_created: int = 0
    subscriptions_removed: int = 0
    handlers_invoked: int = 0
    handler_failures: int = 0
