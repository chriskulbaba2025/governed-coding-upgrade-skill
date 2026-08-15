# Changelog

All notable Governed Coding Upgrade releases are recorded here. The machine-facing skill name remains `governed-coding-upgrade`.

## [2.2.0] — 2026-08-14

### Added

- Project Discovery before planning so repository facts are inspected rather than assumed.
- Universal Project Adapter with independent adapter schema version `1.0.0`.
- Change Tiers: `T1_LOCAL`, `T2_BOUNDARY`, `T3_SYSTEM`, and `T4_RELEASE`.
- Vendor-neutral agent orchestration roles: Scout, Planner, Builder, Challenger, Verifier, Auditor, and Release Authority.
- Truthful `SELF_AUDIT` state when the Builder and Auditor are not independent.
- Execution-control contract `gcu-execution-control/1.0.0` for provider-neutral capability requests, durable escalation, budget-envelope references, usage receipts, and control-plane authority separation.
- Explicit separation between product external-call cost and coding-agent execution-resource cost.
- Explicit rule that Release Authority is human/repository controlled and cannot be model-dispatched.
- Universal Test Area Map covering structure, unit, contract, integration, acceptance, data/migration, security/privacy, reliability/recovery, external-call/cost, performance/resource, compatibility, and release/deployment proof.
- Durable change-workspace template for interrupted sessions and multi-agent handoff.
- Monorepo/multi-component adaptation and affected-component selection rules.
- Challenger gate for T2+ work to actively falsify assumptions and proof before terminal acceptance.
- Universal project model, agent-orchestration guide, execution-control-plane guide, test-area guide, Project Adapter template, agent roster template, Test Area Map template, and change workspace template.

### Changed

- Human-visible release name: **Governed Coding Upgrade v2.2.0 — Universal Project Orchestration**.
- The governing lifecycle now includes Project Discovery / Adapter Check, Change Tier, optional Agent Roster, Execution Control Plane Check when present, Test Area Map, and Challenger gate.
- GCU remains provider/model/billing-system agnostic; concrete routing, credentials, provider pricing, and authoritative execution usage stay outside the skill.
- Final reports may carry orchestrator task/run, routing-decision, approval, budget-envelope, usage-receipt, execution-cost, and provider-bypass evidence without duplicating the authoritative external ledger.
- Testing is expressed as capability-based proof areas instead of assumed folder/framework layouts.
- The legacy Governed Change Profile remains compatible while new installations prefer `.governance/PROJECT_ADAPTER.md`.
- Audit language now distinguishes independent exact-head audit from same-context `SELF_AUDIT`; a stronger model in the same context does not create independence.
- Generalization now explicitly covers monorepos, multi-component repositories, multiple project kinds, and integration with external execution orchestrators / AI policy authorities.

### Retained from v2.1.0

- Release intent: `CHANGE_ONLY`, `STAGING_READY`, `PRODUCTION_READY`.
- Production Spine gate and Producer → Contract → Consumer mapping.
- Acceptance-contract freeze and false-PASS scan.
- Sequential Evidence Gates and balanced verification.
- Single validated-object and evidence-preservation rules.
- External-call and durable-job contracts.
- Terminal-path and full-system production-readiness gates.
- Machine release gate, exact-head audit, Governance Hold, Production Closure, and escaped-proof regression.

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