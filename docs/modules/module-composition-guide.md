# Module Composition Guide

## Standard reusable flow

```text
Analytics → Dashboard
Analytics → Reporting
Reporting → Notification
```

## Vertical composition rule

Verticals should compose modules through their public APIs and should not modify module internals.
