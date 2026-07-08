# M5 Version Gate Final Fix

## Problema

Il test storico M5 continuava a leggere `VERSION`, ma `VERSION` deve rappresentare la release corrente del repository.

Durante M5.1.1 il valore corretto è:

`0.5.1-alpha.7`

La versione M5 deve essere verificata nel documento storico:

`docs/release/M5_BETA_FREEZE.md`

## Correzione

`test_m5_version_gate.py` ora verifica il documento di freeze M5 invece del file globale `VERSION`.
