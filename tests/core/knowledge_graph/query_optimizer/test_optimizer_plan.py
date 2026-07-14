from core.knowledge_graph import (
    And,
    Equals,
    GraphQuery,
    GraphQueryOptimizer,
    Regex,
)


def test_optimizer_returns_optimized_plan():
    optimizer = GraphQueryOptimizer()
    plan = optimizer.plan(
        GraphQuery(
            node_type="document",
            predicate=And(
                (
                    Regex("properties.title", "AI"),
                    Equals("properties.status", "approved"),
                )
            ),
        )
    )

    assert plan.uses_type_filter is True
    assert plan.ordered_predicates == ("Equals", "Regex")
