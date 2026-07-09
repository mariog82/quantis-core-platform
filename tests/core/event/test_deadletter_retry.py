from core.event import Event, EventEnvelope, EventType, InMemoryDeadLetterQueue, RetryPolicy


def test_retry_policy_and_deadletter_queue():
    policy = RetryPolicy(max_attempts=2)
    envelope = EventEnvelope(Event(EventType("failed.event"), {}))
    queue = InMemoryDeadLetterQueue()

    assert policy.should_retry(1) is True
    assert policy.should_retry(2) is False
    entry = queue.add(envelope, "boom")
    assert queue.list_entries()[0] == entry
