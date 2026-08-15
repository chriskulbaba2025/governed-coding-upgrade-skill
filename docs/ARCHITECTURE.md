# Architecture

## Purpose

Governed Coding Upgrade separates universal change governance from repository-specific implementation facts and from the runtime systems that execute AI work.

v2.2 adds a universal adaptation layer so the same governing skill can operate across different languages, frameworks, repository shapes, CI systems, deployment models, agent runtimes, model providers, and AI policy systems.

## Core architecture

```text
Universal GCU protocol
→ Project Discovery
→ Project Adapter
→ Change Tier + Release Intent
→ Agent Roster when useful
→ Execution Control Plane contract when present
→ Test Area Map
→ change-specific governance/evidence
```

The universal protocol owns proof obligations. The Project Adapter owns concrete repository facts. An external execution control plane may own orchestration/model-consumption policy, but it does not own GCU proof or release-readiness claims.

## Control layers

```text
External safety / legal / security constraints
→ Current user authorization and scope
→ Repository governance and product contracts
→ Protected invariants
→ Governed Coding Upgrade skill
→ Project Adapter / legacy Governed Change Profile
→ Change Tier + Release Intent
→ Execution Control Plane authority check when applicable
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

Discovery inspects repository facts before planning. It identifies project kinds, components, build/test systems, persistence, security boundaries, external systems, release mechanics, governance sources, and applicable execution-control authorities.

Unknown material facts remain `UNRESOLVED`.

### Project Adapter

Preferred path:

```text
.governance/PROJECT_ADAPTER.md
```

The adapter maps universal capabilities to the repository's real commands and boundaries.

It may describe one project or multiple monorepo components.

The adapter records a last verified SHA so material repository changes can trigger re-verification instead of silently reusing stale assumptions.

When an execution control plane exists, the adapter records the execution orchestrator, AI policy authority, capability-mapping owner, budget/model-route approval authority, usage-ledger authority, receipt lookup method, independent-context mechanism, and provider-bypass policy. It records authority locations and evidence mechanisms, not provider credentials or duplicate usage transactions.

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

**Release Authority is not model-dispatched.** It remains a human or repository-controlled authorization responsibility. A stronger model cannot approve its own protected operation.

One agent may hold multiple roles on small changes. Stronger separation is preferred or required for higher-risk work.

## Execution Control Plane architecture

Contract:

```text
gcu-execution-control/1.0.0
```

GCU may run directly with a single coding agent or behind a larger governed runtime. The universal boundary is:

```text
GCU
  owns: change scope, Change Tier, Release Intent, proof, challenge, audit
  emits: provider-neutral role/workload/capability context
        ↓

Execution orchestrator
  owns: task/run lifecycle, assignment, approval, escalation, human wait
        ↓

AI policy authority
  owns: provider/model resolution, credentials, budget enforcement,
        authoritative usage accounting, model-policy audit
        ↓

Bounded worker/model execution
        ↓

Durable route/approval/usage receipt references
        ↓

GCU evidence
```

### Capability classes

```text
ECONOMY
STANDARD
ADVANCED
PREMIUM
```

These are provider-neutral minimum capability requests. They are not model IDs and do not grant permission to change providers.

### AI-executable roles

```text
SCOUT
PLANNER
BUILDER
CHALLENGER
VERIFIER
AUDITOR
```

`RELEASE_AUTHORITY` is deliberately excluded.

### Escalation architecture

When the current execution capability is insufficient:

```text
current evidence
→ governed escalation reason
→ durable route request / approval when required
→ policy decision
→ authorized route OR denied/expired state
```

GCU does not silently switch models. Denied/expired escalation does not imply fallback permission.

### Cost architecture

Two cost domains remain separate:

```text
Product external-call cost
  = calls made by the software under test
  = governed by GCU EXTERNAL CALL / COST proof

Execution-resource cost
  = model usage consumed by coding agents
  = governed by the execution control plane
  = GCU stores budget/routing/usage receipt references
```

This prevents product-call budgets from being confused with engineering-agent spend.

### Persistent usage architecture

```text
AI policy authority authoritative usage record
→ durable usage receipt ID
→ orchestrator reference ledger
→ GCU evidence reference
```

GCU does not copy provider billing rows. The receipt must support direct reconciliation using the authoritative system's supported lookup path.

### Independence architecture

Model strength and execution-context independence are separate controls.

```text
stronger model in Builder context ≠ independent audit
```

If an independent Auditor or Challenger is required, the orchestrator must provide a distinct context/assignment and preserve evidence of that separation.

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

When a control plane is present, each AI-executed role may carry provider-neutral capability context and durable route/usage references. Release Authority stays outside the AI execution route.

Dependent work stays sequential. Parallel work is allowed only for genuinely independent, non-overlapping boundaries with explicit ownership and integration responsibility.

## Durable change workspace

For material work, governance state may live under:

```text
.governance/changes/<CHANGE-ID>/
```

with intake, discovery, checklist, agent roster, test map, evidence, and audit records.

This makes repository state the resume/handoff source of truth rather than agent memory.

Execution-control evidence stored here should be compact references: task/run IDs, route decision IDs, approval IDs, budget-envelope references, usage receipt IDs, cost status, and bypass result. Do not duplicate credentials, sensitive prompts, or provider billing transactions.

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

A route approval, budget approval, or other mandatory human-wait state is a stop boundary, not a routine section PASS.

## Balanced verification architecture

Three levels:

1. narrow active test areas;
2. affected boundary/test areas;
3. one terminal full verification after all sections pass.

This reduces cycle time without weakening terminal proof.

## Evidence and validated-object architecture

Strong proof includes exact assertions, persisted state, artifacts/hashes, real-path execution, measured call/task counts, restart proof, contract/object continuity, exact diffs/SHAs, terminal retrieval, execution-control receipts when applicable, machine-gate status, and audit evidence.

For governed boundaries:

```text
assemble complete object
→ validate
→ retain/freeze when applicable
→ persist/transition/render/publish/authorize/consume the validated object
```

## External-call and durable-job architecture

External integrations used by the **software under test** define request/task identity, timeouts, retry classification, budgets, cancellation, recovery/reuse, duplicate-work prevention, and measured counters.

Controlled tests execute below the real adapter/service boundary and avoid unintended live execution where technically feasible.

Asynchronous work persists enough state to recover from a fresh process without reconstructing required input from defaults.

Coding-agent/model execution cost is a separate execution-control-plane responsibility when that control plane exists.

## Terminal and system-readiness architecture

`CHANGE_ONLY` proves the scoped change. `STAGING_READY` proves the governed staging promise. `PRODUCTION_READY` additionally proves the terminal user/business promise and applicable system responsibilities.

A scoped PASS and system readiness are reported separately.

When execution-control evidence is mandatory, unresolved route/approval/budget/usage receipt state prevents a higher readiness claim.

## Monorepo architecture

The adapter may record multiple components. Per change, GCU identifies affected components and shared contracts, then selects narrow tests from those areas plus boundary tests that can be invalidated.

Unrelated expensive whole-workspace tests can remain terminal-only unless repository governance requires earlier execution.

## Correction architecture

When a section, test area, execution-control gate, terminal gate, or audit fails, assign the failure to the owning checklist ID/boundary, correct the smallest governed boundary, rerun direct proof and affected later areas, then rerun terminal verification and audit.

If a production defect escaped earlier green proof, correct both the implementation and the proof system that allowed the false PASS.

If an execution-control defect escaped proof, correct both the adapter/control integration and the approval/receipt/bypass proof that allowed it.