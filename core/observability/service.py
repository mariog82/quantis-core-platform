from core.observability.contracts import LogRecord, MetricRecord, Span, TraceId
from core.observability.in_memory import InMemoryLogger, InMemoryMetrics, InMemoryTracer

class ObservabilityService:
    def __init__(
        self,
        logger: InMemoryLogger | None = None,
        metrics: InMemoryMetrics | None = None,
        tracer: InMemoryTracer | None = None,
    ):
        self.logger = logger or InMemoryLogger()
        self.metrics = metrics or InMemoryMetrics()
        self.tracer = tracer or InMemoryTracer()

    def log(self, level: str, message: str, **context) -> LogRecord:
        record = LogRecord(level=level, message=message, context=context)
        self.logger.emit(record)
        return record

    def metric(self, name: str, value: float, unit: str = "count", labels: dict | None = None) -> MetricRecord:
        metric = MetricRecord(name=name, value=value, unit=unit, labels=labels or {})
        self.metrics.record(metric)
        return metric

    def span(self, name: str, trace_id: TraceId | None = None, attributes: dict | None = None) -> Span:
        return self.tracer.start_span(name, trace_id=trace_id, attributes=attributes)
