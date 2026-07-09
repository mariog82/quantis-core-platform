# M5.1 Beta Freeze Checklist

Before merge:

- [ ] `ruff check .`
- [ ] `python -m pytest --cache-clear --import-mode=importlib`
- [ ] `python -m tools.repository_recovery.cli`
- [ ] `python -m tools.repository_integrity.cli`
- [ ] `python -m tools.test_integrity.cli`
- [ ] `python -m tools.public_api_integrity.cli`
- [ ] `python -m tools.ci_stabilization.cli`
- [ ] `python -m tools.release_manager.cli`
- [ ] `python -m tools.repository_audit.cli`

After merge into `develop`:

- [ ] tag `v0.5.1-beta.1`
- [ ] push tag
- [ ] create `support/0.5.x`
- [ ] start `feature/m6-pr1-event-bus-core`
