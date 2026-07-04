from services.base import EnterpriseService, ServiceResult
from services.compliance.policy import CompliancePolicy


class ComplianceService(EnterpriseService):
    name = "compliance"

    def __init__(self):
        self._policies: dict[str, CompliancePolicy] = {}

    def register_policy(self, policy: CompliancePolicy) -> ServiceResult:
        self._policies[policy.key] = policy
        return ServiceResult(success=True, data={"policy": policy.key})

    def evaluate(self, policy_key: str, implemented_controls: list[str]) -> ServiceResult:
        policy = self._policies.get(policy_key)
        if policy is None:
            return ServiceResult(success=False, error="POLICY_NOT_FOUND")

        missing = [
            control
            for control in policy.required_controls
            if control not in implemented_controls
        ]

        return ServiceResult(success=not missing, data={"missing_controls": missing})
