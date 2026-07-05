from dataclasses import dataclass


@dataclass
class TaxRate:
    key: str
    percentage: float


class TaxCalculator:
    def calculate(self, amount_cents: int, tax_rate: TaxRate | None = None) -> int:
        if tax_rate is None:
            return 0
        return int(round(amount_cents * tax_rate.percentage / 100))
