from services.licensing import Entitlement, License, LicensePolicy, LicenseStatus, LicenseType


def test_license_policy_allows_active_feature():
    policy = LicensePolicy()
    license = License(
        tenant_id="tenant-demo",
        license_type=LicenseType.ENTERPRISE,
        features=["analytics"],
    )

    decision = policy.evaluate(license, Entitlement(tenant_id="tenant-demo", feature="analytics"))

    assert decision.allowed is True


def test_license_policy_denies_missing_feature():
    policy = LicensePolicy()
    license = License(
        tenant_id="tenant-demo",
        license_type=LicenseType.STANDARD,
        features=["dashboard"],
    )

    decision = policy.evaluate(license, Entitlement(tenant_id="tenant-demo", feature="analytics"))

    assert decision.allowed is False
    assert decision.reason == "FEATURE_NOT_LICENSED"


def test_license_policy_denies_suspended_license():
    policy = LicensePolicy()
    license = License(
        tenant_id="tenant-demo",
        license_type=LicenseType.STANDARD,
        status=LicenseStatus.SUSPENDED,
        features=["analytics"],
    )

    decision = policy.evaluate(license, Entitlement(tenant_id="tenant-demo", feature="analytics"))

    assert decision.allowed is False
    assert decision.reason == "LICENSE_SUSPENDED"


def test_license_policy_denies_limit_exceeded():
    policy = LicensePolicy()
    license = License(
        tenant_id="tenant-demo",
        license_type=LicenseType.ENTERPRISE,
        features=["users"],
        limits={"users": 10},
    )

    decision = policy.evaluate(
        license,
        Entitlement(tenant_id="tenant-demo", feature="users", quantity=11),
    )

    assert decision.allowed is False
    assert decision.reason == "FEATURE_LIMIT_EXCEEDED"
    assert decision.metadata["limit"] == 10
