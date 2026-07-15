import pytest
from core.knowledge_graph import EntityFactory, EntityRegistry, InMemoryEntityRepository

def test_entity_registry_registers_and_indexes_entities():
    registry = EntityRegistry(InMemoryEntityRepository())
    entity = EntityFactory.create("organization", {"name": "Quantis"}, aliases=("Quantis Core", "QCP"))
    assert registry.register(entity) == entity
    assert registry.find_by_type("organization") == [entity]
    assert registry.find_by_alias("qcp") == [entity]

def test_entity_registry_rejects_empty_attributes():
    registry = EntityRegistry(InMemoryEntityRepository())
    with pytest.raises(ValueError, match="EMPTY_ENTITY_ATTRIBUTES"):
        registry.register(EntityFactory.create("person", {}))
