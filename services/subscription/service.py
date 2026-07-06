from services.base import EnterpriseService, ServiceResult
from services.subscription.plan import SubscriptionPlan
from services.subscription.subscription import Subscription, SubscriptionStatus


class SubscriptionService(EnterpriseService):
    name = "subscription"

    def __init__(self):
        self._plans: dict[str, SubscriptionPlan] = {}
        self._subscriptions: dict[str, Subscription] = {}

    def register_plan(self, plan: SubscriptionPlan) -> ServiceResult:
        self._plans[plan.key] = plan
        return ServiceResult(success=True, data={"plan": plan.key})

    def subscribe(self, subscription: Subscription) -> ServiceResult:
        if subscription.plan_key not in self._plans:
            return ServiceResult(success=False, error="PLAN_NOT_FOUND")
        self._subscriptions[subscription.tenant_id] = subscription
        return ServiceResult(success=True, data={"tenant_id": subscription.tenant_id})

    def cancel(self, tenant_id: str) -> ServiceResult:
        subscription = self._subscriptions.get(tenant_id)
        if subscription is None:
            return ServiceResult(success=False, error="SUBSCRIPTION_NOT_FOUND")
        subscription.status = SubscriptionStatus.CANCELED
        return ServiceResult(success=True, data={"tenant_id": tenant_id})

    def get_subscription(self, tenant_id: str) -> Subscription | None:
        return self._subscriptions.get(tenant_id)

    def get_plan_for_tenant(self, tenant_id: str) -> SubscriptionPlan | None:
        subscription = self.get_subscription(tenant_id)
        if subscription is None:
            return None
        return self._plans.get(subscription.plan_key)

    def is_feature_available(self, tenant_id: str, feature: str) -> bool:
        subscription = self.get_subscription(tenant_id)
        if subscription is None or not subscription.is_active:
            return False
        plan = self._plans.get(subscription.plan_key)
        return plan.includes(feature) if plan else False
