from dataclasses import dataclass, field
from enum import Enum


class ModuleHealth(str, Enum):
    READY = "READY"
    DEGRADED = "DEGRADED"
    FAILED = "FAILED"
    UNKNOWN = "UNKNOWN"


class RuntimeHealth(str, Enum):
    READY = "READY"
    PARTIAL = "PARTIAL"
    FAILED = "FAILED"


@dataclass
class HealthReport:
    component: str
    status: ModuleHealth | RuntimeHealth
    details: dict = field(default_factory=dict)
