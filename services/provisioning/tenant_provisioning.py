from dataclasses import dataclass
from enum import Enum


class ProvisioningStatus(str, Enum):
    REQUESTED = "requested"
    PROVISIONED = "provisioned"
    FAILED = "failed"


@dataclass
class ProvisioningRequest:
    tenant_id: str
    product_key: str
    plan_key: str
    status: ProvisioningStatus = ProvisioningStatus.REQUESTED
