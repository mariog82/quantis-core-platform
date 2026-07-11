from core.event import (
    Event,
    EventEnvelope,
    EventType,
    InMemoryDeadLetterQueue,
    InMemoryEventDispatcher,
    InMemoryEventSubscriber,
    RetryPolicy,
)


def test_dispatcher_moves_terminal_failure_to_deadletter_queue():
    subscriber = InMemoryEventSubscriber()
    queue = InMemoryDeadLetterQueue()

    def fail_handler(envelope):
        raise RuntimeError("boom")

    subscriber.subscribe("document.failed", fail_handler)

    dispatcher = InMemoryEventDispatcher(
        subscriber=subscriber,
        dead_letter_queue=queue,
        retry_policy=RetryPolicy(max_attempts=1),
    )

    result = dispatcher.dispatch(
        EventEnvelope(Event(EventType("document.failed"), {}))
    )

    assert result.attempts == 1
    assert len(queue.list_entries()) == 1
    assert queue.list_entries()[0].reason == "boom"
