from dataclasses import dataclass, field
from typing import Any


@dataclass
class ProvisionedEnvironment:
    tenant_id: str
    product_key: str
    plan_key: str
    resources: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def resource(self, key: str) -> Any:
        return self.resources.get(key)
