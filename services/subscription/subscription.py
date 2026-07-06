from dataclasses import dataclass
from enum import Enum


class SubscriptionStatus(str, Enum):
    ACTIVE = "active"
    TRIALING = "trialing"
    PAST_DUE = "past_due"
    CANCELED = "canceled"


@dataclass
class Subscription:
    tenant_id: str
    plan_key: str
    status: SubscriptionStatus = SubscriptionStatus.ACTIVE

    @property
    def is_active(self) -> bool:
        return self.status in {SubscriptionStatus.ACTIVE, SubscriptionStatus.TRIALING}
