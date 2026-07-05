from services.subscription import Subscription, SubscriptionPlan, SubscriptionService, SubscriptionStatus


def test_subscription_service_feature_availability():
    service = SubscriptionService()
    service.register_plan(
        SubscriptionPlan(
            key="pro",
            name="Pro",
            price_cents=9900,
            features=["analytics", "dashboard"],
        )
    )
    service.subscribe(Subscription(tenant_id="tenant-demo", plan_key="pro"))

    assert service.is_feature_available("tenant-demo", "analytics") is True
    assert service.is_feature_available("tenant-demo", "billing") is False


def test_subscription_service_cancel():
    service = SubscriptionService()
    service.register_plan(SubscriptionPlan(key="base", name="Base"))
    service.subscribe(Subscription(tenant_id="tenant-demo", plan_key="base"))

    result = service.cancel("tenant-demo")

    assert result.success is True
    assert service.get_subscription("tenant-demo").status == SubscriptionStatus.CANCELED
