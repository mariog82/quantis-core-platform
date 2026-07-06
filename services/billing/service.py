from services.base import EnterpriseService, ServiceResult
from services.billing.invoice import Invoice
from services.billing.tax import TaxCalculator, TaxRate


class BillingService(EnterpriseService):
    name = "billing"

    def __init__(self, tax_calculator: TaxCalculator | None = None):
        self._invoices: dict[str, Invoice] = {}
        self.tax_calculator = tax_calculator or TaxCalculator()

    def issue(self, invoice: Invoice, tax_rate: TaxRate | None = None) -> ServiceResult:
        invoice.tax_cents = self.tax_calculator.calculate(invoice.subtotal_cents, tax_rate)
        invoice.issue()
        self._invoices[invoice.invoice_id] = invoice
        return ServiceResult(
            success=True,
            data={
                "invoice_id": invoice.invoice_id,
                "subtotal_cents": invoice.subtotal_cents,
                "tax_cents": invoice.tax_cents,
                "total_cents": invoice.total_cents,
            },
        )

    def mark_paid(self, invoice_id: str) -> ServiceResult:
        invoice = self._invoices.get(invoice_id)
        if invoice is None:
            return ServiceResult(success=False, error="INVOICE_NOT_FOUND")
        invoice.mark_paid()
        return ServiceResult(success=True, data={"invoice_id": invoice_id})

    def get(self, invoice_id: str) -> Invoice | None:
        return self._invoices.get(invoice_id)

    def list_for_tenant(self, tenant_id: str) -> list[Invoice]:
        return [invoice for invoice in self._invoices.values() if invoice.tenant_id == tenant_id]
