from dataclasses import dataclass
from typing import Any

from framework.di.container import DependencyContainer


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
    container: DependencyContainer | None = None

    def __post_init__(self) -> None:
        if self.container is None:
            self.container = DependencyContainer()

    def has_port(self, name: str) -> bool:
        return getattr(self, name, None) is not None

    def get_port(self, name: str) -> Any:
        return getattr(self, name, None)

    def register_dependency(self, token: str | type, instance: Any) -> None:
        self.container.register_instance(token, instance)

    def resolve_dependency(self, token: str | type) -> Any:
        return self.container.resolve(token)
