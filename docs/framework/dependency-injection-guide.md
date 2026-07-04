# Dependency Injection Guide

## Purpose

The DI container allows modules and runtime components to receive dependencies without importing concrete implementations.

## Supported providers

- instance provider;
- singleton provider;
- factory provider.

## Usage

```python
from framework.di import DependencyContainer

container = DependencyContainer()
container.register_singleton("service", lambda: object())
service = container.resolve("service")
```

## Rule

Modules must resolve dependencies through `RuntimeContext` or `DependencyContainer`.
