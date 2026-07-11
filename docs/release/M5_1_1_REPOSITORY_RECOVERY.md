# M5.1.1 -- Repository Recovery

**Version:** `0.5.1-alpha.7`

## Obiettivo

La milestone **M5.1.1 -- Repository Recovery** consolida il lavoro
svolto durante M5.1, ripristina gli strumenti di qualità del repository
e prepara una baseline stabile per il **Beta Freeze 0.5.1-beta.1**.

## Attività completate

### Repository Integrity

-   Ripristino dei package pubblici.
-   Verifica dei file obbligatori.
-   Controllo dei package namespace non intenzionali.

### Test Integrity

-   Ripristino dei test mancanti.
-   Verifica della copertura minima dei package pubblici.
-   Controllo delle directory contenenti esclusivamente `__pycache__`.

### Public API Integrity

-   Verifica di `__all__`.
-   Controllo delle esportazioni pubbliche.
-   Validazione dei simboli richiesti.

### CI Stabilization

-   Aggiornamento dei workflow GitHub Actions.
-   Inserimento dei controlli:
    -   `ruff check .`
    -   `pytest`
    -   Repository Integrity
    -   Test Integrity
    -   Public API Integrity
    -   Release Manager
    -   Repository Audit

### Repository Audit

-   Analisi della struttura del repository.
-   Individuazione dei package incompleti.
-   Rimozione delle directory contenenti solo `__pycache__`.

### SDK Recovery

-   Risoluzione dei conflitti di importazione tra il package applicativo
    `sdk` e i package di test.
-   Consolidamento della struttura del package SDK.

## Risultato

La milestone M5.1.1 costituisce la baseline tecnica immediatamente
precedente al **M5.1 Beta Freeze (`0.5.1-beta.1`)**.

## Versione storica

Questa release documenta la versione:

`0.5.1-alpha.7`

La versione corrente del repository è gestita separatamente tramite il
file `VERSION`.
