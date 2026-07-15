from core.knowledge_graph import EntityFactory, EntityIndex

def test_entity_index_is_case_insensitive_for_aliases():
    index = EntityIndex()
    entity = EntityFactory.create("document", {"title": "Delibera"}, aliases=("Verbale",))
    index.add(entity)
    assert index.by_alias("verbale") == {entity.entity_id}
    assert index.by_alias("VERBALE") == {entity.entity_id}
