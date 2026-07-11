import pytest

from core.cqrs import Command, InMemoryCommandBus, ValidationMiddleware


class Handler:
    def handle(self, command: Command) -> bool:
        return True


def test_validation_middleware_rejects_invalid_command():
    bus = InMemoryCommandBus()
    bus.register(Command, Handler())
    bus.use(ValidationMiddleware(lambda command: "required" in command.payload))

    with pytest.raises(ValueError):
        bus.execute(Command({}))
