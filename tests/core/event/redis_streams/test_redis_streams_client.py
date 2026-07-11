from core.event import InMemoryRedisStreamsClient


def test_inmemory_redis_streams_client_adds_and_reads_messages():
    client = InMemoryRedisStreamsClient()

    message_id = client.xadd("quantis:test", {"payload": "value"})
    records = client.xrange("quantis:test")

    assert message_id == "1-0"
    assert records == [("1-0", {"payload": "value"})]
