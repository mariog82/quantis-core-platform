from core.knowledge_graph import (
    EntityFactory,
    Relationship,
    RelationshipCardinality,
    RelationshipDirection,
    RelationshipType,
)


def test_relationship_converts_to_graph_edge():
    source = EntityFactory.create("student", {"name": "A"})
    target = EntityFactory.create("class", {"name": "3A"})
    relationship = Relationship(
        source_id=source.entity_id,
        target_id=target.entity_id,
        relationship_type=RelationshipType(
            name="attends",
            direction=RelationshipDirection.DIRECTED,
            cardinality=RelationshipCardinality.MANY_TO_ONE,
            semantic_labels=("school", "membership"),
        ),
    )

    edge = relationship.to_graph_edge()

    assert edge.relation_type == "attends"
    assert edge.properties["cardinality"] == "many_to_one"
    assert edge.properties["semantic_labels"] == [
        "school",
        "membership",
    ]
