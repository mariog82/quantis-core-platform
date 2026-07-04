# Module Development Guide

## Required structure

```text
modules/<module_name>/
  __init__.py
  module.py
```

## Required class

Each module must implement a `BaseModule` subclass with a `ModuleManifest`.

## Lifecycle

Modules are registered and started by `RuntimeKernel`.
