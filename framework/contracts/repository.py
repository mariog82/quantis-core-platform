from typing import Generic, Protocol, TypeVar

T = TypeVar("T")
ID = TypeVar("ID")

class Repository(Protocol, Generic[T, ID]):
    def save(self, entity: T) -> T:
        ...

    def get(self, entity_id: ID) -> T | None:
        ...
