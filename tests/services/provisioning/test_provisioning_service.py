from services.provisioning import (
    ProvisioningRequest,
    ProvisioningService,
    ProvisioningStatus,
)


def test_provisioning_service_creates_environment():
    service = ProvisioningService()
    request = ProvisioningRequest(
        tenant_id="tenant-demo",
        product_key="attentis-ai",
        plan_key="enterprise",
    )

    result = service.provision(request)

    assert result.success is True
    assert service.status("tenant-demo") == ProvisioningStatus.PROVISIONED
    assert service.get_environment("tenant-demo").product_key == "attentis-ai"


def test_provisioning_service_deprovisions_environment():
    service = ProvisioningService()
    service.provision(
        ProvisioningRequest(
            tenant_id="tenant-demo",
            product_key="attentis-ai",
            plan_key="enterprise",
        )
    )

    result = service.deprovision("tenant-demo")

    assert result.success is True
    assert service.status("tenant-demo") == ProvisioningStatus.DEPROVISIONED
    assert service.get_environment("tenant-demo") is None


def test_provisioning_service_returns_result_snapshot():
    service = ProvisioningService()
    service.provision(
        ProvisioningRequest(
            tenant_id="tenant-demo",
            product_key="quantis",
            plan_key="pro",
        )
    )

    result = service.result("tenant-demo")

    assert result.tenant_id == "tenant-demo"
    assert result.status == ProvisioningStatus.PROVISIONED
    assert result.resources["plan_key"] == "pro"
