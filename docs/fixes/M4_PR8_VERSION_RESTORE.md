# M4 PR8 Version Restore

## Problema

Il gate M4 falliva perché `VERSION` è tornato a:

```text
0.3.0-beta.1
```

mentre M4 PR8 richiede:

```text
0.4.0-beta.1
```

## Correzione

Ripristinato `VERSION` a `0.4.0-beta.1`.

## Verifica

```powershell
type VERSION
ruff check .
python -m pytest tests/services/stabilization
python -m pytest tests/core tests/framework tests/modules tests/services
```
