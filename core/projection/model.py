from dataclasses import dataclass
from enum import Enum


class ProjectionStatus(str, Enum):
    IDLE = "idle"
    RUNNING = "running"
    FAILED = "failed"
    COMPLETED = "completed"


@dataclass(frozen=True)
class ProjectionDefinition:
    name: str
    event_types: tuple[str, ...]
    version: int = 1


@dataclass(frozen=True)
class ProjectionCheckpoint:
    projection_name: str
    stream_id: str
    event_version: int
