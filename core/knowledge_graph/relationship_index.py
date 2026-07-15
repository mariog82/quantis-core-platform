from collections import defaultdict

from core.knowledge_graph.identifiers import EdgeId, NodeId
from core.knowledge_graph.relationships import Relationship


class RelationshipIndex:
    def __init__(self) -> None:
        self._by_type: dict[str, set[EdgeId]] = defaultdict(set)
        self._outgoing: dict[NodeId, set[EdgeId]] = defaultdict(set)
        self._incoming: dict[NodeId, set[EdgeId]] = defaultdict(set)

    def add(self, relationship: Relationship) -> None:
        relationship_id = relationship.relationship_id
        self._by_type[relationship.relationship_type.name].add(
            relationship_id
        )
        self._outgoing[relationship.source_id].add(relationship_id)
        self._incoming[relationship.target_id].add(relationship_id)

        if not relationship.directed:
            self._outgoing[relationship.target_id].add(relationship_id)
            self._incoming[relationship.source_id].add(relationship_id)

    def remove(self, relationship: Relationship) -> None:
        relationship_id = relationship.relationship_id
        self._by_type[relationship.relationship_type.name].discard(
            relationship_id
        )
        self._outgoing[relationship.source_id].discard(relationship_id)
        self._incoming[relationship.target_id].discard(relationship_id)
        self._outgoing[relationship.target_id].discard(relationship_id)
        self._incoming[relationship.source_id].discard(relationship_id)

    def by_type(self, relationship_type: str) -> set[EdgeId]:
        return set(self._by_type.get(relationship_type, set()))

    def outgoing(self, node_id: NodeId) -> set[EdgeId]:
        return set(self._outgoing.get(node_id, set()))

    def incoming(self, node_id: NodeId) -> set[EdgeId]:
        return set(self._incoming.get(node_id, set()))
