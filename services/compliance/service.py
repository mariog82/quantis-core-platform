from services.base import EnterpriseService, ServiceResult
from services.compliance.control import ComplianceControl, ComplianceControlStatus
from services.compliance.evaluation import ComplianceEvaluationResult
from services.compliance.policy import CompliancePolicy


class ComplianceService(EnterpriseService):
    name = "compliance"

    def __init__(self):
        self._policies: dict[str, CompliancePolicy] = {}

    def register_policy(self, policy: CompliancePolicy) -> ServiceResult:
        self._policies[policy.key] = policy
        return ServiceResult(success=True, data={"policy": policy.key})

    def get_policy(self, policy_key: str) -> CompliancePolicy | None:
        return self._policies.get(policy_key)

    def evaluate_controls(
        self,
        policy_key: str,
        controls: list[ComplianceControl],
    ) -> ComplianceEvaluationResult:
        policy = self.get_policy(policy_key)
        if policy is None:
            return ComplianceEvaluationResult(policy_key=policy_key, compliant=False)

        controls_by_key = {control.key: control for control in controls}
        implemented = []
        partial = []
        missing = []

        for required_key in policy.required_controls:
            control = controls_by_key.get(required_key)
            if control is None:
                missing.append(required_key)
                continue
            if control.status == ComplianceControlStatus.IMPLEMENTED:
                implemented.append(required_key)
            elif control.status == ComplianceControlStatus.PARTIAL:
                partial.append(required_key)
            else:
                missing.append(required_key)

        return ComplianceEvaluationResult(
            policy_key=policy.key,
            compliant=not missing and not partial,
            implemented_controls=implemented,
            missing_controls=missing,
            partial_controls=partial,
        )

    def evaluate(self, policy_key: str, implemented_controls: list[str]) -> ServiceResult:
        policy = self.get_policy(policy_key)
        if policy is None:
            return ServiceResult(success=False, error="POLICY_NOT_FOUND")
        controls = [
            ComplianceControl(
                key=control_key,
                name=control_key,
                status=ComplianceControlStatus.IMPLEMENTED,
            )
            for control_key in implemented_controls
        ]
        result = self.evaluate_controls(policy_key, controls)
        return ServiceResult(
            success=result.compliant,
            data={
                "policy_key": result.policy_key,
                "implemented_controls": result.implemented_controls,
                "missing_controls": result.missing_controls,
                "partial_controls": result.partial_controls,
            },
        )
