# M5 Beta Ruff and SDK Import Fix

## Problema

La release M5 Beta presentava:

- import inutilizzati rilevati da Ruff;
- test con più istruzioni sulla stessa riga;
- collisione del nome `sdk` durante il gate dei package pubblici.

## Correzione

- rimossi gli import inutilizzati;
- riscritti i test senza `;`;
- aggiunto `__all__` al package di test `tests/framework/adapters/sdk`.
