from collections import deque

from core.knowledge_graph.identifiers import EdgeId, NodeId
from core.knowledge_graph.relationship_index import RelationshipIndex
from core.knowledge_graph.relationship_repository import (
    RelationshipRepository,
)
from core.knowledge_graph.relationships import Relationship


class RelationshipEngine:
    def __init__(
        self,
        repository: RelationshipRepository,
        *,
        index: RelationshipIndex | None = None,
    ) -> None:
        self.repository = repository
        self.index = index or RelationshipIndex()

    def register(self, relationship: Relationship) -> Relationship:
        if relationship.source_id == relationship.target_id:
            raise ValueError("SELF_RELATIONSHIP")

        if self.repository.get(relationship.relationship_id) is not None:
            raise ValueError(
                "Relationship already registered: "
                f"{relationship.relationship_id.value}"
            )

        saved = self.repository.save(relationship)
        self.index.add(saved)
        return saved

    def get(self, relationship_id: EdgeId) -> Relationship:
        relationship = self.repository.get(relationship_id)
        if relationship is None:
            raise KeyError(relationship_id.value)
        return relationship

    def unregister(self, relationship_id: EdgeId) -> Relationship:
        relationship = self.get(relationship_id)
        deleted = self.repository.delete(relationship_id)
        self.index.remove(relationship)
        return deleted

    def outgoing(self, node_id: NodeId) -> list[Relationship]:
        return [
            self.get(relationship_id)
            for relationship_id in sorted(
                self.index.outgoing(node_id),
                key=lambda current: current.value,
            )
        ]

    def incoming(self, node_id: NodeId) -> list[Relationship]:
        return [
            self.get(relationship_id)
            for relationship_id in sorted(
                self.index.incoming(node_id),
                key=lambda current: current.value,
            )
        ]

    def related(self, node_id: NodeId) -> set[NodeId]:
        result: set[NodeId] = set()

        for relationship in self.repository.list_for_node(node_id):
            if relationship.source_id == node_id:
                result.add(relationship.target_id)
            if relationship.target_id == node_id:
                result.add(relationship.source_id)

        return result

    def shortest_path(
        self,
        source_id: NodeId,
        target_id: NodeId,
    ) -> list[NodeId]:
        queue: deque[tuple[NodeId, list[NodeId]]] = deque(
            [(source_id, [source_id])]
        )
        visited = {source_id}

        while queue:
            current, path = queue.popleft()
            if current == target_id:
                return path

            for neighbor in sorted(
                self.related(current),
                key=lambda node_id: node_id.value,
            ):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return []
