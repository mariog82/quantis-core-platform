from dataclasses import dataclass

from core.cqrs import InMemoryQueryBus, Query


@dataclass(frozen=True)
class GetTenant(Query):
    pass


class GetTenantHandler:
    def handle(self, query: GetTenant) -> dict[str, str]:
        return {"tenant_id": query.criteria["tenant_id"]}


def test_query_bus_returns_result():
    bus = InMemoryQueryBus()
    bus.register(GetTenant, GetTenantHandler())

    result = bus.ask(GetTenant({"tenant_id": "t1"}))

    assert result == {"tenant_id": "t1"}
