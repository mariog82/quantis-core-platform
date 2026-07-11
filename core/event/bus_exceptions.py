class EventBusException(Exception):
    pass


class EventBusPublishException(EventBusException):
    pass


class EventBusSubscriptionException(EventBusException):
    pass


class EventBusBackendException(EventBusException):
    pass
