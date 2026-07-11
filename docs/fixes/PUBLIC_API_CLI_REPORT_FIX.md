# Public API CLI Report Fix

Fixes `tools.public_api_integrity.cli` so it treats
`run_public_api_integrity_checks()` as an `APIReport` object, not as an iterable list.
