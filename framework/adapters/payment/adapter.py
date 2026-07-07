from abc import abstractmethod

from framework.adapters import Adapter, AdapterMetadata, AdapterResult
from framework.adapters.payment.contracts import (
    PaymentProviderType,
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
        version="0.5.0-alpha.9",
        description="Provider-neutral payment adapter contract.",
        capabilities=["payment", "authorization", "capture", "refund"],
        provider="quantis",
    )

    @abstractmethod
    def authorize(self, request: PaymentRequest) -> PaymentResponse:
        raise NotImplementedError

    @abstractmethod
    def capture(self, payment_id: str) -> PaymentResponse:
        raise NotImplementedError

    @abstractmethod
    def refund(self, request: PaymentRefundRequest) -> PaymentRefundResponse:
        raise NotImplementedError

    def execute(self, operation: str, payload: dict | None = None) -> AdapterResult:
        payload = payload or {}
        if operation == "authorize":
            request = payload.get("request")
            if not isinstance(request, PaymentRequest):
                return AdapterResult.fail("INVALID_PAYMENT_REQUEST")
            return AdapterResult.ok(self.authorize(request))
        if operation == "capture":
            payment_id = payload.get("payment_id")
            if not isinstance(payment_id, str):
                return AdapterResult.fail("INVALID_PAYMENT_ID")
            return AdapterResult.ok(self.capture(payment_id))
        if operation == "refund":
            request = payload.get("request")
            if not isinstance(request, PaymentRefundRequest):
                return AdapterResult.fail("INVALID_REFUND_REQUEST")
            return AdapterResult.ok(self.refund(request))
        return AdapterResult.fail("UNSUPPORTED_OPERATION")


class InMemoryPaymentAdapter(PaymentAdapter):
    metadata = AdapterMetadata(
        name="memory-payment",
        adapter_type="payment",
        version="0.5.0-alpha.9",
        description="In-memory payment adapter for tests.",
        capabilities=["payment", "authorization", "capture", "refund"],
        provider=PaymentProviderType.MEMORY.value,
    )

    def __init__(self):
        super().__init__()
        self._payments: dict[str, PaymentResponse] = {}
        self._refunds: dict[str, PaymentRefundResponse] = {}

    def authorize(self, request: PaymentRequest) -> PaymentResponse:
        if request.amount_cents <= 0:
            response = PaymentResponse(
                status=PaymentStatus.FAILED,
                amount_cents=request.amount_cents,
                currency=request.currency,
                provider=PaymentProviderType.MEMORY,
                error="INVALID_AMOUNT",
            )
        else:
            response = PaymentResponse(
                status=PaymentStatus.AUTHORIZED,
                amount_cents=request.amount_cents,
                currency=request.currency,
                provider=PaymentProviderType.MEMORY,
                metadata={"description": request.description},
            )
        self._payments[response.payment_id] = response
        return response

    def capture(self, payment_id: str) -> PaymentResponse:
        payment = self._payments.get(payment_id)
        if payment is None:
            return PaymentResponse(
                payment_id=payment_id,
                status=PaymentStatus.FAILED,
                provider=PaymentProviderType.MEMORY,
                error="PAYMENT_NOT_FOUND",
            )
        if payment.status != PaymentStatus.AUTHORIZED:
            payment.status = PaymentStatus.FAILED
            payment.error = "PAYMENT_NOT_AUTHORIZED"
            return payment
        payment.status = PaymentStatus.CAPTURED
        return payment

    def refund(self, request: PaymentRefundRequest) -> PaymentRefundResponse:
        payment = self._payments.get(request.payment_id)
        if payment is None:
            return PaymentRefundResponse(
                payment_id=request.payment_id,
                status=PaymentStatus.FAILED,
                error="PAYMENT_NOT_FOUND",
            )
        amount = request.amount_cents if request.amount_cents is not None else payment.amount_cents
        payment.status = PaymentStatus.REFUNDED
        response = PaymentRefundResponse(
            payment_id=payment.payment_id,
            status=PaymentStatus.REFUNDED,
            amount_cents=amount,
        )
        self._refunds[response.refund_id] = response
        return response

    def list_payments(self) -> list[PaymentResponse]:
        return list(self._payments.values())
