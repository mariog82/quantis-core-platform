from dataclasses import dataclass, field
from typing import Any, Callable


class CQRSMiddleware:
    def __call__(
        self,
        message: Any,
        next_handler: Callable[[Any], Any],
    ) -> Any:
        return next_handler(message)


@dataclass
class LoggingMiddleware(CQRSMiddleware):
    calls: list[str] = field(default_factory=list)

    def __call__(
        self,
        message: Any,
        next_handler: Callable[[Any], Any],
    ) -> Any:
        identifier = getattr(
            message,
            "command_id",
            getattr(message, "query_id", "unknown"),
        )
        self.calls.append(identifier)
        return next_handler(message)


class ValidationMiddleware(CQRSMiddleware):
    def __init__(self, validator: Callable[[Any], bool]) -> None:
        self.validator = validator

    def __call__(
        self,
        message: Any,
        next_handler: Callable[[Any], Any],
    ) -> Any:
        if not self.validator(message):
            raise ValueError("CQRS message validation failed")
        return next_handler(message)
