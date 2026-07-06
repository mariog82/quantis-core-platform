from services.billing import BillingService, Invoice, InvoiceLine
from services.compliance import ComplianceControl, ComplianceControlStatus, CompliancePolicy, ComplianceService
from services.licensing import Entitlement, License, LicenseType, LicensingService
from services.provisioning import ProvisioningRequest, ProvisioningService, ProvisioningStatus
from services.subscription import Subscription, SubscriptionPlan, SubscriptionService


def test_full_enterprise_services_flow():
    tenant_id = "tenant-demo"

    subscription = SubscriptionService()
    licensing = LicensingService()
    billing = BillingService()
    provisioning = ProvisioningService()
    compliance = ComplianceService()

    subscription.register_plan(
        SubscriptionPlan(
            key="enterprise",
            name="Enterprise",
            price_cents=29900,
            features=["analytics", "dashboard", "compliance"],
        )
    )
    subscription.subscribe(Subscription(tenant_id=tenant_id, plan_key="enterprise"))

    plan = subscription.get_plan_for_tenant(tenant_id)

    licensing.assign(
        License(
            tenant_id=tenant_id,
            license_type=LicenseType.ENTERPRISE,
            features=plan.features,
        )
    )

    entitlement = licensing.evaluate(
        Entitlement(tenant_id=tenant_id, feature="compliance")
    )

    provision_result = provisioning.provision(
        ProvisioningRequest(
            tenant_id=tenant_id,
            product_key="quantis-core",
            plan_key=plan.key,
        )
    )

    invoice = Invoice(
        tenant_id=tenant_id,
        lines=[InvoiceLine(description=plan.name, amount_cents=plan.price_cents)],
    )
    billing_result = billing.issue(invoice)

    compliance.register_policy(
        CompliancePolicy(
            key="gdpr-basic",
            name="GDPR Basic",
            required_controls=["audit"],
        )
    )
    compliance_result = compliance.evaluate_controls(
        "gdpr-basic",
        [
            ComplianceControl(
                key="audit",
                name="Audit Log",
                status=ComplianceControlStatus.IMPLEMENTED,
            )
        ],
    )

    assert entitlement.allowed is True
    assert provision_result.success is True
    assert provisioning.status(tenant_id) == ProvisioningStatus.PROVISIONED
    assert billing_result.data["total_cents"] == 29900
    assert compliance_result.compliant is True
