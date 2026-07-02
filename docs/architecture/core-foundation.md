\# M1 - Core Foundation



\## Obiettivo



Costruire il nucleo della Quantis Core Platform™.



Il Core non contiene logica di dominio.



È completamente indipendente dai prodotti verticali.



\## Architettura

&#x20;                Quantis Core Platform™



&#x20;                    Framework



&#x20;                          │



&#x20;       ┌──────────────────┼──────────────────┐



&#x20;       │                  │                  │



&#x20;    Identity           Event Bus        Observability



&#x20;       │                  │                  │



&#x20;     Tenant            Workflow         Configuration



&#x20;       │                  │                  │



&#x20;     Audit              Plugin            Licensing

\## Responsabilità



Il Core fornisce:



\- autenticazione



\- autorizzazione



\- gestione tenant



\- eventi



\- logging



\- configurazione



\- audit



\- plugin



\## Non contiene



\- business logic



\- dashboard



\- analytics



\- AI



\- report



\- moduli verticali

