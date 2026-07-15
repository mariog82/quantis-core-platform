# ADR-091 — M7 Query Optimizer

## Status

Accepted

## Decision

Introduce a rule-based query optimizer before adding database-specific
translation and execution backends.

## Consequence

Quantis can normalize and reduce query cost independently from the selected
graph persistence engine.
