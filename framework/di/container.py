from collections.abc import Callable
from typing import Any

from framework.di.exceptions import DependencyNotFound, DependencyRegistrationError
from framework.di.provider import FactoryProvider, InstanceProvider, SingletonProvider
from framework.di.token import DependencyToken


class DependencyContainer:
    def __init__(self):
        self._providers: dict[DependencyToken, object] = {}

    def register_instance(self, token: str | type, instance: Any) -> None:
        self._providers[DependencyToken.of(token)] = InstanceProvider(instance)

    def register_singleton(self, token: str | type, factory: Callable[[], Any]) -> None:
        if not callable(factory):
            raise DependencyRegistrationError("Singleton factory must be callable")
        self._providers[DependencyToken.of(token)] = SingletonProvider(factory)

    def register_factory(self, token: str | type, factory: Callable[[], Any]) -> None:
        if not callable(factory):
            raise DependencyRegistrationError("Factory must be callable")
        self._providers[DependencyToken.of(token)] = FactoryProvider(factory)

    def resolve(self, token: str | type) -> Any:
        dependency_token = DependencyToken.of(token)
        provider = self._providers.get(dependency_token)
        if provider is None:
            raise DependencyNotFound(dependency_token.name)
        return provider.resolve()

    def exists(self, token: str | type) -> bool:
        return DependencyToken.of(token) in self._providers

    def unregister(self, token: str | type) -> None:
        dependency_token = DependencyToken.of(token)
        if dependency_token not in self._providers:
            raise DependencyNotFound(dependency_token.name)
        self._providers.pop(dependency_token)

    def list_tokens(self) -> list[str]:
        return [token.name for token in self._providers]
