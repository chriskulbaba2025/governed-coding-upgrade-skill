# Changelog

All notable changes to Governed Coding Upgrade are recorded here.

The project follows semantic versioning for the protocol artifact. The machine-facing skill name remains `governed-coding-upgrade` across compatible releases.

## [1.2.0] — 2026-08-12

### Added

- Sequential Evidence Gates for multi-section governed changes and Production Closure work: inspect → define proof → implement → narrow verify → section audit → automatically continue on PASS.
- Balanced machine-verification cadence with narrow section checks, affected integration checks only when needed, and one complete terminal verification after all sections pass.
- Terminal machine release-gate contract. Agent prose, confidence, local substitutes, or environmental explanations cannot override a failed required gate.
- `CODE VERIFIED / GOVERNANCE HOLD` state for code that passes controlled local verification while a mandatory external release condition such as exact-head CI is temporarily unavailable.
- Controlled credential-isolation rule for provider/LLM acceptance: inject controlled transports below production adapters, isolate real credentials where feasible, fail unexpected live execution, and measure call counters rather than hardcoding PASS.
- Interrupted-agent/API resume rule that recovers from repository/checklist evidence and continues from the first unproven section rather than restarting completed valid work.
- Cross-section integration review before terminal verification.
- Reusable `templates/MACHINE_RELEASE_GATE_TEMPLATE.md`.

### Changed

- Human-visible release name is now **Governed Coding Upgrade v1.2.0 — Sequential Evidence Gates**.
- Production Closure Mode now executes ordered closure sections sequentially and automatically continues after direct section PASS evidence.
- Verification guidance now explicitly balances cycle time against proof depth instead of requiring full regression after every section.
- Exact-head CI that is mandatory but externally unavailable now blocks release-ready status without being mislabeled as a repository code defect.
- Global invocation rule now enforces sequential sections, credential-safe controlled testing, interruption resume, balanced verification, and the terminal machine release gate.
- Governed Change Profile now records affected-integration verification, controlled-test credential policy, and terminal machine-gate command.
- Independent audit and final-report templates now distinguish code verification, governance hold, and release readiness.
- Package validation now verifies the new v1.2.0 controls and machine release-gate template.

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

- Human-visible release name became **Governed Coding Upgrade v1.1.0 — Production Closure**.
- The machine-facing skill identifier remained `governed-coding-upgrade` for backward compatibility.
- Blocked protocol distinguished genuine external/governance blockers from repository-owned implementation requirements.
- Global invocation rule routed production-readiness completion requests into Production Closure Mode.
- Package validation checked the production-closure template and version consistency across release metadata.

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
