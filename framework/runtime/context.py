from dataclasses import dataclass
from typing import Any

@dataclass
class RuntimeContext:
    identity: Any = None
    tenant: Any = None
    rbac: Any = None
    audit: Any = None
    configuration: Any = None
    eventbus: Any = None
    logger: Any = None
    metrics: Any = None
    tracer: Any = None

    def has_port(self, name: str) -> bool:
        return getattr(self, name, None) is not None

    def get_port(self, name: str):
        return getattr(self, name, None)
