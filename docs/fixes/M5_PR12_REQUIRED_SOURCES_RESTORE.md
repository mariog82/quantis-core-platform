# M5 PR12 Required Sources Restore

## Problema

Il beta freeze aggiungeva i gate di stabilizzazione, ma alcuni sorgenti richiesti dai gate non erano presenti nel branch:

- `framework/adapters/identity/__init__.py`
- sorgenti Identity Provider Adapter
- sorgenti SDK, incluso `sdk/client.py`

## Correzione

Ripristinati i sorgenti minimi richiesti per Identity Provider Adapter e SDK Foundations.
