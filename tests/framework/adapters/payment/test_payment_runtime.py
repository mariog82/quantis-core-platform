from framework.adapters.payment import InMemoryPaymentAdapter, PaymentRefundRequest, PaymentRequest
from framework.adapters.payment.runtime import PaymentRuntime


def test_payment_runtime_authorizes_captures_and_refunds():
    runtime = PaymentRuntime(InMemoryPaymentAdapter())
    authorization = runtime.authorize(PaymentRequest(amount_cents=1500))
    capture = runtime.capture(authorization.payment_id)
    refund = runtime.refund(PaymentRefundRequest(payment_id=authorization.payment_id))
    assert authorization.successful is True
    assert capture.successful is True
    assert refund.payment_id == authorization.payment_id
