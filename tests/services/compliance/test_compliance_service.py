from services.compliance import (
    ComplianceControl,
    ComplianceControlStatus,
    CompliancePolicy,
    ComplianceService,
)


def test_compliance_service_registers_and_evaluates_policy():
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


def test_compliance_service_evaluates_full_controls():
    service = ComplianceService()
    service.register_policy(
        CompliancePolicy(
            key="security-basic",
            name="Security Basic",
            required_controls=["audit", "backup"],
        )
    )

    result = service.evaluate_controls(
        "security-basic",
        [
            ComplianceControl(
                key="audit",
                name="Audit Log",
                status=ComplianceControlStatus.IMPLEMENTED,
            ),
            ComplianceControl(
                key="backup",
                name="Backup",
                status=ComplianceControlStatus.IMPLEMENTED,
            ),
        ],
    )

    assert result.compliant is True
    assert result.missing_controls == []


def test_compliance_service_detects_partial_control():
    service = ComplianceService()
    service.register_policy(
        CompliancePolicy(
            key="nis2-basic",
            name="NIS2 Basic",
            required_controls=["incident-response"],
        )
    )

    result = service.evaluate_controls(
        "nis2-basic",
        [
            ComplianceControl(
                key="incident-response",
                name="Incident Response",
                status=ComplianceControlStatus.PARTIAL,
            )
        ],
    )

    assert result.compliant is False
    assert result.partial_controls == ["incident-response"]
