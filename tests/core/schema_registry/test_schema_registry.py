from core.schema_registry import EventSchema, InMemoryEventSchemaRegistry


def test_schema_registry_registers_and_validates():
    registry = InMemoryEventSchemaRegistry()
    registry.register(
        EventSchema(
            event_type="tenant.created",
            version=1,
            required_fields=("tenant_id",),
        )
    )

    assert registry.validate(
        "tenant.created",
        1,
        {"tenant_id": "t1"},
    ) is True
    assert registry.validate(
        "tenant.created",
        1,
        {},
    ) is False
