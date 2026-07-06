from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class AdapterMetadata:
    name: str
    adapter_type: str
    version: str = "0.5.0-alpha.2"
    description: str = ""
    capabilities: list[str] = field(default_factory=list)
    provider: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
