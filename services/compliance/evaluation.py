from dataclasses import dataclass, field

from services.compliance.control import ComplianceControl
from services.compliance.policy import CompliancePolicy


@dataclass
class ComplianceEvaluation:
    policy: CompliancePolicy
    controls: list[ComplianceControl]


@dataclass
class ComplianceEvaluationResult:
    policy_key: str
    compliant: bool
    implemented_controls: list[str] = field(default_factory=list)
    missing_controls: list[str] = field(default_factory=list)
    partial_controls: list[str] = field(default_factory=list)
