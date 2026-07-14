from core.knowledge_graph import GraphQuery, GraphQueryOptimizer


def test_optimizer_caps_excessive_limit():
    result = GraphQueryOptimizer().optimize(
        GraphQuery(limit=5000)
    )

    assert result.optimized.limit == 1000
    assert "normalize-pagination" in result.applied_rules
