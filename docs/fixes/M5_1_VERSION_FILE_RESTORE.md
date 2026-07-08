# M5.1 Version File Restore

## Problema

Il test `tests/modules/stabilization/test_m3_release_gate.py` legge il file globale `VERSION`.

L'errore:

`FileNotFoundError: VERSION`

indica che il file `VERSION` non è presente nella root del repository dopo l'estrazione/copia delle patch.

## Correzione

Ripristinato il file root:

`VERSION`

con valore corrente:

`0.5.1-alpha.2`
