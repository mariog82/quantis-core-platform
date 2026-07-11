from dataclasses import dataclass, field
from enum import Enum
from uuid import uuid4


class InvoiceStatus(str, Enum):
    DRAFT = "draft"
    ISSUED = "issued"
    PAID = "paid"
    VOID = "void"


@dataclass
class InvoiceLine:
    description: str
    amount_cents: int
    quantity: int = 1

    @property
    def total_cents(self) -> int:
        return self.amount_cents * self.quantity


@dataclass
class Invoice:
    tenant_id: str
    lines: list[InvoiceLine] = field(default_factory=list)
    invoice_id: str = field(default_factory=lambda: str(uuid4()))
    status: InvoiceStatus = InvoiceStatus.DRAFT
    currency: str = "EUR"
    tax_cents: int = 0

    @property
    def subtotal_cents(self) -> int:
        return sum(line.total_cents for line in self.lines)

    @property
    def total_cents(self) -> int:
        return self.subtotal_cents + self.tax_cents

    def issue(self) -> None:
        self.status = InvoiceStatus.ISSUED

    def mark_paid(self) -> None:
        self.status = InvoiceStatus.PAID
