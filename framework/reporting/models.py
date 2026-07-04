from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable
from uuid import uuid4


class ReportFormat(str, Enum):
    TEXT = "text"


@dataclass(frozen=True)
class ReportId:
    value: str = field(default_factory=lambda: str(uuid4()))


@dataclass
class ReportContext:
    tenant_id: str | None = None


@dataclass
class ReportDefinition:
    id: ReportId
    name: str
    title: str
    provider: Callable[[ReportContext], dict[str, Any]] | None = None


@dataclass
class ReportOutput:
    name: str
    format: ReportFormat
    content: bytes
    content_type: str
