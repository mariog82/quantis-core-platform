class RedisStreamsException(Exception):
    pass


class RedisStreamsPublishException(RedisStreamsException):
    pass


class RedisStreamsReadException(RedisStreamsException):
    pass


class RedisStreamsConfigurationException(RedisStreamsException):
    pass
