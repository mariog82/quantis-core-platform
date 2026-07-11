from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Any

from framework.di.scope import DependencyScope


class DependencyProvider(ABC):
    scope: DependencyScope

    @abstractmethod
    def resolve(self) -> Any:
        raise NotImplementedError


class InstanceProvider(DependencyProvider):
    scope = DependencyScope.INSTANCE

    def __init__(self, instance: Any):
        self.instance = instance

    def resolve(self) -> Any:
        return self.instance


class SingletonProvider(DependencyProvider):
    scope = DependencyScope.SINGLETON

    def __init__(self, factory: Callable[[], Any]):
        self.factory = factory
        self._instance: Any = None
        self._resolved = False

    def resolve(self) -> Any:
        if not self._resolved:
            self._instance = self.factory()
            self._resolved = True
        return self._instance


class FactoryProvider(DependencyProvider):
    scope = DependencyScope.FACTORY

    def __init__(self, factory: Callable[[], Any]):
        self.factory = factory

    def resolve(self) -> Any:
        return self.factory()
