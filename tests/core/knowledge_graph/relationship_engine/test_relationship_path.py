from core.knowledge_graph import (
    EntityFactory,
    InMemoryRelationshipRepository,
    Relationship,
    RelationshipEngine,
    RelationshipType,
)


def test_relationship_engine_finds_shortest_path():
    first = EntityFactory.create("person", {"name": "A"})
    second = EntityFactory.create("organization", {"name": "B"})
    third = EntityFactory.create("document", {"name": "C"})
    relationship_type = RelationshipType("related_to")
    engine = RelationshipEngine(InMemoryRelationshipRepository())

    engine.register(
        Relationship(
            source_id=first.entity_id,
            target_id=second.entity_id,
            relationship_type=relationship_type,
        )
    )
    engine.register(
        Relationship(
            source_id=second.entity_id,
            target_id=third.entity_id,
            relationship_type=relationship_type,
        )
    )

    assert engine.shortest_path(first.entity_id, third.entity_id) == [
        first.entity_id,
        second.entity_id,
        third.entity_id,
    ]
