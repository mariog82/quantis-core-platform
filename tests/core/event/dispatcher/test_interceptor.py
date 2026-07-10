from core.event import (
    Event,
    EventEnvelope,
    EventType,
    InMemoryEventDispatcher,
    RecordingInterceptor,
)


def test_dispatcher_runs_interceptors_before_and_after():
    dispatcher = InMemoryEventDispatcher()
    interceptor = RecordingInterceptor()
    dispatcher.add_interceptor(interceptor)

    envelope = EventEnvelope(Event(EventType("invoice.generated"), {}))
    result = dispatcher.dispatch(envelope)

    assert interceptor.before == [envelope.event_id]
    assert interceptor.after == [result.event_id]
