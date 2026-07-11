# BPMN Layer Architecture

```text
BPMN XML
   ↓
BPMNValidator
   ↓
SimpleBPMNParser
   ↓
WorkflowDefinition
   ↓
WorkflowRegistry

WorkflowDefinition
   ↓
BPMNExporter
   ↓
BPMN XML
```
