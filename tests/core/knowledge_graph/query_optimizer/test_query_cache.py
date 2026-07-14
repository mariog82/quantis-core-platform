from core.knowledge_graph import (
    GraphNode,
    GraphQuery,
    KnowledgeGraph,
    OptimizedGraphQueryExecutor,
)


def test_optimized_executor_uses_cache():
    graph = KnowledgeGraph()
    graph.add_node(GraphNode("document", {"title": "A"}))
    executor = OptimizedGraphQueryExecutor()
    query = GraphQuery(node_type="document")

    first = executor.execute(graph, query)
    second = executor.execute(graph, query)

    assert first == second
    assert executor.metrics.cache_misses == 1
    assert executor.metrics.cache_hits == 1
