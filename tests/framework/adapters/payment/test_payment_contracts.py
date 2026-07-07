from framework.adapters.payment import Currency, PaymentRequest, PaymentResponse, PaymentStatus


def test_payment_request_defaults():
    request = PaymentRequest(amount_cents=1000, description="Demo")
    assert request.currency == Currency.EUR
    assert request.amount_cents == 1000


def test_payment_response_successful_property():
    response = PaymentResponse(status=PaymentStatus.AUTHORIZED)
    assert response.successful is True
