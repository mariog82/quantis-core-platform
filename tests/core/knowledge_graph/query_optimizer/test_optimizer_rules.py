from core.knowledge_graph import (
    And,
    Equals,
    GraphQuery,
    GraphQueryOptimizer,
    Regex,
)


def test_optimizer_removes_duplicates_and_reorders_predicates():
    duplicate = Equals("properties.status", "approved")
    query = GraphQuery(
        predicate=And(
            (
                Regex("properties.title", "AI"),
                duplicate,
                duplicate,
            )
        )
    )

    result = GraphQueryOptimizer().optimize(query)

    assert result.applied_rules == (
        "remove-duplicate-predicates",
        "reorder-and-predicates",
    )
    assert isinstance(result.optimized.predicate, And)
    assert len(result.optimized.predicate.predicates) == 2
    assert type(result.optimized.predicate.predicates[0]).__name__ == "Equals"
