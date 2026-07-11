from services.billing import BillingService, Invoice, InvoiceLine
from services.subscription import Subscription, SubscriptionPlan, SubscriptionService


def test_subscription_plan_generates_invoice():
    subscriptions = SubscriptionService()
    billing = BillingService()

    subscriptions.register_plan(
        SubscriptionPlan(
            key="enterprise",
            name="Enterprise",
            price_cents=29900,
            features=["analytics", "reporting"],
        )
    )
    subscriptions.subscribe(Subscription(tenant_id="tenant-demo", plan_key="enterprise"))

    plan = subscriptions.get_plan_for_tenant("tenant-demo")
    invoice = Invoice(
        tenant_id="tenant-demo",
        lines=[InvoiceLine(description=plan.name, amount_cents=plan.price_cents)],
    )

    result = billing.issue(invoice)

    assert result.success is True
    assert result.data["total_cents"] == 29900
