from core.knowledge_graph import (
    GraphAnalyticsService,
    GraphEdge,
    GraphNode,
    KnowledgeGraph,
)


def build_graph():
    graph = KnowledgeGraph()
    first = graph.add_node(GraphNode("person", {"name": "A"}))
    second = graph.add_node(GraphNode("organization", {"name": "B"}))
    isolated = graph.add_node(GraphNode("person", {"name": "C"}))
    graph.add_edge(
        GraphEdge(
            first.node_id,
            second.node_id,
            "member_of",
        )
    )
    return graph, first, second, isolated


def test_graph_summary():
    graph, _, _, isolated = build_graph()
    summary = GraphAnalyticsService().summarize(graph)

    assert summary.node_count == 3
    assert summary.edge_count == 1
    assert summary.isolated_nodes == (isolated.node_id,)
    assert summary.density > 0


def test_graph_distributions_and_node_analytics():
    graph, first, second, _ = build_graph()
    report = GraphAnalyticsService().report(graph)

    node_types = {
        bucket.key: bucket.count
        for bucket in report.node_types
    }
    relationship_types = {
        bucket.key: bucket.count
        for bucket in report.relationship_types
    }
    analytics = {
        item.node_id: item
        for item in report.node_analytics
    }

    assert node_types == {
        "organization": 1,
        "person": 2,
    }
    assert relationship_types == {"member_of": 1}
    assert analytics[first.node_id].outbound_degree == 1
    assert analytics[second.node_id].inbound_degree == 1
    assert report.metadata["execution_time_seconds"] >= 0
