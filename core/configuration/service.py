from typing import Any
from core.configuration.contracts import ConfigScope, ConfigurationProvider
from core.configuration.in_memory import InMemoryConfigurationProvider

class ConfigurationService:
    def __init__(self, provider: ConfigurationProvider | None = None):
        self.provider = provider or InMemoryConfigurationProvider()

    def get(self, key: str, default: Any = None, tenant_id: str | None = None) -> Any:
        return self.provider.get(key, default=default, tenant_id=tenant_id)

    def set(self, key: str, value: Any, scope: ConfigScope = "platform", tenant_id: str | None = None) -> None:
        self.provider.set(key, value, scope=scope, tenant_id=tenant_id)
