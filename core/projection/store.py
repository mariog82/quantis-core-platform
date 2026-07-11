from copy import deepcopy
from typing import Any, Protocol


class ProjectionStore(Protocol):
    def get(self, projection_name: str, key: str) -> dict[str, Any] | None:
        ...

    def put(
        self,
        projection_name: str,
        key: str,
        state: dict[str, Any],
    ) -> dict[str, Any]:
        ...

    def all(self, projection_name: str) -> dict[str, dict[str, Any]]:
        ...


class InMemoryProjectionStore:
    def __init__(self) -> None:
        self._data: dict[str, dict[str, dict[str, Any]]] = {}

    def get(self, projection_name: str, key: str) -> dict[str, Any] | None:
        state = self._data.get(projection_name, {}).get(key)
        return deepcopy(state) if state is not None else None

    def put(
        self,
        projection_name: str,
        key: str,
        state: dict[str, Any],
    ) -> dict[str, Any]:
        self._data.setdefault(projection_name, {})[key] = deepcopy(state)
        return deepcopy(state)

    def all(self, projection_name: str) -> dict[str, dict[str, Any]]:
        return deepcopy(self._data.get(projection_name, {}))
