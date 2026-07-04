# M3 PR6 — Module Integration Tests

## Purpose

Validate that reusable M3 modules can work together through framework-neutral composition.

## Covered flows

- Runtime registration and lifecycle for default modules.
- Analytics results feeding Reporting.
- Analytics results feeding Dashboard.
- Reporting output feeding Notification.
- Full flow: Analytics → Dashboard → Reporting → Notification.

## Rule

Module integration tests must remain vertical-neutral. They validate reusable capabilities only.
