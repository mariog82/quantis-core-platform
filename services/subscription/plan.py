from dataclasses import dataclass, field


@dataclass
class SubscriptionPlan:
    key: str
    name: str
    price_cents: int = 0
    features: list[str] = field(default_factory=list)
