# M5 Beta SDK Generator Import Fix

## Problema

Durante il gate dei package pubblici, `sdk` poteva essere risolto dal package di test:

`tests/framework/adapters/sdk`

invece che dal package applicativo:

`sdk`

Questo causava:

`ModuleNotFoundError: No module named 'sdk.generator'`

## Correzione

Il gate ora forza la root del repository come primo elemento di `sys.path` e rimuove eventuali moduli `sdk` caricati dal package di test.
