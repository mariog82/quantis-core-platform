from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Literal
from uuid import uuid4

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

@dataclass(frozen=True)
class TraceId:
    value: str = field(default_factory=lambda: str(uuid4()))

@dataclass(frozen=True)
class SpanId:
    value: str = field(default_factory=lambda: str(uuid4()))

@dataclass
class LogRecord:
    level: LogLevel
    message: str
    service: str = "quantis-core"
    tenant_id: str | None = None
    trace_id: str | None = None
    span_id: str | None = None
    context: dict = field(default_factory=dict)
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

@dataclass
class MetricRecord:
    name: str
    value: float
    unit: str = "count"
    labels: dict = field(default_factory=dict)
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

@dataclass
class Span:
    trace_id: TraceId
    span_id: SpanId
    name: str
    service: str = "quantis-core"
    attributes: dict = field(default_factory=dict)
    started_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    ended_at: datetime | None = None

    def finish(self) -> None:
        self.ended_at = datetime.now(timezone.utc)

class LoggerPort:
    def emit(self, record: LogRecord) -> None:
        raise NotImplementedError

class MetricsPort:
    def record(self, metric: MetricRecord) -> None:
        raise NotImplementedError

class TracerPort:
    def start_span(self, name: str, trace_id: TraceId | None = None, attributes: dict | None = None) -> Span:
        raise NotImplementedError
