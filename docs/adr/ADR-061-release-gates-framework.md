# ADR-061 — Release Gates Framework

## Status

Accepted

## Decision

Separate current version gates from historical release gates.

## Consequence

Future milestones must place active gates under `tests/release/current` and historical gates under `tests/release/history`.
