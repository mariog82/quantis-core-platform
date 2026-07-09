# M5.1.1 Historical Gate Fix

## Problema

Il gate M5.1.1 controllava ancora il file globale `VERSION`.

Durante il Beta Freeze il file `VERSION` deve essere:

`0.5.1-beta.1`

La versione `0.5.1-alpha.7` deve invece restare verificata come release storica nel documento:

`docs/release/M5_1_1_REPOSITORY_RECOVERY.md`

## Correzione

- `test_m5_1_1_version_gate.py` ora controlla il documento storico M5.1.1.
- `test_m5_1_beta_version_gate.py` controlla la versione corrente beta.
