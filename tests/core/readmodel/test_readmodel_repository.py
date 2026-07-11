from core.readmodel import InMemoryReadModelRepository


def test_readmodel_repository_saves_gets_and_searches():
    repository = InMemoryReadModelRepository()
    repository.save(
        "tenant",
        "t1",
        {"tenant_id": "t1", "plan": "enterprise"},
    )
    repository.save(
        "tenant",
        "t2",
        {"tenant_id": "t2", "plan": "base"},
    )

    assert repository.get("tenant", "t1")["plan"] == "enterprise"
    assert repository.search(
        "tenant",
        {"plan": "enterprise"},
    ) == [{"tenant_id": "t1", "plan": "enterprise"}]
