# Changelog

All notable changes to Governed Coding Upgrade are recorded here.

The project follows semantic versioning for the protocol artifact. The machine-facing skill name remains `governed-coding-upgrade` across compatible releases.

## [1.1.0] — 2026-08-12

### Added

- Production Closure Mode for completing end-to-end production-readiness corrections rather than stopping after repeated partial audits.
- Repository-owned blocker classification: required migrations, tables, durable execution, validators, transport abstractions, endpoints, caches, budget gates, integration harnesses, recovery tests, and negative proofs are implementation work when already required by the governed production contract.
- Dirty-tree continuation rule for preserving and governing active correction work without resetting merely to create a clean baseline.
- Real production path acceptance rule requiring production adapters/services with injected controlled transports or clients.
- Validation-before-transition rule for persistence, lifecycle advancement, rendering, publication, and exposure boundaries.
- Durable execution, restart/recovery, retry classification, paid-task idempotency, and abort-propagation proof requirements when applicable.
- Keep-going production-closure correction loop until PASS or a genuine external blocker remains.
- Reusable `templates/PRODUCTION_CLOSURE_TEMPLATE.md`.

### Changed

- Human-visible release name is now **Governed Coding Upgrade v1.1.0 — Production Closure**.
- The machine-facing skill identifier remains `governed-coding-upgrade` for backward compatibility.
- Blocked protocol now distinguishes genuine external/governance blockers from repository-owned implementation requirements.
- Global invocation rule now routes production-readiness completion requests into Production Closure Mode.
- Package validation now checks the production-closure template and version consistency across release metadata.
- Repository descriptor now reflects public visibility and the production-closure capability.

## [1.0.0] — 2026-08-08

### Added

- Universal governed coding-upgrade execution skill.
- Mandatory global invocation rule.
- Governed Change Profile project adapter layer.
- Frozen checklist and direct-proof requirements.
- Independent exact-head audit protocol.
- Consolidated correction and re-audit workflow.
- Five-area semantic quality scorecard.
- Repository adoption, architecture, and governance documentation.
- Reusable governance templates.
- Repository package integrity validation and GitHub Actions workflow.
