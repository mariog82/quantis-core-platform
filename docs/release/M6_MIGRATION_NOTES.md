# M6 Migration Notes

## From `0.6.0-rc.1` to `0.6.0`

No intentional public API breaking changes are introduced.

Required actions:

1. Replace the version value with `0.6.0`.
2. Run the M6 stabilization tool.
3. Run Ruff and the full test suite.
4. Confirm that historical version tests do not assert the current `VERSION` file.
5. Keep only `tests/release/current` responsible for the active release version.
6. Commit generated reports only when required by repository policy.

## Historical version gates

Historical milestones must test their own release documents or frozen fixtures.
They must not assert that the repository's current `VERSION` still equals an old
beta or release-candidate value.
