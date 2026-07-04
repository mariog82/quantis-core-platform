# M3 PR3 Reporting Context Compatibility Fix

## Problema

I test del Reporting Module fallivano con:

```text
TypeError: ReportContext.__init__() got an unexpected keyword argument 'filters'
```

La causa è che nel branch corrente `framework.reporting.ReportContext` non espone `filters` come argomento del costruttore.

## Correzione

`ReportingModuleService` ora crea `ReportContext()` senza argomenti e valorizza dinamicamente:

- `context.filters`, se disponibile;
- `context.metadata`, come fallback compatibile.

## Verifica

```powershell
ruff check .
python -m pytest tests/modules/reporting
python -m pytest tests/core tests/framework tests/modules
```
