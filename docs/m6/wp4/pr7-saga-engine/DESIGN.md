# Design Notes

The Saga Engine uses orchestration semantics.

Completed steps are compensated in reverse order when a subsequent action fails.
