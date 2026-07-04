from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class LicenseType(str, Enum):
    TRIAL = "trial"
    STANDARD = "standard"
    ENTERPRISE = "enterprise"


class LicenseStatus(str, Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"
    EXPIRED = "expired"


@dataclass
class License:
    tenant_id: str
    license_type: LicenseType
    status: LicenseStatus = LicenseStatus.ACTIVE
    features: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def allows(self, feature: str) -> bool:
        return self.status == LicenseStatus.ACTIVE and feature in self.features
