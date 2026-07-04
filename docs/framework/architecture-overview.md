# Framework Architecture Overview

The Framework is the programmable layer between Core capabilities and reusable Modules.

```text
Core
  ↓
Framework
  ↓
Modules
  ↓
Verticals
```

## Responsibilities

The Framework provides:

- lifecycle management;
- dependency injection;
- API contracts;
- persistence contracts;
- plugin extension points;
- workflow orchestration;
- dashboard composition;
- report generation contracts.

## Non-responsibilities

The Framework must not include:

- school-specific logic;
- political-specific logic;
- healthcare-specific logic;
- festival-specific logic;
- product branding;
- tenant-specific configuration values.
