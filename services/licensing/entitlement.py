from dataclasses import dataclass, field
from typing import Any


@dataclass
class Entitlement:
    tenant_id: str
    feature: str
    quantity: int = 1
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class EntitlementDecision:
    allowed: bool
    reason: str = "ALLOWED"
    metadata: dict[str, Any] = field(default_factory=dict)
