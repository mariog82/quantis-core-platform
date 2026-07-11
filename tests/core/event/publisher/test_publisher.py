from core.event.contracts import Event, EventType
from core.event.publisher import InMemoryPublisher

def test_publish():
    p=InMemoryPublisher()
    e=Event(EventType("tenant.created"),{})
    env=p.publish(e)
    assert env.event==e
    assert p.metrics.published==1
