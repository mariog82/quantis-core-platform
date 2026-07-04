from __future__ import annotations

from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar("T")
ID = TypeVar("ID")


@dataclass
class RepositoryQuery:
    filters: dict = field(default_factory=dict)
    limit: int | None = None
    offset: int = 0


class BaseRepository(Generic[T, ID]):
    def save(self, entity: T) -> T:
        raise NotImplementedError

    def get(self, entity_id: ID) -> T | None:
        raise NotImplementedError

    def delete(self, entity_id: ID) -> bool:
        raise NotImplementedError

    def list(self, query: RepositoryQuery | None = None) -> list[T]:
        raise NotImplementedError


class InMemoryRepository(BaseRepository[T, ID]):
    def __init__(self):
        self._items: dict[ID, T] = {}

    def save(self, entity: T) -> T:
        entity_id = getattr(getattr(entity, "id", None), "value", None)
        if entity_id is None:
            entity_id = getattr(entity, "id", None)
        if entity_id is None:
            raise ValueError("ENTITY_ID_REQUIRED")
        self._items[entity_id] = entity
        return entity

    def get(self, entity_id: ID) -> T | None:
        key = getattr(entity_id, "value", entity_id)
        return self._items.get(key)

    def delete(self, entity_id: ID) -> bool:
        key = getattr(entity_id, "value", entity_id)
        return self._items.pop(key, None) is not None

    def list(self, query: RepositoryQuery | None = None) -> list[T]:
        values = list(self._items.values())
        query = query or RepositoryQuery()

        for field_name, expected in query.filters.items():
            values = [item for item in values if getattr(item, field_name, None) == expected]

        if query.offset:
            values = values[query.offset :]

        if query.limit is not None:
            values = values[: query.limit]

        return values
