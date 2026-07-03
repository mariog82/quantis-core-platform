from dataclasses import dataclass

from framework.persistence import InMemoryRepository, RepositoryQuery


@dataclass
class DemoEntity:
    id: str
    name: str
    status: str = "active"


def test_in_memory_repository_save_get_delete():
    repo = InMemoryRepository[DemoEntity, str]()
    entity = DemoEntity(id="1", name="Demo")

    repo.save(entity)

    assert repo.get("1") == entity
    assert repo.delete("1") is True
    assert repo.get("1") is None


def test_in_memory_repository_list_with_filters():
    repo = InMemoryRepository[DemoEntity, str]()
    repo.save(DemoEntity(id="1", name="A", status="active"))
    repo.save(DemoEntity(id="2", name="B", status="disabled"))

    result = repo.list(RepositoryQuery(filters={"status": "active"}))

    assert len(result) == 1
    assert result[0].name == "A"


def test_in_memory_repository_limit_offset():
    repo = InMemoryRepository[DemoEntity, str]()
    repo.save(DemoEntity(id="1", name="A"))
    repo.save(DemoEntity(id="2", name="B"))
    repo.save(DemoEntity(id="3", name="C"))

    result = repo.list(RepositoryQuery(limit=1, offset=1))

    assert len(result) == 1
    assert result[0].name == "B"
