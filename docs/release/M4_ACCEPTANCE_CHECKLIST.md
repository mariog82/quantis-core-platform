# M4 Acceptance Checklist

## Code

- [ ] Licensing Service available
- [ ] Subscription Service available
- [ ] Billing Service available
- [ ] Provisioning Service available
- [ ] Compliance Service available
- [ ] EnterpriseServiceRegistry available

## Tests

- [ ] `ruff check .`
- [ ] `python -m pytest tests/core`
- [ ] `python -m pytest tests/framework`
- [ ] `python -m pytest tests/modules`
- [ ] `python -m pytest tests/services`
- [ ] `python -m pytest tests/services/integration`
- [ ] `python -m pytest tests/services/stabilization`

## Documentation

- [ ] Enterprise Services README
- [ ] Architecture overview
- [ ] Licensing guide
- [ ] Subscription guide
- [ ] Billing guide
- [ ] Provisioning guide
- [ ] Compliance guide
- [ ] Service composition guide
- [ ] Testing guide
- [ ] Public API baseline
- [ ] M4 summary

## Release

- [ ] VERSION updated
- [ ] ROADMAP updated
- [ ] CHANGELOG updated
- [ ] Release notes added
- [ ] Beta freeze document added
- [ ] Public API baseline added
