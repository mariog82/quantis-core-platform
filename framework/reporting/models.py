from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable
from uuid import uuid4


class ReportFormat(str, Enum):
    TEXT = "text"
    HTML = "html"
    PDF = "pdf"
    XLSX = "xlsx"
    JSON = "json"


@dataclass(frozen=True)
class ReportId:
    value: str = field(default_factory=lambda: str(uuid4()))


@dataclass
class ReportContext:
    tenant_id: str | None = None
    actor_id: str | None = None
    filters: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class ReportDefinition:
    id: ReportId
    name: str
    title: str
    description: str = ""
    default_format: ReportFormat = ReportFormat.TEXT
    provider: Callable[[ReportContext], dict[str, Any]] | None = None


@dataclass
class Report:
    definition: ReportDefinition
    payload: dict[str, Any]
    context: ReportContext


@dataclass
class ReportOutput:
    name: str
    format: ReportFormat
    content: bytes
    content_type: str
    metadata: dict[str, Any] = field(default_factory=dict)
