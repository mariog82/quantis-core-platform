from typing import Any
from core.configuration.contracts import ConfigKey, ConfigScope, ConfigValue, ConfigurationProvider

class InMemoryConfigurationProvider(ConfigurationProvider):
    def __init__(self):
        self.items: dict[tuple[str | None, str], ConfigValue] = {}

    def get(self, key: str, default: Any = None, tenant_id: str | None = None) -> Any:
        scoped = self.items.get((tenant_id, key))
        if scoped is not None:
            return scoped.value
        platform = self.items.get((None, key))
        if platform is not None:
            return platform.value
        return default

    def set(self, key: str, value: Any, scope: ConfigScope = "platform", tenant_id: str | None = None) -> None:
        self.items[(tenant_id, key)] = ConfigValue(
            key=ConfigKey(key),
            value=value,
            scope=scope,
            tenant_id=tenant_id,
        )
