from services.subscription import Subscription, SubscriptionPlan, SubscriptionService


def test_subscription_service_registers_plan_and_subscribes_tenant():
    service = SubscriptionService()
    service.register_plan(
        SubscriptionPlan(
            key="pro",
            name="Pro",
            price_cents=9900,
            features=["analytics"],
        )
    )

    result = service.subscribe(Subscription(tenant_id="tenant-demo", plan_key="pro"))

    assert result.success is True
    assert service.get_plan_for_tenant("tenant-demo").key == "pro"
