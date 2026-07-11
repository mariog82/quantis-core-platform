class SubscriberException(Exception):
    pass


class InvalidSubscriptionException(SubscriberException):
    pass


class DuplicateSubscriptionException(SubscriberException):
    pass


class SubscriberNotFoundException(SubscriberException):
    pass
