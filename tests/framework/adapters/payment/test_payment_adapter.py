from framework.adapters.payment import (
    InMemoryPaymentAdapter,
    PaymentRefundRequest,
    PaymentRequest,
    PaymentStatus,
)


def test_in_memory_payment_adapter_authorizes_and_captures():
    adapter = InMemoryPaymentAdapter()
    authorization = adapter.authorize(PaymentRequest(amount_cents=2500))
    capture = adapter.capture(authorization.payment_id)
    assert authorization.successful is True
    assert capture.status == PaymentStatus.CAPTURED


def test_in_memory_payment_adapter_rejects_invalid_amount():
    adapter = InMemoryPaymentAdapter()
    response = adapter.authorize(PaymentRequest(amount_cents=0))
    assert response.status == PaymentStatus.FAILED
    assert response.error == "INVALID_AMOUNT"


def test_in_memory_payment_adapter_refunds_payment():
    adapter = InMemoryPaymentAdapter()
    authorization = adapter.authorize(PaymentRequest(amount_cents=3000))
    adapter.capture(authorization.payment_id)
    refund = adapter.refund(PaymentRefundRequest(payment_id=authorization.payment_id))
    assert refund.status == PaymentStatus.REFUNDED
    assert refund.amount_cents == 3000


def test_payment_adapter_execute_operations():
    adapter = InMemoryPaymentAdapter()
    authorize_result = adapter.execute("authorize", {"request": PaymentRequest(amount_cents=1000)})
    payment_id = authorize_result.data.payment_id
    capture_result = adapter.execute("capture", {"payment_id": payment_id})
    refund_result = adapter.execute("refund", {"request": PaymentRefundRequest(payment_id=payment_id)})
    assert authorize_result.success is True
    assert capture_result.success is True
    assert refund_result.success is True
