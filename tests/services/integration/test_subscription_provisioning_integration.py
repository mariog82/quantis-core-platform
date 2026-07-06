from services.provisioning import ProvisioningRequest, ProvisioningService, ProvisioningStatus
from services.subscription import Subscription, SubscriptionPlan, SubscriptionService


def test_subscription_plan_can_provision_tenant_environment():
    subscriptions = SubscriptionService()
    provisioning = ProvisioningService()

    subscriptions.register_plan(
        SubscriptionPlan(
            key="enterprise",
            name="Enterprise",
            price_cents=29900,
            features=["analytics", "dashboard"],
        )
    )
    subscriptions.subscribe(Subscription(tenant_id="tenant-demo", plan_key="enterprise"))

    plan = subscriptions.get_plan_for_tenant("tenant-demo")
    result = provisioning.provision(
        ProvisioningRequest(
            tenant_id="tenant-demo",
            product_key="quantis-core",
            plan_key=plan.key,
        )
    )

    assert result.success is True
    assert provisioning.status("tenant-demo") == ProvisioningStatus.PROVISIONED
