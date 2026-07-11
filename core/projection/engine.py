from dataclasses import dataclass
from typing import Any, Protocol

from core.eventstore import EventRecord
from core.projection.exceptions import ProjectionHandlerNotFound
from core.projection.model import (
    ProjectionCheckpoint,
    ProjectionDefinition,
)
from core.projection.store import (
    InMemoryProjectionStore,
    ProjectionStore,
)


class ProjectionHandler(Protocol):
    def key_for(self, record: EventRecord) -> str:
        ...

    def apply(
        self,
        current_state: dict[str, Any],
        record: EventRecord,
    ) -> dict[str, Any]:
        ...


class ProjectionEngine(Protocol):
    def register(
        self,
        definition: ProjectionDefinition,
        handler: ProjectionHandler,
    ) -> None:
        ...

    def project(self, record: EventRecord) -> list[ProjectionCheckpoint]:
        ...


@dataclass(frozen=True)
class RegisteredProjection:
    definition: ProjectionDefinition
    handler: ProjectionHandler


class InMemoryProjectionEngine:
    def __init__(
        self,
        store: ProjectionStore | None = None,
    ) -> None:
        self.store = store or InMemoryProjectionStore()
        self._projections: dict[str, RegisteredProjection] = {}
        self._checkpoints: dict[tuple[str, str], ProjectionCheckpoint] = {}

    def register(
        self,
        definition: ProjectionDefinition,
        handler: ProjectionHandler,
    ) -> None:
        self._projections[definition.name] = RegisteredProjection(
            definition=definition,
            handler=handler,
        )

    def project(self, record: EventRecord) -> list[ProjectionCheckpoint]:
        checkpoints: list[ProjectionCheckpoint] = []
        event_type = record.envelope.event.event_type.name

        for registration in self._projections.values():
            if event_type not in registration.definition.event_types:
                continue

            key = registration.handler.key_for(record)
            current = self.store.get(registration.definition.name, key) or {}
            updated = registration.handler.apply(current, record)
            self.store.put(registration.definition.name, key, updated)

            checkpoint = ProjectionCheckpoint(
                projection_name=registration.definition.name,
                stream_id=record.stream_id,
                event_version=record.version,
            )
            self._checkpoints[
                (registration.definition.name, record.stream_id)
            ] = checkpoint
            checkpoints.append(checkpoint)

        if not checkpoints and not self._projections:
            raise ProjectionHandlerNotFound(event_type)

        return checkpoints

    def checkpoint(
        self,
        projection_name: str,
        stream_id: str,
    ) -> ProjectionCheckpoint | None:
        return self._checkpoints.get((projection_name, stream_id))
