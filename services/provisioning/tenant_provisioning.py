from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class ProvisioningStatus(str, Enum):
    REQUESTED = "requested"
    PROVISIONING = "provisioning"
    PROVISIONED = "provisioned"
    FAILED = "failed"
    DEPROVISIONED = "deprovisioned"


@dataclass
class ProvisioningRequest:
    tenant_id: str
    product_key: str
    plan_key: str
    requested_by: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    status: ProvisioningStatus = ProvisioningStatus.REQUESTED


@dataclass
class ProvisioningResult:
    tenant_id: str
    status: ProvisioningStatus
    resources: dict[str, Any] = field(default_factory=dict)
    error: str | None = None
