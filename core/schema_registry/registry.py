from dataclasses import dataclass
from typing import Any, Protocol


@dataclass(frozen=True)
class EventSchema:
    event_type: str
    version: int
    required_fields: tuple[str, ...]


class EventSchemaRegistry(Protocol):
    def register(self, schema: EventSchema) -> EventSchema:
        ...

    def get(self, event_type: str, version: int) -> EventSchema | None:
        ...

    def validate(
        self,
        event_type: str,
        version: int,
        payload: dict[str, Any],
    ) -> bool:
        ...


class InMemoryEventSchemaRegistry:
    def __init__(self) -> None:
        self._schemas: dict[tuple[str, int], EventSchema] = {}

    def register(self, schema: EventSchema) -> EventSchema:
        self._schemas[(schema.event_type, schema.version)] = schema
        return schema

    def get(self, event_type: str, version: int) -> EventSchema | None:
        return self._schemas.get((event_type, version))

    def validate(
        self,
        event_type: str,
        version: int,
        payload: dict[str, Any],
    ) -> bool:
        schema = self.get(event_type, version)
        if schema is None:
            return False

        return all(field in payload for field in schema.required_fields)
