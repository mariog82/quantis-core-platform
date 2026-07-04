from services.billing import BillingService, Invoice, InvoiceLine


def test_billing_service_issues_invoice():
    service = BillingService()
    invoice = Invoice(
        tenant_id="tenant-demo",
        lines=[
            InvoiceLine(description="Plan", amount_cents=9900),
            InvoiceLine(description="Addon", amount_cents=1000),
        ],
    )

    result = service.issue(invoice)

    assert result.success is True
    assert result.data["total_cents"] == 10900
