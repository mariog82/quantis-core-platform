class PaymentRuntime:
    def __init__(self, adapter):
        self.adapter = adapter
    def authorize(self, request):
        return self.adapter.authorize(request)
    def capture(self, payment_id):
        return self.adapter.capture(payment_id)
    def refund(self, request):
        return self.adapter.refund(request)
