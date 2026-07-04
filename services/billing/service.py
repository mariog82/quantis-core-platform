from services.base import EnterpriseService, ServiceResult
from services.billing.invoice import Invoice


class BillingService(EnterpriseService):
    name = "billing"

    def __init__(self):
        self._invoices: dict[str, Invoice] = {}

    def issue(self, invoice: Invoice) -> ServiceResult:
        self._invoices[invoice.invoice_id] = invoice
        return ServiceResult(
            success=True,
            data={
                "invoice_id": invoice.invoice_id,
                "total_cents": invoice.total_cents,
            },
        )

    def get(self, invoice_id: str) -> Invoice | None:
        return self._invoices.get(invoice_id)
