from dataclasses import dataclass
from enum import Enum

from core.knowledge_graph.query_engine import (
    GraphQuery,
    GraphResult,
)


class QueryDirection(str, Enum):
    ANY = "any"
    OUTGOING = "outgoing"
    INCOMING = "incoming"


class SortDirection(str, Enum):
    ASCENDING = "ascending"
    DESCENDING = "descending"


@dataclass(frozen=True)
class SortSpec:
    field: str
    direction: SortDirection = SortDirection.ASCENDING


@dataclass(frozen=True)
class GraphQueryPlan:
    query: GraphQuery
    estimated_cost: float
    uses_type_filter: bool
    ordered_predicates: tuple[str, ...] = ()


@dataclass(frozen=True)
class GraphCursor:
    offset: int


@dataclass(frozen=True)
class GraphPage:
    result: GraphResult
    next_cursor: GraphCursor | None = None


@dataclass(frozen=True)
class GraphCount:
    value: int


__all__ = [
    "GraphQuery",
    "GraphResult",
    "QueryDirection",
    "SortDirection",
    "SortSpec",
    "GraphQueryPlan",
    "GraphCursor",
    "GraphPage",
    "GraphCount",
]
