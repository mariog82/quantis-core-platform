from time import perf_counter
from typing import Any
from core.knowledge_graph.graph import KnowledgeGraph
from core.knowledge_graph.query import GraphQuery, GraphResult, SortDirection

class GraphQueryPlanner:
    def estimate_cost(self, query: GraphQuery) -> float:
        cost = 1.0
        if query.node_type is not None:
            cost *= 0.5
        if query.predicate is not None:
            cost += 1.0
        return cost + query.offset * 0.01

class GraphQueryMetrics:
    def __init__(self) -> None:
        self.executions = 0
        self.failures = 0
        self.nodes_scanned = 0
        self.execution_time_seconds = 0.0

class GraphQueryExecutor:
    def __init__(self, metrics: GraphQueryMetrics | None = None) -> None:
        self.metrics = metrics or GraphQueryMetrics()

    def execute(self, graph: KnowledgeGraph, query: GraphQuery) -> GraphResult:
        started = perf_counter() 
        self.metrics.executions += 1
        try:
            items = [{"node_id": n.node_id.value, "node_type": n.node_type, "properties": dict(n.properties)} for n in graph.nodes()]
            self.metrics.nodes_scanned += len(items)
            if query.node_type is not None:
                items = [i for i in items if i["node_type"] == query.node_type]
            if query.predicate is not None:
                items = [i for i in items if query.predicate.evaluate(i)]
            for spec in reversed(query.sort):
                def key(item: dict[str, Any]):
                    current: Any = item
                    for part in spec.field.split("."):
                        current = current.get(part) if isinstance(current, dict) else None
                    return (current is None, current)
                items.sort(key=key, reverse=spec.direction == SortDirection.DESCENDING)
            total = len(items)
            start=query.offset
            end=None if query.limit is None else start+query.limit
            page = items[start:end]
            if query.projection:
                projected=[]
                for item in page:
                    row={}
                    for field in query.projection:
                        current: Any=item
                        for part in field.split("."):
                            current=current.get(part) if isinstance(current,dict) else None
                        row[field]=current
                    projected.append(row)
                page=projected
            return GraphResult(tuple(page), total, query.offset, query.limit)
        except Exception:
            self.metrics.failures += 1
            raise
        finally:
            self.metrics.execution_time_seconds += perf_counter()-started
