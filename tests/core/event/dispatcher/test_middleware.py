from core.event import (
    CorrelationMiddleware,
    Event,
    EventEnvelope,
    EventType,
    HeaderMiddleware,
    InMemoryEventDispatcher,
)


def test_dispatcher_executes_middleware_in_order():
    dispatcher = InMemoryEventDispatcher()
    dispatcher.use(CorrelationMiddleware(lambda: "corr-1"))
    dispatcher.use(HeaderMiddleware("x-quantis", "event"))

    envelope = EventEnvelope(Event(EventType("user.created"), {}))
    result = dispatcher.dispatch(envelope)

    assert result.event.metadata.correlation_id == "corr-1"
    assert result.event.metadata.headers["x-quantis"] == "event"
