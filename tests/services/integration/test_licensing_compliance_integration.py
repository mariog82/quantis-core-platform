from services.compliance import ComplianceControl, ComplianceControlStatus, CompliancePolicy, ComplianceService
from services.licensing import Entitlement, License, LicenseType, LicensingService


def test_enterprise_license_can_enable_compliance_capability():
    licensing = LicensingService()
    compliance = ComplianceService()

    licensing.assign(
        License(
            tenant_id="tenant-demo",
            license_type=LicenseType.ENTERPRISE,
            features=["compliance"],
        )
    )

    decision = licensing.evaluate(
        Entitlement(tenant_id="tenant-demo", feature="compliance")
    )

    compliance.register_policy(
        CompliancePolicy(
            key="gdpr-basic",
            name="GDPR Basic",
            required_controls=["audit"],
        )
    )

    result = compliance.evaluate_controls(
        "gdpr-basic",
        [
            ComplianceControl(
                key="audit",
                name="Audit",
                status=ComplianceControlStatus.IMPLEMENTED,
            )
        ],
    )

    assert decision.allowed is True
    assert result.compliant is True
