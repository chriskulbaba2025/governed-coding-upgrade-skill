# Architecture

## Purpose

Governed Coding Upgrade separates universal change governance from repository-specific implementation facts.

v2.2 adds a universal adaptation layer so the same governing skill can operate across different languages, frameworks, repository shapes, CI systems, deployment models, and agent runtimes.

## Core architecture

```text
Universal GCU protocol
→ Project Discovery
→ Project Adapter
→ Change Tier + Release Intent
→ Agent Roster when useful
→ Test Area Map
→ change-specific governance/evidence
```

The universal protocol owns proof obligations. The Project Adapter owns concrete repository facts.

## Control layers

```text
External safety / legal / security constraints
→ Current user authorization and scope
→ Repository governance and product contracts
→ Protected invariants
→ Governed Coding Upgrade skill
→ Project Adapter / legacy Governed Change Profile
→ Change Tier + Release Intent
→ Production Spine + Producer/Contract/Consumer map when applicable
→ Acceptance contract freeze + false-PASS scan
→ Frozen checklist + Test Area Map
→ Sequential Evidence Gates
→ Challenger gate
→ Balanced verification
→ Cross-section review
→ Terminal-path gate
→ Full-system readiness gate when PRODUCTION_READY
→ Terminal machine release gate
→ Exact-head audit
→ Release authority
```

A lower layer cannot silently override a higher layer.

## Universal adaptation layer

### Project Discovery

Discovery inspects repository facts before planning. It identifies project kinds, components, build/test systems, persistence, security boundaries, external systems, release mechanics, and governance sources.

Unknown material facts remain `UNRESOLVED`.

### Project Adapter

Preferred path:

```text
.governance/PROJECT_ADAPTER.md
```

The adapter maps universal capabilities to the repository's real commands and boundaries.

It may describe one project or multiple monorepo components.

The adapter records a last verified SHA so material repository changes can trigger re-verification instead of silently reusing stale assumptions.

## Change Tier architecture

Change Tier scales proof depth without weakening required proof.

- `T1_LOCAL` — local behavior.
- `T2_BOUNDARY` — contracts/interfaces/data/auth boundaries.
- `T3_SYSTEM` — cross-boundary/persistence/async/provider/security/end-to-end behavior.
- `T4_RELEASE` — staging/production readiness and protected release gates.

Release Intent remains separate because complexity and readiness claim are different questions.

## Agent architecture

GCU roles are vendor-neutral responsibility boundaries:

### Scout

Read-only discovery and adapter verification by default.

### Planner

Freezes scope, checklist, acceptance, agent roster, and test areas.

### Builder

Implements only governed sections.

### Challenger

Attempts to falsify assumptions and proof before terminal acceptance.

### Verifier

Executes active test areas and records direct evidence.

### Auditor

Inspects the exact candidate head. If the Builder performs the audit in the same context, the result is `SELF_AUDIT`, not independent.

### Release Authority

Provides protected merge/deploy/release authorization required by governance.

One agent may hold multiple roles on small changes. Stronger separation is preferred or required for higher-risk work.

## Test Area architecture

Universal test areas are logical proof lanes, not required folders or frameworks:

```text
STRUCTURE
UNIT
CONTRACT
INTEGRATION
END_TO_END / ACCEPTANCE
DATA / MIGRATION
SECURITY / PRIVACY
RELIABILITY / RECOVERY
EXTERNAL CALL / COST
PERFORMANCE / RESOURCE
COMPATIBILITY
RELEASE / DEPLOYMENT
```

The Project Adapter maps each area to stable repository commands where available. The per-change Test Area Map activates only relevant areas.

`N/A` requires a reason. Missing knowledge is `UNRESOLVED`.

## Runtime orchestration

Recommended high-level flow:

```text
Scout
→ Planner
→ Builder(section)
→ Verifier(section)
→ repeat
→ Challenger
→ Terminal Verifier
→ Auditor
→ Release Authority when required
```

Dependent work stays sequential. Parallel work is allowed only for genuinely independent, non-overlapping boundaries with explicit ownership and integration responsibility.

## Durable change workspace

For material work, governance state may live under:

```text
.governance/changes/<CHANGE-ID>/
```

with intake, discovery, checklist, agent roster, test map, evidence, and audit records.

This makes repository state the resume/handoff source of truth rather than agent memory.

## Production Spine architecture

The Production Spine prevents isolated component PASS from being mistaken for end-to-end correctness.

```text
real entry
→ auth/validation when applicable
→ service/application boundary
→ persistence/durable state
→ jobs/external services when applicable
→ normalization/contracts
→ decision/transformation
→ rendering/publication/delivery
→ terminal retrieval/outcome
```

Every material handoff is mapped as Producer → Contract → Consumer with state/artifact, validation point, failure behavior, authorization/tenant implication, and direct proof.

## Acceptance architecture

Acceptance is designed before implementation for changes that require real-path proof.

The frozen acceptance record names:

- real project/production modules executed;
- controlled dependency seam;
- production contracts/validators;
- persisted state/artifacts inspected;
- positive terminal assertion;
- negative/fail-closed assertion;
- prohibited later effects;
- external-call ceiling;
- exact command.

The false-PASS scan rejects proof that bypasses the boundary being claimed.

## Sequential evidence architecture

```text
inspect
→ define proof
→ reproduce failure when safe/feasible
→ implement complete section
→ narrow verify
→ section audit
→ PASS
→ next section
```

A failed section is corrected before dependent work proceeds.

## Balanced verification architecture

Three levels:

1. narrow active test areas;
2. affected boundary/test areas;
3. one terminal full verification after all sections pass.

This reduces cycle time without weakening terminal proof.

## Evidence and validated-object architecture

Strong proof includes exact assertions, persisted state, artifacts/hashes, real-path execution, measured call/task counts, restart proof, contract/object continuity, exact diffs/SHAs, terminal retrieval, machine-gate status, and audit evidence.

For governed boundaries:

```text
assemble complete object
→ validate
→ retain/freeze when applicable
→ persist/transition/render/publish/authorize/consume the validated object
```

## External-call and durable-job architecture

External integrations define request/task identity, timeouts, retry classification, budgets, cancellation, recovery/reuse, duplicate-work prevention, and measured counters.

Controlled tests execute below the real adapter/service boundary and avoid unintended live execution where technically feasible.

Asynchronous work persists enough state to recover from a fresh process without reconstructing required input from defaults.

## Terminal and system-readiness architecture

`CHANGE_ONLY` proves the scoped change. `STAGING_READY` proves the governed staging promise. `PRODUCTION_READY` additionally proves the terminal user/business promise and applicable system responsibilities.

A scoped PASS and system readiness are reported separately.

## Monorepo architecture

The adapter may record multiple components. Per change, GCU identifies affected components and shared contracts, then selects narrow tests from those areas plus boundary tests that can be invalidated.

Unrelated expensive whole-workspace tests can remain terminal-only unless repository governance requires earlier execution.

## Correction architecture

When a section, test area, terminal gate, or audit fails, assign the failure to the owning checklist ID/boundary, correct the smallest governed boundary, rerun direct proof and affected later areas, then rerun terminal verification and audit.

If a production defect escaped earlier green proof, correct both the implementation and the proof system that allowed the false PASS.
