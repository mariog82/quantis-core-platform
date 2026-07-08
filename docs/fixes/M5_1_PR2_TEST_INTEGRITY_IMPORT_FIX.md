# M5.1 PR2 Test Integrity Import Fix

## Problema

`tools.test_integrity` risultava namespace package e non esportava `run_test_integrity_checks`.

Pytest emetteva ancora un warning perché gli alias pubblici `TestIntegrityReport` e `TestIntegrityIssue` iniziavano con `Test`.

## Correzione

- aggiunto/ripristinato `tools/__init__.py`;
- aggiunto/ripristinato `tools/test_integrity/__init__.py`;
- esportato `run_test_integrity_checks`;
- impostato `__test__ = False` sulle classi e sugli alias pubblici.
