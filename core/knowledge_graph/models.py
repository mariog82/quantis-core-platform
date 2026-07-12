from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from core.knowledge_graph.identifiers import EdgeId, NodeId

def utc_now() -> datetime:
    return datetime.now(timezone.utc)

@dataclass(frozen=True)
class GraphMetadata:
    tenant_id: str | None = None
    source: str | None = None
    correlation_id: str | None = None
    created_by: str | None = None
    labels: tuple[str, ...] = ()
    attributes: dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

@dataclass(frozen=True)
class GraphVersion:
    value: int = 1

    def next(self) -> "GraphVersion":
        return GraphVersion(self.value + 1)

@dataclass(frozen=True)
class GraphNode:
    node_type: str
    properties: dict[str, Any]
    node_id: NodeId = field(default_factory=NodeId.generate)
    metadata: GraphMetadata = field(default_factory=GraphMetadata)
    version: GraphVersion = field(default_factory=GraphVersion)

    def __post_init__(self) -> None:
        if not self.node_type.strip():
            raise ValueError("node_type must not be empty")

@dataclass(frozen=True)
class GraphEdge:
    source_id: NodeId
    target_id: NodeId
    relation_type: str
    properties: dict[str, Any] = field(default_factory=dict)
    edge_id: EdgeId = field(default_factory=EdgeId.generate)
    directed: bool = True
    weight: float = 1.0
    metadata: GraphMetadata = field(default_factory=GraphMetadata)
    version: GraphVersion = field(default_factory=GraphVersion)

    def __post_init__(self) -> None:
        if not self.relation_type.strip():
            raise ValueError("relation_type must not be empty")
        if self.weight < 0:
            raise ValueError("weight must be >= 0")
