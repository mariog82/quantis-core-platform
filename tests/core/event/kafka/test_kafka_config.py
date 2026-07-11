from core.event import KafkaConfig


def test_kafka_config_builds_topic_name():
    config = KafkaConfig(topic_prefix="quantis-test")

    assert config.topic_name("tenant.created") == "quantis-test-tenant-created"
