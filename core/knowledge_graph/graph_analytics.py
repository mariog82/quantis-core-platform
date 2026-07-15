from collections import Counter
from time import perf_counter
from typing import Any

from core.knowledge_graph.analytics_models import (
    DistributionBucket,
    GraphAnalyticsReport,
    GraphSummary,
    NodeAnalytics,
)
from core.knowledge_graph.identifiers import NodeId


def _nodes(graph: Any) -> tuple[Any, ...]:
    return tuple(graph.nodes())


def _edges(graph: Any) -> tuple[Any, ...]:
    return tuple(graph.edges()) if hasattr(graph, "edges") else ()


def _incoming(graph: Any, node_id: NodeId) -> tuple[Any, ...]:
    if hasattr(graph, "incoming"):
        return tuple(graph.incoming(node_id))
    return tuple(edge for edge in _edges(graph) if edge.target_id == node_id)


def _outgoing(graph: Any, node_id: NodeId) -> tuple[Any, ...]:
    if hasattr(graph, "outgoing"):
        return tuple(graph.outgoing(node_id))
    return tuple(edge for edge in _edges(graph) if edge.source_id == node_id)


class GraphAnalyticsService:
    def summarize(self, graph: Any) -> GraphSummary:
        nodes = _nodes(graph)
        edges = _edges(graph)
        node_count = len(nodes)
        edge_count = len(edges)

        possible_edges = node_count * (node_count - 1)
        density = (
            edge_count / possible_edges
            if possible_edges > 0
            else 0.0
        )

        isolated = tuple(
            node.node_id
            for node in nodes
            if not _incoming(graph, node.node_id)
            and not _outgoing(graph, node.node_id)
        )

        return GraphSummary(
            node_count=node_count,
            edge_count=edge_count,
            density=density,
            isolated_nodes=isolated,
        )

    def node_analytics(
        self,
        graph: Any,
    ) -> tuple[NodeAnalytics, ...]:
        result: list[NodeAnalytics] = []

        for node in _nodes(graph):
            inbound = _incoming(graph, node.node_id)
            outbound = _outgoing(graph, node.node_id)
            neighbors = {
                edge.source_id
                for edge in inbound
                if edge.source_id != node.node_id
            }
            neighbors.update(
                edge.target_id
                for edge in outbound
                if edge.target_id != node.node_id
            )

            result.append(
                NodeAnalytics(
                    node_id=node.node_id,
                    degree=len(inbound) + len(outbound),
                    inbound_degree=len(inbound),
                    outbound_degree=len(outbound),
                    neighbor_count=len(neighbors),
                )
            )

        return tuple(result)

    def node_type_distribution(
        self,
        graph: Any,
    ) -> tuple[DistributionBucket, ...]:
        counts = Counter(node.node_type for node in _nodes(graph))
        return tuple(
            DistributionBucket(key=key, count=count)
            for key, count in sorted(counts.items())
        )

    def relationship_type_distribution(
        self,
        graph: Any,
    ) -> tuple[DistributionBucket, ...]:
        counts = Counter(
            getattr(edge, "relation_type", "unknown")
            for edge in _edges(graph)
        )
        return tuple(
            DistributionBucket(key=key, count=count)
            for key, count in sorted(counts.items())
        )

    def report(self, graph: Any) -> GraphAnalyticsReport:
        started = perf_counter()
        summary = self.summarize(graph)
        node_analytics = self.node_analytics(graph)

        return GraphAnalyticsReport(
            summary=summary,
            node_types=self.node_type_distribution(graph),
            relationship_types=self.relationship_type_distribution(graph),
            node_analytics=node_analytics,
            metadata={
                "execution_time_seconds": perf_counter() - started,
            },
        )
