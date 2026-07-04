from services.compliance import CompliancePolicy, ComplianceService


def test_compliance_service_evaluates_policy():
    service = ComplianceService()
    service.register_policy(
        CompliancePolicy(
            key="gdpr-basic",
            name="GDPR Basic",
            required_controls=["audit", "retention"],
        )
    )

    result = service.evaluate("gdpr-basic", ["audit"])

    assert result.success is False
    assert result.data["missing_controls"] == ["retention"]
