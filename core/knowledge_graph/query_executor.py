from time import perf_counter
from typing import Any

from core.knowledge_graph import query_engine as legacy
from core.knowledge_graph.graph import KnowledgeGraph
from core.knowledge_graph.query_metrics import GraphQueryMetrics
from core.knowledge_graph.query_models import GraphQuery, GraphResult


def _resolve(item: dict[str, Any], field: str) -> Any:
    current: Any = item

    for part in field.split("."):
        if not isinstance(current, dict):
            return None
        current = current.get(part)

    return current


def _node_item(node: Any) -> dict[str, Any]:
    return {
        "node_id": node.node_id.value,
        "node_type": node.node_type,
        "properties": dict(node.properties),
    }


if hasattr(legacy, "GraphQueryExecutor"):
    GraphQueryExecutor = legacy.GraphQueryExecutor

elif hasattr(legacy, "GraphQueryEngine"):

    class GraphQueryExecutor(legacy.GraphQueryEngine):
        pass

else:

    class GraphQueryExecutor:
        def __init__(
            self,
            metrics: GraphQueryMetrics | None = None,
        ) -> None:
            self.metrics = metrics or GraphQueryMetrics()

        def execute(
            self,
            graph: KnowledgeGraph,
            query: GraphQuery,
        ) -> GraphResult:
            started = perf_counter()
            self.metrics.executions += 1

            try:
                items = [
                    _node_item(node)
                    for node in graph.nodes()
                ]
                self.metrics.nodes_scanned += len(items)

                node_type = getattr(query, "node_type", None)
                if node_type is not None:
                    items = [
                        item
                        for item in items
                        if item["node_type"] == node_type
                    ]

                predicate = getattr(query, "predicate", None)
                if predicate is not None:
                    items = [
                        item
                        for item in items
                        if predicate.evaluate(item)
                    ]

                sort_specs = getattr(query, "sort", ())
                for sort_spec in reversed(sort_specs):
                    direction = getattr(
                        sort_spec.direction,
                        "value",
                        str(sort_spec.direction),
                    )
                    reverse = direction in {
                        "descending",
                        "desc",
                    }

                    items.sort(
                        key=lambda item: (
                            _resolve(item, sort_spec.field) is None,
                            _resolve(item, sort_spec.field),
                        ),
                        reverse=reverse,
                    )

                total_count = len(items)
                offset = getattr(query, "offset", 0)
                limit = getattr(query, "limit", None)
                end = None if limit is None else offset + limit
                page_items = items[offset:end]

                projection = getattr(query, "projection", ())
                if projection:
                    page_items = [
                        {
                            field: _resolve(item, field)
                            for field in projection
                        }
                        for item in page_items
                    ]

                try:
                    return GraphResult(
                        items=tuple(page_items),
                        total_count=total_count,
                        offset=offset,
                        limit=limit,
                    )
                except TypeError:
                    return GraphResult(
                        tuple(page_items),
                        total_count,
                    )

            except Exception:
                self.metrics.failures += 1
                raise

            finally:
                self.metrics.execution_time_seconds += (
                    perf_counter() - started
                )


__all__ = ["GraphQueryExecutor"]
