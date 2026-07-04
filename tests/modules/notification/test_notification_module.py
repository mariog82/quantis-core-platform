from modules.notification import NotificationModule


def test_notification_module_lifecycle_and_send():
    module = NotificationModule()

    module.initialize(context={})
    module.boot()
    module.start()

    assert module.initialized is True
    assert module.started is True
    assert module.send("user@example.com", "Subject", "Body") is True
