from core.event import RedisStreamsConfig


def test_redis_streams_config_builds_stream_name():
    config = RedisStreamsConfig(stream_prefix="quantis-test")

    assert config.stream_name("tenant.created") == "quantis-test:tenant:created"
