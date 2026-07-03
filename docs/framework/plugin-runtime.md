# M2 PR6 — Plugin Runtime

## Purpose

Introduce the first provider-neutral Plugin Runtime for Quantis Core Platform.

## Components

- PluginRegistry
- PluginLifecycleManager
- PluginRuntime
- ExtensionPoint
- ExtensionPointRegistry

## Rule

Plugins extend the Framework through declared extension points. They must not bypass Runtime, Core or Framework contracts.
