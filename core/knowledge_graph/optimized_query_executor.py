from core.knowledge_graph.graph import KnowledgeGraph
from core.knowledge_graph.query_cache import QueryResultCache
from core.knowledge_graph.query_executor import GraphQueryExecutor
from core.knowledge_graph.query_metrics import GraphQueryMetrics
from core.knowledge_graph.query_models import GraphQuery, GraphResult
from core.knowledge_graph.query_optimizer import GraphQueryOptimizer


class OptimizedGraphQueryExecutor:
    def __init__(
        self,
        executor: GraphQueryExecutor | None = None,
        optimizer: GraphQueryOptimizer | None = None,
        cache: QueryResultCache | None = None,
        metrics: GraphQueryMetrics | None = None,
    ) -> None:
        self.metrics = metrics or GraphQueryMetrics()
        self.executor = executor or GraphQueryExecutor(self.metrics)
        self.optimizer = optimizer or GraphQueryOptimizer()
        self.cache = cache or QueryResultCache()

    def execute(
        self,
        graph: KnowledgeGraph,
        query: GraphQuery,
        *,
        use_cache: bool = True,
    ) -> GraphResult:
        optimization = self.optimizer.optimize(query)
        optimized = optimization.optimized

        if use_cache:
            cached = self.cache.get(optimized)

            if cached is not None:
                self.metrics.cache_hits += 1
                return cached

            self.metrics.cache_misses += 1

        result = self.executor.execute(graph, optimized)

        if use_cache:
            self.cache.put(optimized, result)

        return result


__all__ = ["OptimizedGraphQueryExecutor"]
