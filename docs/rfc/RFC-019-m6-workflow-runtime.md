# RFC-019 — M6 Workflow Runtime

## Goals

- Create workflow instances from registered definitions.
- Resolve executors by step type.
- Execute transitions deterministically.
- Support waiting, failure and completion.
- Guard against non-progressing execution loops.
