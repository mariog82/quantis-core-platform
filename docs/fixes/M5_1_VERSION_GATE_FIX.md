# M5.1 Version Gate Fix

## Problema

Il gate storico M5 controllava ancora il file globale `VERSION`.

Durante M5.1 il file `VERSION` deve diventare `0.5.1-alpha.1`, quindi il test M5 non deve più confrontare la versione corrente.

## Correzione

- `test_m5_version_gate.py` verifica ora che la versione M5 beta sia registrata in `docs/release/M5_BETA_FREEZE.md`.
- `test_m5_1_version_gate.py` verifica la versione corrente `0.5.1-alpha.1`.
