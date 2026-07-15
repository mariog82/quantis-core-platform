from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from core.knowledge_graph.identifiers import EdgeId, NodeId
from core.knowledge_graph.models import GraphEdge, GraphMetadata, GraphVersion


class RelationshipDirection(str, Enum):
    DIRECTED = "directed"
    UNDIRECTED = "undirected"
    BIDIRECTIONAL = "bidirectional"


class RelationshipCardinality(str, Enum):
    ONE_TO_ONE = "one_to_one"
    ONE_TO_MANY = "one_to_many"
    MANY_TO_ONE = "many_to_one"
    MANY_TO_MANY = "many_to_many"


@dataclass(frozen=True)
class RelationshipType:
    name: str
    inverse_name: str | None = None
    direction: RelationshipDirection = RelationshipDirection.DIRECTED
    cardinality: RelationshipCardinality = RelationshipCardinality.MANY_TO_MANY
    semantic_labels: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Relationship type name must not be empty")


@dataclass(frozen=True)
class Relationship:
    source_id: NodeId
    target_id: NodeId
    relationship_type: RelationshipType
    properties: dict[str, Any] = field(default_factory=dict)
    relationship_id: EdgeId = field(default_factory=EdgeId.generate)
    weight: float = 1.0
    metadata: GraphMetadata = field(default_factory=GraphMetadata)
    version: GraphVersion = field(default_factory=GraphVersion)

    def __post_init__(self) -> None:
        if self.weight < 0:
            raise ValueError("Relationship weight must be >= 0")

    @property
    def directed(self) -> bool:
        return self.relationship_type.direction != RelationshipDirection.UNDIRECTED

    def to_graph_edge(self) -> GraphEdge:
        properties = dict(self.properties)
        properties["direction"] = self.relationship_type.direction.value
        properties["cardinality"] = self.relationship_type.cardinality.value
        properties["semantic_labels"] = list(
            self.relationship_type.semantic_labels
        )
        if self.relationship_type.inverse_name:
            properties["inverse_name"] = self.relationship_type.inverse_name

        return GraphEdge(
            edge_id=self.relationship_id,
            source_id=self.source_id,
            target_id=self.target_id,
            relation_type=self.relationship_type.name,
            properties=properties,
            directed=self.directed,
            weight=self.weight,
            metadata=self.metadata,
            version=self.version,
        )
