from collections import defaultdict
from core.knowledge_graph.entities import Entity
from core.knowledge_graph.identifiers import NodeId

class EntityIndex:
    def __init__(self) -> None:
        self._by_type: dict[str, set[NodeId]] = defaultdict(set)
        self._by_alias: dict[str, set[NodeId]] = defaultdict(set)

    def add(self, entity: Entity) -> None:
        self._by_type[entity.entity_type].add(entity.entity_id)
        for alias in entity.aliases:
            self._by_alias[alias.strip().lower()].add(entity.entity_id)

    def remove(self, entity: Entity) -> None:
        self._by_type[entity.entity_type].discard(entity.entity_id)
        for alias in entity.aliases:
            self._by_alias[alias.strip().lower()].discard(entity.entity_id)

    def by_type(self, entity_type: str) -> set[NodeId]:
        return set(self._by_type.get(entity_type, set()))

    def by_alias(self, alias: str) -> set[NodeId]:
        return set(self._by_alias.get(alias.strip().lower(), set()))
