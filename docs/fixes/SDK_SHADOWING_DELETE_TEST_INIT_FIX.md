# SDK Shadowing Delete Test Init Fix

## Problema

`tests/framework/adapters/sdk/__init__.py` trasforma la cartella dei test in un package chiamato `sdk`.

Quando pytest mette `tests/framework/adapters` nel path, `import sdk` viene risolto da:

`tests/framework/adapters/sdk/__init__.py`

invece che da:

`sdk/__init__.py`

## Correzione

Eliminare:

- `tests/framework/adapters/sdk/__init__.py`
- `tests/framework/adapters/sdk/__pycache__`
- `tests/sdk/__pycache__`

I test non devono diventare package applicativi con lo stesso nome dei package reali.
