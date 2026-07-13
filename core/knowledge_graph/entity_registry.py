from core.knowledge_graph.entities import Entity
from core.knowledge_graph.entity_index import EntityIndex
from core.knowledge_graph.entity_repository import EntityRepository
from core.knowledge_graph.entity_validation import EntityValidator
from core.knowledge_graph.identifiers import NodeId

class EntityRegistry:
    def __init__(
        self,
        repository: EntityRepository,
        *,
        validator: EntityValidator | None = None,
        index: EntityIndex | None = None,
    ) -> None:
        self.repository = repository
        self.validator = validator or EntityValidator()
        self.index = index or EntityIndex()

    def register(self, entity: Entity) -> Entity:
        report = self.validator.validate(entity)
        if not report.passed:
            raise ValueError(", ".join(issue.code for issue in report.issues))
        if self.repository.get(entity.entity_id) is not None:
            raise ValueError(f"Entity already registered: {entity.entity_id.value}")
        saved = self.repository.save(entity)
        self.index.add(saved)
        return saved

    def get(self, entity_id: NodeId) -> Entity:
        entity = self.repository.get(entity_id)
        if entity is None:
            raise KeyError(entity_id.value)
        return entity

    def unregister(self, entity_id: NodeId) -> Entity:
        entity = self.get(entity_id)
        deleted = self.repository.delete(entity_id)
        self.index.remove(entity)
        return deleted

    def find_by_type(self, entity_type: str) -> list[Entity]:
        ids = sorted(self.index.by_type(entity_type), key=lambda item: item.value)
        return [self.get(entity_id) for entity_id in ids]

    def find_by_alias(self, alias: str) -> list[Entity]:
        ids = sorted(self.index.by_alias(alias), key=lambda item: item.value)
        return [self.get(entity_id) for entity_id in ids]
