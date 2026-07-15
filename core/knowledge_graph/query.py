from dataclasses import dataclass
from enum import Enum
from typing import Any, Protocol

class SortDirection(str, Enum):
    ASCENDING = "ascending"
    DESCENDING = "descending"

@dataclass(frozen=True)
class SortSpec:
    field: str
    direction: SortDirection = SortDirection.ASCENDING

class Predicate(Protocol):
    def evaluate(self, values: dict[str, Any]) -> bool: ...

@dataclass(frozen=True)
class GraphQuery:
    predicate: Predicate | None = None
    node_type: str | None = None
    projection: tuple[str, ...] = ()
    sort: tuple[SortSpec, ...] = ()
    limit: int | None = None
    offset: int = 0

    def __post_init__(self) -> None:
        if self.limit is not None and self.limit < 0:
            raise ValueError("limit must be >= 0")
        if self.offset < 0:
            raise ValueError("offset must be >= 0")

@dataclass(frozen=True)
class GraphResult:
    items: tuple[dict[str, Any], ...]
    total_count: int
    offset: int
    limit: int | None
