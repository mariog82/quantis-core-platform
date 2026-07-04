# Plugin Runtime Guide

## Purpose

Plugins extend framework behavior through declared extension points.

## Components

- `PluginRuntime`
- `PluginRegistry`
- `PluginLifecycleManager`
- `ExtensionPointRegistry`
- `ExtensionPoint`

## Lifecycle

```text
install
enable
disable
```

## Rule

Plugins must not bypass Core, Framework contracts or Runtime lifecycle.
