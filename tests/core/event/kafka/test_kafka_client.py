from core.event import InMemoryKafkaClient


def test_inmemory_kafka_client_produces_and_consumes():
    client = InMemoryKafkaClient()

    offset = client.produce(
        topic="quantis-test",
        key="event-1",
        value="payload",
        headers={"event_type": "tenant.created"},
    )
    records = client.consume("quantis-test")

    assert offset == "0"
    assert records == [
        (
            "event-1",
            "payload",
            {"event_type": "tenant.created"},
        )
    ]
