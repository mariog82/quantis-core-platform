# M5 Beta SDK Generator Source Restore

## Problema

La CI non trovava `sdk.generator` perché i sorgenti del package `sdk/generator` non erano presenti nel branch.

## Correzione

Ripristinati:

- `sdk/__init__.py`
- `sdk/client.py`
- `sdk/config.py`
- `sdk/response.py`
- `sdk/exceptions.py`
- `sdk/generator/__init__.py`
- `sdk/generator/manifest.py`
- `sdk/generator/openapi.py`
- test SDK generator
