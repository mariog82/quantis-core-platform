# M5 Version Gates Fix

## Problema

Il test M4 controllava ancora il file globale `VERSION`, ma `VERSION` rappresenta la versione corrente del progetto. Durante M5 il valore corretto è `0.5.0-alpha.x`, quindi il gate storico M4 non deve più confrontare `VERSION`.

## Correzione

- `test_m4_version_gate.py` ora verifica che la versione M4 sia registrata nel documento di freeze M4.
- aggiunto `test_m5_version_gate.py` per verificare la versione corrente della milestone M5.
