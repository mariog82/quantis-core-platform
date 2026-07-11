from dataclasses import dataclass, field
from typing import Any, Literal

ConfigScope = Literal["platform", "tenant", "module", "vertical"]

@dataclass(frozen=True)
class ConfigKey:
    value: str

@dataclass
class ConfigValue:
    key: ConfigKey
    value: Any
    scope: ConfigScope = "platform"
    tenant_id: str | None = None
    metadata: dict = field(default_factory=dict)

class ConfigurationProvider:
    def get(self, key: str, default: Any = None, tenant_id: str | None = None) -> Any:
        raise NotImplementedError

    def set(self, key: str, value: Any, scope: ConfigScope = "platform", tenant_id: str | None = None) -> None:
        raise NotImplementedError
