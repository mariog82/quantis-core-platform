from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class ComplianceControlStatus(str, Enum):
    IMPLEMENTED = "implemented"
    MISSING = "missing"
    PARTIAL = "partial"


@dataclass
class ComplianceControl:
    key: str
    name: str
    status: ComplianceControlStatus = ComplianceControlStatus.MISSING
    evidence: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def is_implemented(self) -> bool:
        return self.status == ComplianceControlStatus.IMPLEMENTED
