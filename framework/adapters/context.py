from dataclasses import dataclass, field
from typing import Any


@dataclass
class AdapterContext:
    tenant_id: str | None = None
    actor_id: str | None = None
    correlation_id: str | None = None
    configuration: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)
