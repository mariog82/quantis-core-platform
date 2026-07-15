from core.knowledge_graph import EntityFactory

def test_entity_converts_to_graph_node():
    entity = EntityFactory.create("person", {"name": "Mario"}, aliases=("Founder",))
    node = entity.to_graph_node()
    assert node.node_id == entity.entity_id
    assert node.node_type == "person"
    assert node.properties["aliases"] == ["Founder"]
