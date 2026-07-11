from framework.adapters import Adapter, AdapterMetadata, AdapterResult
from framework.adapters.payment.contracts import (
    PaymentRefundRequest,
    PaymentRefundResponse,
    PaymentRequest,
    PaymentResponse,
    PaymentStatus,
)


class PaymentAdapter(Adapter):
    metadata = AdapterMetadata(
        name="payment",
        adapter_type="payment",
        version="0.5.0-beta.1",
        capabilities=["payment"],
        provider="quantis",
    )

    def authorize(self, request: PaymentRequest) -> PaymentResponse:
        raise NotImplementedError

    def capture(self, payment_id: str) -> PaymentResponse:
        raise NotImplementedError

    def refund(self, request: PaymentRefundRequest) -> PaymentRefundResponse:
        raise NotImplementedError

    def execute(self, operation: str, payload: dict | None = None) -> AdapterResult:
        payload = payload or {}
        if operation == "authorize":
            return AdapterResult.ok(self.authorize(payload["request"]))
        if operation == "capture":
            return AdapterResult.ok(self.capture(payload["payment_id"]))
        if operation == "refund":
            return AdapterResult.ok(self.refund(payload["request"]))
        return AdapterResult.fail("UNSUPPORTED_OPERATION")


class InMemoryPaymentAdapter(PaymentAdapter):
    def __init__(self):
        super().__init__()
        self._payments: dict[str, PaymentResponse] = {}

    def authorize(self, request: PaymentRequest) -> PaymentResponse:
        response = PaymentResponse(
            status=PaymentStatus.AUTHORIZED
            if request.amount_cents > 0
            else PaymentStatus.FAILED,
            amount_cents=request.amount_cents,
            currency=request.currency,
            error=None if request.amount_cents > 0 else "INVALID_AMOUNT",
        )
        self._payments[response.payment_id] = response
        return response

    def capture(self, payment_id: str) -> PaymentResponse:
        payment = self._payments[payment_id]
        payment.status = PaymentStatus.CAPTURED
        return payment

    def refund(self, request: PaymentRefundRequest) -> PaymentRefundResponse:
        payment = self._payments[request.payment_id]
        payment.status = PaymentStatus.REFUNDED
        return PaymentRefundResponse(
            payment_id=payment.payment_id,
            amount_cents=request.amount_cents or payment.amount_cents,
        )
