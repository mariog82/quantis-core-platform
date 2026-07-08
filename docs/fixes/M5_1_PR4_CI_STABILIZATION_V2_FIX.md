# M5.1 PR4 CI Stabilization v2 Fix

## Problema

Il workflow `m5-1-ci-stabilization.yml` installava Ruff ma non eseguiva `ruff check .`.

Inoltre il checker era troppo rigido perché cercava comandi letterali invece di pattern semantici.

## Correzione

- aggiunto step `Ruff` nel workflow M5.1;
- sostituito il controllo letterale `REQUIRED_COMMANDS` con `REQUIRED_PATTERNS`;
- aggiornati i test per accettare anche varianti come `python -m ruff check .`.
