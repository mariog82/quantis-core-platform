# Workflow Runtime Guide

## Purpose

Workflows compose reusable steps into executable processes.

## Components

- `Workflow`
- `WorkflowStep`
- `WorkflowContext`
- `WorkflowExecution`
- `WorkflowRegistry`
- `WorkflowEngine`

## Usage

```python
from framework.workflow import Workflow, WorkflowId, WorkflowStep

workflow = Workflow(id=WorkflowId(), name="demo")
workflow.add_step(WorkflowStep(name="step", handler=lambda context: context))
```
