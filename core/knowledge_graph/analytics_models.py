from dataclasses import dataclass
from typing import Any

from core.knowledge_graph.identifiers import NodeId


@dataclass(frozen=True)
class GraphSummary:
    node_count: int
    edge_count: int
    density: float
    isolated_nodes: tuple[NodeId, ...]


@dataclass(frozen=True)
class NodeAnalytics:
    node_id: NodeId
    degree: int
    inbound_degree: int
    outbound_degree: int
    neighbor_count: int


@dataclass(frozen=True)
class DistributionBucket:
    key: str
    count: int


@dataclass(frozen=True)
class GraphAnalyticsReport:
    summary: GraphSummary
    node_types: tuple[DistributionBucket, ...]
    relationship_types: tuple[DistributionBucket, ...]
    node_analytics: tuple[NodeAnalytics, ...]
    metadata: dict[str, Any]
