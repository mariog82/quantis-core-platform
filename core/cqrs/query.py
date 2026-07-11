from dataclasses import dataclass, field
from typing import Any, Generic, Protocol, TypeVar
from uuid import uuid4

from core.cqrs.exceptions import (
    DuplicateHandlerRegistration,
    QueryHandlerNotFound,
)

TQuery = TypeVar("TQuery", bound="Query")
TResult = TypeVar("TResult")


@dataclass(frozen=True)
class Query:
    criteria: dict[str, Any]
    query_id: str = field(default_factory=lambda: str(uuid4()))
    tenant_id: str | None = None


class QueryHandler(Protocol, Generic[TQuery, TResult]):
    def handle(self, query: TQuery) -> TResult:
        ...


class QueryBus(Protocol):
    def register(self, query_type: type[Query], handler: QueryHandler) -> None:
        ...

    def ask(self, query: Query) -> Any:
        ...


class InMemoryQueryBus:
    def __init__(self) -> None:
        self._handlers: dict[type[Query], QueryHandler] = {}
        self._middleware: list[Any] = []

    def register(self, query_type: type[Query], handler: QueryHandler) -> None:
        if query_type in self._handlers:
            raise DuplicateHandlerRegistration(query_type.__name__)
        self._handlers[query_type] = handler

    def use(self, middleware: Any) -> None:
        self._middleware.append(middleware)

    def ask(self, query: Query) -> Any:
        handler = self._handlers.get(type(query))
        if handler is None:
            raise QueryHandlerNotFound(type(query).__name__)

        def invoke(current: Query) -> Any:
            return handler.handle(current)

        chain = invoke

        for middleware in reversed(self._middleware):
            previous = chain

            def make_chain(mw, nxt):
                def wrapped(current: Query):
                    return mw(current, nxt)
                return wrapped

            chain = make_chain(middleware, previous)

        return chain(query)
