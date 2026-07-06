# Billing Service Guide

## Purpose

The Billing Service provides provider-neutral invoice primitives.

## Public API

- `Invoice`
- `InvoiceLine`
- `InvoiceStatus`
- `TaxRate`
- `TaxCalculator`
- `BillingService`

## Provider-neutrality

FatturaPA, Stripe invoices, PagoPA and accounting integrations must be implemented as adapters.
