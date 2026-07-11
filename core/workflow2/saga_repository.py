from typing import Protocol

from core.workflow2.saga import SagaId, SagaInstance


class SagaRepository(Protocol):
    def save(self, instance: SagaInstance) -> SagaInstance:
        ...

    def get(self, saga_id: SagaId) -> SagaInstance | None:
        ...

    def list_all(self) -> list[SagaInstance]:
        ...


class InMemorySagaRepository:
    def __init__(self) -> None:
        self._instances: dict[str, SagaInstance] = {}

    def save(self, instance: SagaInstance) -> SagaInstance:
        self._instances[instance.saga_id.value] = instance
        return instance

    def get(self, saga_id: SagaId) -> SagaInstance | None:
        return self._instances.get(saga_id.value)

    def list_all(self) -> list[SagaInstance]:
        return list(self._instances.values())
