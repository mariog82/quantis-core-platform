from copy import deepcopy
from typing import Any, Protocol


class ReadModelRepository(Protocol):
    def save(self, model_type: str, key: str, value: dict[str, Any]) -> None:
        ...

    def get(self, model_type: str, key: str) -> dict[str, Any] | None:
        ...

    def search(
        self,
        model_type: str,
        filters: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        ...


class InMemoryReadModelRepository:
    def __init__(self) -> None:
        self._models: dict[str, dict[str, dict[str, Any]]] = {}

    def save(self, model_type: str, key: str, value: dict[str, Any]) -> None:
        self._models.setdefault(model_type, {})[key] = deepcopy(value)

    def get(self, model_type: str, key: str) -> dict[str, Any] | None:
        value = self._models.get(model_type, {}).get(key)
        return deepcopy(value) if value is not None else None

    def search(
        self,
        model_type: str,
        filters: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        values = list(self._models.get(model_type, {}).values())
        if not filters:
            return deepcopy(values)

        return [
            deepcopy(value)
            for value in values
            if all(value.get(key) == expected for key, expected in filters.items())
        ]
