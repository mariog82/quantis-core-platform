from services.billing import BillingService, Invoice, InvoiceLine, InvoiceStatus, TaxRate


def test_billing_service_issues_invoice_with_tax():
    service = BillingService()
    invoice = Invoice(
        tenant_id="tenant-demo",
        lines=[InvoiceLine(description="Plan", amount_cents=10000)],
    )

    result = service.issue(invoice, TaxRate(key="vat22", percentage=22))

    assert result.success is True
    assert result.data["subtotal_cents"] == 10000
    assert result.data["tax_cents"] == 2200
    assert result.data["total_cents"] == 12200
    assert invoice.status == InvoiceStatus.ISSUED


def test_billing_service_marks_invoice_paid():
    service = BillingService()
    invoice = Invoice(
        tenant_id="tenant-demo",
        lines=[InvoiceLine(description="Plan", amount_cents=10000)],
    )
    service.issue(invoice)

    result = service.mark_paid(invoice.invoice_id)

    assert result.success is True
    assert service.get(invoice.invoice_id).status == InvoiceStatus.PAID
