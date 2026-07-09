from core.event.publisher_factory import PublisherFactory
from core.event.publisher import InMemoryPublisher
def test_factory():
    assert isinstance(PublisherFactory.create(),InMemoryPublisher)
