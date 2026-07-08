class NotificationRuntime:
    def __init__(self, adapter):
        self.adapter = adapter
    def send(self, request):
        return self.adapter.send(request)
    def list_sent(self):
        return self.adapter.list_sent()
