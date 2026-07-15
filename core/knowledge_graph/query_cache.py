from dataclasses import dataclass
from hashlib import sha256
import json

from core.knowledge_graph.query_models import GraphQuery, GraphResult


@dataclass(frozen=True)
class QueryCacheEntry:
    key: str
    result: GraphResult


class QueryResultCache:
    def __init__(self) -> None:
        self._entries: dict[str, GraphResult] = {}

    def key_for(self, query: GraphQuery) -> str:
        sort_specs = getattr(query, "sort", ())

        payload = json.dumps(
            {
                "node_type": getattr(query, "node_type", None),
                "projection": getattr(query, "projection", ()),
                "sort": [
                    (
                        item.field,
                        getattr(
                            item.direction,
                            "value",
                            str(item.direction),
                        ),
                    )
                    for item in sort_specs
                ],
                "limit": getattr(query, "limit", None),
                "offset": getattr(query, "offset", 0),
                "predicate": repr(
                    getattr(query, "predicate", None)
                ),
            },
            sort_keys=True,
            default=str,
        )

        return sha256(payload.encode("utf-8")).hexdigest()

    def get(
        self,
        query: GraphQuery,
    ) -> GraphResult | None:
        return self._entries.get(self.key_for(query))

    def put(
        self,
        query: GraphQuery,
        result: GraphResult,
    ) -> QueryCacheEntry:
        key = self.key_for(query)
        self._entries[key] = result

        return QueryCacheEntry(
            key=key,
            result=result,
        )

    def clear(self) -> None:
        self._entries.clear()


__all__ = [
    "QueryCacheEntry",
    "QueryResultCache",
]
