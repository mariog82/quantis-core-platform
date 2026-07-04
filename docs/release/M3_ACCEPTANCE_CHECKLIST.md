# M3 Acceptance Checklist

## Tests

- [ ] `ruff check .`
- [ ] `python -m pytest tests/core tests/framework tests/modules`
- [ ] `python -m pytest tests/modules/integration`
- [ ] `python -m pytest tests/modules/stabilization`

## Release

- [ ] VERSION updated to `0.3.0-beta.1`
- [ ] CHANGELOG updated
- [ ] ROADMAP updated
- [ ] M3 release notes added
- [ ] M3 beta freeze document added
