import pytest

from core.knowledge_graph import (
    GraphAlgorithmMetrics,
    GraphAlgorithmsService,
    GraphContainsCycle,
    GraphEdge,
    GraphNode,
    KnowledgeGraph,
)


def build_graph():
    graph = KnowledgeGraph()

    first = graph.add_node(
        GraphNode(
            "node",
            {"name": "A"},
        )
    )
    second = graph.add_node(
        GraphNode(
            "node",
            {"name": "B"},
        )
    )
    third = graph.add_node(
        GraphNode(
            "node",
            {"name": "C"},
        )
    )

    graph.add_edge(
        GraphEdge(
            first.node_id,
            second.node_id,
            "next",
            weight=1.0,
        )
    )
    graph.add_edge(
        GraphEdge(
            second.node_id,
            third.node_id,
            "next",
            weight=2.0,
        )
    )

    return graph, first, second, third


def test_traversal_and_paths():
    graph, first, second, third = build_graph()
    service = GraphAlgorithmsService()

    assert service.breadth_first(
        graph,
        first.node_id,
    ) == (
        first.node_id,
        second.node_id,
        third.node_id,
    )

    assert service.depth_first(
        graph,
        first.node_id,
    ) == (
        first.node_id,
        second.node_id,
        third.node_id,
    )

    assert service.shortest_path(
        graph,
        first.node_id,
        third.node_id,
    ).nodes == (
        first.node_id,
        second.node_id,
        third.node_id,
    )

    weighted = service.dijkstra(
        graph,
        first.node_id,
        third.node_id,
    )

    assert weighted.nodes == (
        first.node_id,
        second.node_id,
        third.node_id,
    )
    assert weighted.total_weight == 3.0


def test_components_centrality_and_metrics():
    graph, _, second, _ = build_graph()

    graph.add_node(
        GraphNode(
            "node",
            {"name": "D"},
        )
    )

    metrics = GraphAlgorithmMetrics()
    service = GraphAlgorithmsService(metrics)

    components = service.connected_components(graph)
    degree = service.degree_centrality(graph)
    closeness = service.closeness_centrality(graph)

    assert len(components.components) == 2
    assert degree.values[second.node_id] >= 2 / 3
    assert closeness.values[second.node_id] > 0
    assert metrics.executions >= 3
    assert metrics.failures == 0


def test_cycle_and_topological_sort():
    graph, first, _, third = build_graph()
    service = GraphAlgorithmsService()

    assert service.has_cycle(graph) is False

    assert set(service.topological_sort(graph)) == {
        node.node_id
        for node in graph.nodes()
    }

    graph.add_edge(
        GraphEdge(
            third.node_id,
            first.node_id,
            "next",
        )
    )

    assert service.has_cycle(graph) is True

    with pytest.raises(GraphContainsCycle):
        service.topological_sort(graph)
