from core.event import RabbitMQConfig


def test_rabbitmq_config_builds_queue_name():
    config = RabbitMQConfig(queue_prefix="quantis-test")

    assert (
        config.queue_name("tenant.created", "tenant-projection")
        == "quantis-test-tenant-projection-tenant-created"
    )
