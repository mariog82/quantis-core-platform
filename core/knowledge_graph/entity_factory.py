from typing import Any
from core.knowledge_graph.entities import Entity
from core.knowledge_graph.models import GraphMetadata

class EntityFactory:
    @staticmethod
    def create(
        entity_type: str,
        attributes: dict[str, Any],
        *,
        aliases: tuple[str, ...] = (),
        metadata: GraphMetadata | None = None,
    ) -> Entity:
        return Entity(
            entity_type=entity_type,
            attributes=dict(attributes),
            aliases=tuple(aliases),
            metadata=metadata or GraphMetadata(),
        )
