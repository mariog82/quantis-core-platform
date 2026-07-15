from typing import Protocol
from core.knowledge_graph.entities import Entity
from core.knowledge_graph.identifiers import NodeId

class EntityRepository(Protocol):
    def save(self, entity: Entity) -> Entity: ...
    def get(self, entity_id: NodeId) -> Entity | None: ...
    def delete(self, entity_id: NodeId) -> Entity: ...
    def list_all(self) -> list[Entity]: ...

class InMemoryEntityRepository:
    def __init__(self) -> None:
        self._entities: dict[NodeId, Entity] = {}

    def save(self, entity: Entity) -> Entity:
        self._entities[entity.entity_id] = entity
        return entity

    def get(self, entity_id: NodeId) -> Entity | None:
        return self._entities.get(entity_id)

    def delete(self, entity_id: NodeId) -> Entity:
        try:
            return self._entities.pop(entity_id)
        except KeyError as exc:
            raise KeyError(entity_id.value) from exc

    def list_all(self) -> list[Entity]:
        return list(self._entities.values())
