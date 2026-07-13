from core.knowledge_graph import (
    EntityFactory,
    InMemoryRelationshipRepository,
    Relationship,
    RelationshipEngine,
    RelationshipType,
)


def test_relationship_engine_registers_and_indexes_relationships():
    source = EntityFactory.create("person", {"name": "Mario"})
    target = EntityFactory.create("organization", {"name": "Quantis"})
    relationship = Relationship(
        source_id=source.entity_id,
        target_id=target.entity_id,
        relationship_type=RelationshipType(
            name="founded",
            inverse_name="founded_by",
        ),
        weight=0.95,
    )
    engine = RelationshipEngine(InMemoryRelationshipRepository())

    registered = engine.register(relationship)

    assert engine.get(relationship.relationship_id) == registered
    assert engine.outgoing(source.entity_id) == [relationship]
    assert engine.incoming(target.entity_id) == [relationship]
    assert engine.related(source.entity_id) == {target.entity_id}
