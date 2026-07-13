from typing import Protocol

from core.knowledge_graph.identifiers import EdgeId, NodeId
from core.knowledge_graph.relationships import Relationship


class RelationshipRepository(Protocol):
    def save(self, relationship: Relationship) -> Relationship:
        ...

    def get(self, relationship_id: EdgeId) -> Relationship | None:
        ...

    def delete(self, relationship_id: EdgeId) -> Relationship:
        ...

    def list_all(self) -> list[Relationship]:
        ...

    def list_for_node(self, node_id: NodeId) -> list[Relationship]:
        ...


class InMemoryRelationshipRepository:
    def __init__(self) -> None:
        self._relationships: dict[EdgeId, Relationship] = {}

    def save(self, relationship: Relationship) -> Relationship:
        self._relationships[relationship.relationship_id] = relationship
        return relationship

    def get(self, relationship_id: EdgeId) -> Relationship | None:
        return self._relationships.get(relationship_id)

    def delete(self, relationship_id: EdgeId) -> Relationship:
        try:
            return self._relationships.pop(relationship_id)
        except KeyError as exc:
            raise KeyError(relationship_id.value) from exc

    def list_all(self) -> list[Relationship]:
        return list(self._relationships.values())

    def list_for_node(self, node_id: NodeId) -> list[Relationship]:
        return [
            relationship
            for relationship in self._relationships.values()
            if relationship.source_id == node_id
            or relationship.target_id == node_id
        ]
