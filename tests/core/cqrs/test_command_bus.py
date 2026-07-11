from dataclasses import dataclass

import pytest

from core.cqrs import (
    Command,
    CommandHandlerNotFound,
    InMemoryCommandBus,
    LoggingMiddleware,
)


@dataclass(frozen=True)
class CreateTenant(Command):
    pass


class CreateTenantHandler:
    def handle(self, command: CreateTenant) -> str:
        return command.payload["tenant_id"]


def test_command_bus_executes_handler_and_middleware():
    bus = InMemoryCommandBus()
    logger = LoggingMiddleware()
    bus.use(logger)
    bus.register(CreateTenant, CreateTenantHandler())

    command = CreateTenant({"tenant_id": "t1"})

    assert bus.execute(command) == "t1"
    assert logger.calls == [command.command_id]


def test_command_bus_raises_for_missing_handler():
    with pytest.raises(CommandHandlerNotFound):
        InMemoryCommandBus().execute(Command({}))
