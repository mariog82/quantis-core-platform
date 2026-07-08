# M5.1 PR2 Test Integrity Fix

## Problema

Il test positivo costruiva un repository temporaneo senza creare il test directory richiesto da `tools/repository_integrity`.

Inoltre Pytest emetteva un warning perché la dataclass pubblica `TestIntegrityReport` iniziava con `Test`.

## Correzione

- aggiunta `tests/tools/repository_integrity` al fixture del test positivo;
- rinominate le classi interne in `IntegrityIssue` e `IntegrityReport`;
- mantenuti alias pubblici `TestIntegrityIssue` e `TestIntegrityReport`.
