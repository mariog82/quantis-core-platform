from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class InvoiceLine:
    description: str
    amount_cents: int


@dataclass
class Invoice:
    tenant_id: str
    lines: list[InvoiceLine] = field(default_factory=list)
    invoice_id: str = field(default_factory=lambda: str(uuid4()))

    @property
    def total_cents(self) -> int:
        return sum(line.amount_cents for line in self.lines)
