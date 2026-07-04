import pytest

from framework.di import DependencyContainer, DependencyNotFound


class DemoService:
    def __init__(self, value: str = "demo"):
        self.value = value


def test_register_and_resolve_instance():
    container = DependencyContainer()
    service = DemoService()
    container.register_instance("demo.service", service)
    assert container.resolve("demo.service") is service


def test_register_and_resolve_singleton():
    container = DependencyContainer()
    container.register_singleton(DemoService, lambda: DemoService("singleton"))

    first = container.resolve(DemoService)
    second = container.resolve(DemoService)

    assert first is second
    assert first.value == "singleton"


def test_register_and_resolve_factory():
    container = DependencyContainer()
    container.register_factory("factory.service", lambda: DemoService("factory"))

    first = container.resolve("factory.service")
    second = container.resolve("factory.service")

    assert first is not second
    assert first.value == "factory"


def test_missing_dependency_raises():
    container = DependencyContainer()
    with pytest.raises(DependencyNotFound):
        container.resolve("missing")


def test_unregister_dependency():
    container = DependencyContainer()
    container.register_instance("demo", DemoService())
    container.unregister("demo")
    assert not container.exists("demo")
