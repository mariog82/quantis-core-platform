from services.provisioning import ProvisioningRequest, ProvisioningService, ProvisioningStatus


def test_provisioning_service_provisions_tenant():
    service = ProvisioningService()
    request = ProvisioningRequest(
        tenant_id="tenant-demo",
        product_key="attentis-ai",
        plan_key="enterprise",
    )

    result = service.provision(request)

    assert result.success is True
    assert service.get("tenant-demo").status == ProvisioningStatus.PROVISIONED
