from dataclasses import dataclass, field
from typing import Any
from core.knowledge_graph.identifiers import NodeId
from core.knowledge_graph.models import GraphMetadata, GraphNode, GraphVersion

@dataclass(frozen=True)
class Entity:
    entity_type: str
    attributes: dict[str, Any]
    entity_id: NodeId = field(default_factory=NodeId.generate)
    aliases: tuple[str, ...] = ()
    metadata: GraphMetadata = field(default_factory=GraphMetadata)
    version: GraphVersion = field(default_factory=GraphVersion)

    def __post_init__(self) -> None:
        if not self.entity_type.strip():
            raise ValueError("entity_type must not be empty")

    def to_graph_node(self) -> GraphNode:
        properties = dict(self.attributes)
        if self.aliases:
            properties["aliases"] = list(self.aliases)
        return GraphNode(
            node_id=self.entity_id,
            node_type=self.entity_type,
            properties=properties,
            metadata=self.metadata,
            version=self.version,
        )
