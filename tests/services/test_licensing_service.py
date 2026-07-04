from services.licensing import License, LicenseType, LicensingService


def test_licensing_service_enables_feature():
    service = LicensingService()
    service.assign(
        License(
            tenant_id="tenant-demo",
            license_type=LicenseType.ENTERPRISE,
            features=["analytics"],
        )
    )

    assert service.is_feature_enabled("tenant-demo", "analytics") is True
    assert service.is_feature_enabled("tenant-demo", "billing") is False
