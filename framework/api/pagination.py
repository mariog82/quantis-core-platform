from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Pagination:
    page: int = 1
    size: int = 20
    total: int | None = None

    @property
    def offset(self) -> int:
        return max(self.page - 1, 0) * self.size


@dataclass
class Page(Generic[T]):
    items: list[T]
    pagination: Pagination
    metadata: dict = field(default_factory=dict)
