from dataclasses import dataclass, field
from enum import Enum
from uuid import uuid4


class PaymentProviderType(str, Enum):
    MEMORY = "memory"


class PaymentStatus(str, Enum):
    AUTHORIZED = "authorized"
    CAPTURED = "captured"
    FAILED = "failed"
    REFUNDED = "refunded"


class Currency(str, Enum):
    EUR = "EUR"


@dataclass
class PaymentRequest:
    amount_cents: int
    currency: Currency = Currency.EUR
    description: str = ""


@dataclass
class PaymentResponse:
    payment_id: str = field(default_factory=lambda: str(uuid4()))
    status: PaymentStatus = PaymentStatus.AUTHORIZED
    amount_cents: int = 0
    currency: Currency = Currency.EUR
    provider: PaymentProviderType = PaymentProviderType.MEMORY
    error: str | None = None

    @property
    def successful(self) -> bool:
        return self.status in {PaymentStatus.AUTHORIZED, PaymentStatus.CAPTURED, PaymentStatus.REFUNDED}


@dataclass(frozen=True)
class PaymentRefundRequest:
    payment_id: str
    amount_cents: int | None = None


@dataclass
class PaymentRefundResponse:
    refund_id: str = field(default_factory=lambda: str(uuid4()))
    payment_id: str = ""
    status: PaymentStatus = PaymentStatus.REFUNDED
    amount_cents: int = 0
    error: str | None = None
