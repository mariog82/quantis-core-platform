class RabbitMQException(Exception):
    pass


class RabbitMQPublishException(RabbitMQException):
    pass


class RabbitMQConsumeException(RabbitMQException):
    pass


class RabbitMQConfigurationException(RabbitMQException):
    pass
