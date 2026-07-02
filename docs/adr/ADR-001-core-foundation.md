\# ADR-001



\## Title



Core Foundation



\## Status



Accepted



\## Context



La piattaforma deve poter supportare molteplici prodotti verticali.



Duplicare codice infrastrutturale aumenterebbe il costo di manutenzione.



\## Decision



Creare un Core indipendente che implementi esclusivamente funzionalità riutilizzabili.



Ogni prodotto verticale utilizzerà il Core attraverso il Framework.



\## Consequences



Vantaggi



\- alta riusabilità



\- maggiore manutenibilità



\- standardizzazione



\- API uniformi



\- minore duplicazione



Svantaggi



\- maggiore investimento iniziale



\- progettazione più rigorosa



\- necessità di contratti stabili

