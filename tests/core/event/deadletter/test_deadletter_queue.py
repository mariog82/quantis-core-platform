from core.event import Event, EventEnvelope, EventStatus, EventType, InMemoryDeadLetterQueue


def test_deadletter_add_replay_remove():
    queue = InMemoryDeadLetterQueue()
    envelope = EventEnvelope(Event(EventType("document.failed"), {"id": "d1"}))

    entry = queue.add(envelope, "boom")

    assert entry.envelope.attempts == 1
    assert queue.get(entry.dead_letter_id) == entry

    replayed = queue.replay(entry.dead_letter_id)

    assert replayed is not None
    assert replayed.status == EventStatus.PENDING

    stored = queue.get(entry.dead_letter_id)

    assert stored is not None
    assert stored.replayed is True
    assert stored.replay_count == 1

    assert queue.remove(entry.dead_letter_id) is True
    assert queue.get(entry.dead_letter_id) is None
