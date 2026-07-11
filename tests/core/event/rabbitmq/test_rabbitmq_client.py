from core.event import InMemoryRabbitMQClient


def test_inmemory_rabbitmq_client_declares_binds_and_publishes():
    client = InMemoryRabbitMQClient()
    client.declare_exchange("events")
    client.declare_queue("queue-1")
    client.bind_queue("queue-1", "events", "tenant.created")

    message_id = client.publish(
        "events",
        "tenant.created",
        "payload",
    )

    assert message_id == "rabbit-1"
    assert client.get_messages("queue-1") == [
        ("rabbit-1", "payload")
    ]
