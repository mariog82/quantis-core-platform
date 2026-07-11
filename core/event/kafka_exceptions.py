class KafkaException(Exception):
    pass


class KafkaProduceException(KafkaException):
    pass


class KafkaConsumeException(KafkaException):
    pass


class KafkaConfigurationException(KafkaException):
    pass
