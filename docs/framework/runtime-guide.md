# Runtime Kernel Guide

## Main components

- `RuntimeKernel`
- `RuntimeManager`
- `ModuleRegistry`
- `ModuleLifecycleManager`
- `DependencyGraph`
- `RuntimeContext`

## Runtime flow

```text
boot()
initialize()
start()
stop()
shutdown()
```

## Module lifecycle

```text
REGISTERED
INITIALIZED
READY
RUNNING
STOPPING
STOPPED
```

## Usage

```python
from framework.runtime import RuntimeKernel, RuntimeManager

manager = RuntimeManager()
kernel = RuntimeKernel(manager)
kernel.boot()
kernel.initialize()
kernel.start()
```
