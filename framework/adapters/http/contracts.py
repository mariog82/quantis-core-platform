from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class HttpMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


class HttpStatus(int, Enum):
    OK = 200
    CREATED = 201
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500


@dataclass(frozen=True)
class HttpHeader:
    name: str
    value: str


@dataclass
class HttpRequest:
    method: HttpMethod
    url: str
    headers: list[HttpHeader] = field(default_factory=list)
    body: Any = None


@dataclass
class HttpResponse:
    status: HttpStatus | int
    body: Any = None
    headers: list[HttpHeader] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return 200 <= int(self.status) < 300
