from typing import Protocol

from framework.api.context import RequestContext


class Middleware(Protocol):
    def handle(self, context: RequestContext) -> RequestContext:
        ...


class MiddlewarePipeline:
    def __init__(self):
        self._items: list[Middleware] = []

    def add(self, middleware: Middleware) -> None:
        self._items.append(middleware)

    def execute(self, context: RequestContext) -> RequestContext:
        current = context
        for middleware in self._items:
            current = middleware.handle(current)
        return current
