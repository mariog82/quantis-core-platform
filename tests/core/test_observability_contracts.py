from core.observability import ObservabilityService, TraceId

def test_log_record_is_emitted():
    service = ObservabilityService()
    record = service.log("INFO", "platform started", tenant_id="tenant-demo")
    assert record.message == "platform started"
    assert len(service.logger.records) == 1

def test_metric_record_is_collected():
    service = ObservabilityService()
    service.metric("request.count", 1, labels={"route": "/health"})
    service.metric("request.count", 2, labels={"route": "/health"})
    summary = service.metrics.summary()
    assert summary["request.count"]["count"] == 2
    assert summary["request.count"]["sum"] == 3

def test_span_is_created_and_finished():
    service = ObservabilityService()
    trace_id = TraceId("trace-1")
    span = service.span("core.operation", trace_id=trace_id, attributes={"component": "test"})
    span.finish()
    assert span.trace_id.value == "trace-1"
    assert span.ended_at is not None
    assert len(service.tracer.spans) == 1
