# Modules Architecture Overview

```text
Core
  ↓
Framework
  ↓
Modules
  ↓
Verticals
```

Modules implement reusable business capabilities on top of the Framework.

## Dependency rule

Modules may depend on:

- Core contracts;
- Framework runtime and services;
- other reusable modules, when declared in `ModuleManifest.dependencies`.

Modules must not depend on vertical products.
