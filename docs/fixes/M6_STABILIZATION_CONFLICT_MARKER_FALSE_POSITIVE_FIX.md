# M6 Stabilization Conflict Marker False Positive Fix

The scanner now detects only real Git conflict-marker lines:

- `<<<<<<< ...`
- `=======`
- `>>>>>>> ...`

Marker text embedded in Python strings, tests or generated Markdown reports is ignored.
