from dataclasses import dataclass, field


@dataclass
class PlanFeature:
    key: str
    limit: int | None = None


@dataclass
class SubscriptionPlan:
    key: str
    name: str
    price_cents: int = 0
    currency: str = "EUR"
    features: list[str] = field(default_factory=list)
    feature_limits: dict[str, int] = field(default_factory=dict)

    def includes(self, feature: str) -> bool:
        return feature in self.features

    def limit_for(self, feature: str) -> int | None:
        return self.feature_limits.get(feature)
