from dataclasses import dataclass, field
from enum import Enum
from typing import Any
from uuid import uuid4


class PaymentProviderType(str, Enum):
    MEMORY = "memory"
    STRIPE = "stripe"
    PAYPAL = "paypal"
    NEXI = "nexi"
    PAGOPA = "pagopa"
    SEPA = "sepa"


class PaymentMethodType(str, Enum):
    CARD = "card"
    BANK_TRANSFER = "bank_transfer"
    WALLET = "wallet"
    PAGOPA = "pagopa"
    SEPA = "sepa"


class PaymentStatus(str, Enum):
    CREATED = "created"
    AUTHORIZED = "authorized"
    CAPTURED = "captured"
    FAILED = "failed"
    REFUNDED = "refunded"


class Currency(str, Enum):
    EUR = "EUR"
    USD = "USD"
    GBP = "GBP"


@dataclass(frozen=True)
class PaymentMethod:
    method_type: PaymentMethodType
    token: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class PaymentRequest:
    amount_cents: int
    currency: Currency = Currency.EUR
    description: str = ""
    method: PaymentMethod | None = None
    customer_id: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class PaymentResponse:
    payment_id: str = field(default_factory=lambda: str(uuid4()))
    status: PaymentStatus = PaymentStatus.CREATED
    amount_cents: int = 0
    currency: Currency = Currency.EUR
    provider: PaymentProviderType = PaymentProviderType.MEMORY
    error: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def successful(self) -> bool:
        return self.status in {PaymentStatus.AUTHORIZED, PaymentStatus.CAPTURED}


@dataclass(frozen=True)
class PaymentRefundRequest:
    payment_id: str
    amount_cents: int | None = None
    reason: str = ""


@dataclass
class PaymentRefundResponse:
    refund_id: str = field(default_factory=lambda: str(uuid4()))
    payment_id: str = ""
    status: PaymentStatus = PaymentStatus.REFUNDED
    amount_cents: int = 0
    error: str | None = None
