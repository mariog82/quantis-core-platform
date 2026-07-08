# M5 Historical Version Gate Fix

## Problema

Il test M5 continuava a leggere `VERSION`, ma il file globale `VERSION` rappresenta sempre la versione corrente del repository.

Durante M5.1 il valore corretto è:

`0.5.1-alpha.6`

La versione M5 deve invece essere verificata come dato storico nel documento di freeze.

## Correzione

- `test_m5_version_gate.py` ora controlla `docs/release/M5_BETA_FREEZE.md`;
- `test_m5_1_version_gate.py` continua a controllare il file globale `VERSION`.
