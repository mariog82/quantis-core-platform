from services.licensing import Entitlement, License, LicenseType, LicensingService


def test_licensing_service_assigns_and_evaluates_license():
    service = LicensingService()
    service.assign(
        License(
            tenant_id="tenant-demo",
            license_type=LicenseType.ENTERPRISE,
            features=["analytics"],
        )
    )

    decision = service.evaluate(Entitlement(tenant_id="tenant-demo", feature="analytics"))

    assert decision.allowed is True


def test_licensing_service_revokes_license():
    service = LicensingService()
    service.assign(
        License(
            tenant_id="tenant-demo",
            license_type=LicenseType.TRIAL,
            features=["analytics"],
        )
    )

    result = service.revoke("tenant-demo")

    assert result.success is True
    assert service.is_feature_enabled("tenant-demo", "analytics") is False
