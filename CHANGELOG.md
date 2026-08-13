# Changelog

All notable Governed Coding Upgrade releases are recorded here. The machine-facing skill name remains `governed-coding-upgrade`.

## [2.1.0] — 2026-08-13

### Added

- Release intent: `CHANGE_ONLY`, `STAGING_READY`, `PRODUCTION_READY`.
- Production Spine gate and Producer → Contract → Consumer mapping.
- Acceptance-contract freeze and explicit false-PASS scan.
- Single validated-object and evidence-preservation rules.
- External-call and durable-job contracts.
- Terminal-path and full-system production-readiness gates.
- Change-PASS versus system-readiness separation.
- Escaped-proof regression rule.
- New-application vertical-spine rule.
- Production-spine and acceptance-contract templates.

### Retained from v1.2.0

- Sequential Evidence Gates.
- Dirty-tree continuation and interrupted-session resume.
- Balanced verification cadence.
- Production Closure Mode.
- Repository-owned-work classification.
- Terminal machine release gate and Governance Hold.

### Changed

- Human-visible release name: **Governed Coding Upgrade v2.1.0 — Production Spine + Sequential Evidence**.
- Repository documentation, templates, PR governance, scorecard, metadata, and package validation now align with v2.1.
- A scoped PASS no longer implies a production-ready system; the declared release intent controls the required proof depth.

## [1.2.0] — 2026-08-12

- Added Sequential Evidence Gates, balanced verification, terminal machine release gating, Governance Hold, controlled external-call isolation, interruption resume, and cross-section review.

## [1.1.0] — 2026-08-12

- Added Production Closure Mode, repository-owned-work classification, dirty-tree continuation, real-path acceptance, validation-before-transition, and durability/recovery proof.

## [1.0.0] — 2026-08-08

- Initial universal governed coding-upgrade protocol, global invocation rule, change profile, frozen checklist, exact-head audit, correction workflow, scorecard, templates, validator, and CI.
