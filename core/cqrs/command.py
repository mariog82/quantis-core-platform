from dataclasses import dataclass, field
from typing import Any, Generic, Protocol, TypeVar
from uuid import uuid4

from core.cqrs.exceptions import (
    CommandHandlerNotFound,
    DuplicateHandlerRegistration,
)

TCommand = TypeVar("TCommand", bound="Command")
TResult = TypeVar("TResult")


@dataclass(frozen=True)
class Command:
    payload: dict[str, Any]
    command_id: str = field(default_factory=lambda: str(uuid4()))
    tenant_id: str | None = None


class CommandHandler(Protocol, Generic[TCommand, TResult]):
    def handle(self, command: TCommand) -> TResult:
        ...


class CommandBus(Protocol):
    def register(self, command_type: type[Command], handler: CommandHandler) -> None:
        ...

    def execute(self, command: Command) -> Any:
        ...


class InMemoryCommandBus:
    def __init__(self) -> None:
        self._handlers: dict[type[Command], CommandHandler] = {}
        self._middleware: list[Any] = []

    def register(self, command_type: type[Command], handler: CommandHandler) -> None:
        if command_type in self._handlers:
            raise DuplicateHandlerRegistration(command_type.__name__)
        self._handlers[command_type] = handler

    def use(self, middleware: Any) -> None:
        self._middleware.append(middleware)

    def execute(self, command: Command) -> Any:
        handler = self._handlers.get(type(command))
        if handler is None:
            raise CommandHandlerNotFound(type(command).__name__)

        def invoke(current: Command) -> Any:
            return handler.handle(current)

        chain = invoke

        for middleware in reversed(self._middleware):
            previous = chain

            def make_chain(mw, nxt):
                def wrapped(current: Command):
                    return mw(current, nxt)
                return wrapped

            chain = make_chain(middleware, previous)

        return chain(command)
