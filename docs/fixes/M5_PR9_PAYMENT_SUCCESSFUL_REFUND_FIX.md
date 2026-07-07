# M5 PR9 Payment Successful Refund Fix

## Problema

Il test runtime falliva perché `PaymentResponse.successful` considerava successful solo `AUTHORIZED` e `CAPTURED`.

Nel flusso runtime il pagamento viene autorizzato, catturato e poi rimborsato. Poiché l'adapter in memoria conserva lo stesso oggetto `PaymentResponse`, dopo il refund lo stato diventa `REFUNDED` e `successful` tornava `False`.

## Correzione

`PaymentResponse.successful` considera ora successful anche `REFUNDED`.

## Verifica

```powershell
ruff check .
python -m pytest tests/framework/adapters/payment
python -m pytest tests/core tests/framework tests/modules tests/services
```
