from __future__ import annotations

from typing import Generic, Protocol, TypeVar

T = TypeVar("T")
ID = TypeVar("ID")


class Repository(Protocol, Generic[T, ID]):
    def save(self, entity: T) -> T:
        ...

    def get(self, entity_id: ID) -> T | None:
        ...

    def delete(self, entity_id: ID) -> bool:
        ...

    def list(self) -> list[T]:
        ...


class BaseRepository(Generic[T, ID]):
    def save(self, entity: T) -> T:
        raise NotImplementedError

    def get(self, entity_id: ID) -> T | None:
        raise NotImplementedError

    def delete(self, entity_id: ID) -> bool:
        raise NotImplementedError

    def list(self) -> list[T]:
        raise NotImplementedError
