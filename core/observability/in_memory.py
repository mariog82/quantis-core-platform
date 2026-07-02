from core.observability.contracts import (
    LogRecord,
    LoggerPort,
    MetricRecord,
    MetricsPort,
    Span,
    SpanId,
    TraceId,
    TracerPort,
)

class InMemoryLogger(LoggerPort):
    def __init__(self):
        self.records: list[LogRecord] = []

    def emit(self, record: LogRecord) -> None:
        self.records.append(record)

class InMemoryMetrics(MetricsPort):
    def __init__(self):
        self.records: list[MetricRecord] = []

    def record(self, metric: MetricRecord) -> None:
        self.records.append(metric)

    def summary(self) -> dict:
        grouped: dict[str, list[float]] = {}
        for metric in self.records:
            grouped.setdefault(metric.name, []).append(metric.value)
        return {
            name: {
                "count": len(values),
                "sum": sum(values),
                "avg": round(sum(values) / len(values), 3) if values else 0,
            }
            for name, values in grouped.items()
        }

class InMemoryTracer(TracerPort):
    def __init__(self):
        self.spans: list[Span] = []

    def start_span(self, name: str, trace_id: TraceId | None = None, attributes: dict | None = None) -> Span:
        span = Span(
            trace_id=trace_id or TraceId(),
            span_id=SpanId(),
            name=name,
            attributes=attributes or {},
        )
        self.spans.append(span)
        return span
