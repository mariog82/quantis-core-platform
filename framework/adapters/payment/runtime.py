from framework.adapters.payment.adapter import PaymentAdapter
from framework.adapters.payment.contracts import (
    PaymentRefundRequest,
    PaymentRefundResponse,
    PaymentRequest,
    PaymentResponse,
)


class PaymentRuntime:
    def __init__(self, adapter: PaymentAdapter):
        self.adapter = adapter

    def authorize(self, request: PaymentRequest) -> PaymentResponse:
        return self.adapter.authorize(request)

    def capture(self, payment_id: str) -> PaymentResponse:
        return self.adapter.capture(payment_id)

    def refund(self, request: PaymentRefundRequest) -> PaymentRefundResponse:
        return self.adapter.refund(request)
