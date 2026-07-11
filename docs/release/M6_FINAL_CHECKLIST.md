# M6 Final Release Checklist

## Repository

- [x] Version set to `0.6.0`
- [x] Working tree expected to be clean before tagging
- [x] No unresolved conflict markers
- [x] No generated cache directories committed
- [x] Release documentation present

## Quality

- [x] Ruff gate enabled
- [x] Full pytest gate enabled
- [x] M6 stabilization tool enabled
- [x] Public package import gate enabled
- [x] Current release version gate enabled

## Architecture

- [x] Event Platform stabilized
- [x] Event Store and Outbox stabilized
- [x] CQRS and Projection Engine stabilized
- [x] Workflow Engine 2.0 stabilized
- [x] Python Workflow SDK stabilized

## Release

- [x] Changelog updated
- [x] Migration notes published
- [x] Public API baseline published
- [x] GitHub Actions final workflow enabled
- [ ] Tag `v0.6.0` created after CI passes
- [ ] GitHub Release published after tag creation
