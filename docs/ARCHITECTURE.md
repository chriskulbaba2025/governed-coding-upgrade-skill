# Architecture

## Purpose

Governed Coding Upgrade (GCU) separates universal software-change governance from repository-specific implementation facts, vendor-specific agent interfaces, execution-control systems, and protected release authority.

v2.3 adds **Surgical Determinacy** without replacing the v2.2 production-correctness architecture. The protocol now governs both sides of a change:

```text
BEFORE IMPLEMENTATION
preserve requirement
→ prove change hypothesis
→ freeze smallest causally justified architectural surface
→ protect everything else

AFTER IMPLEMENTATION
prove real behavior
→ prove every material changed boundary was necessary
→ inspect exact candidate head
→ verify readiness and authorization truthfully
```

## Core architecture

```text
Authoritative GCU protocol: SKILL.md
        │
        ├── persistent invocation: GLOBAL_AGENT_RULE.md
        │       └── vendor adapters such as GLOBAL_CLAUDE_RULE.md
        │
        ├── repository truth: Project Discovery + Project Adapter
        │
        ├── per-change truth: Requirement Preservation + Surgical Change Contract
        │
        ├── proof selection: Change Tier + Release Intent + Test Area Map
        │
        ├── production correctness: Production Spine + contracts + acceptance
        │
        ├── execution: bounded Builder / optional role orchestration
        │
        ├── post-change necessity: Causal Necessity Audit
        │
        └── closure: machine gate + exact-head / Surgical Determinacy Audit
```

The universal protocol owns governance semantics. The Project Adapter owns repository facts. Vendor adapters own invocation mechanics. An external execution control plane may own AI execution policy. Release Authority owns protected release authorization.

No lower layer silently acquires authority owned by a higher layer.

## Control layers

```text
External safety / legal / security constraints
→ Current user authorization and requested outcome
→ Repository governance and product contracts
→ Protected invariants
→ Governed Coding Upgrade protocol
→ Project Adapter / legacy Governed Change Profile
→ Requirement Preservation
→ Surgical Change Determinacy Gate
→ Change Tier + Release Intent
→ Execution Control Plane authority check when applicable
→ Production Spine + Producer/Contract/Consumer map when applicable
→ Acceptance contract freeze + false-PASS scan
→ FROZEN CHECKLIST + Test Area Map
→ Sequential Evidence Gates
→ Causal Necessity Audit
→ Challenger gate
→ Balanced verification + Cross-section review
→ Terminal-path gate
→ Full-system readiness gate when PRODUCTION_READY
→ Terminal machine release gate
→ Independent exact-head audit + Surgical Determinacy Audit
→ Release Authority
```

## Surgical Determinacy architecture

Surgical Determinacy is intentionally implemented as **one pre-change gate and one post-change audit**, not a chain of overlapping approvals.

### Requirement Preservation

Before choosing implementation, preserve:

```text
original requested outcome
governed implementation-independent interpretation
explicit exclusions / non-goals
observable acceptance condition
```

This prevents the governance system from becoming precise around the wrong interpretation.

### Surgical Change Determinacy Gate

The pre-change gate freezes:

```text
required outcome
direct evidence
change hypothesis + predicted effect
causal boundary
REQUIRED / EXPECTED / PROHIBITED change surface
protected surface
structural change budget
acceptance proof
scope-expansion conditions
```

Material causal facts cannot remain `UNRESOLVED` at implementation start.

The structural budget measures architectural surface—modules, contracts, schemas, persistence, dependencies, integrations, configuration, abstractions, migrations—not arbitrary lines changed or diff size.

### Discovery does not create authorization

Discovery may reveal technical debt, a second bug, an outdated dependency, a naming issue, a security-hardening opportunity, or a desirable refactor.

Those findings are evidence, not permission.

A new boundary enters the active change only after direct evidence establishes causal necessity and the determinacy gate is reopened **before** that new boundary is modified.

### Causal Necessity Audit

After implementation, every material changed production boundary maps to:

```text
Requirement ID
→ changed boundary
→ why the requirement remains incorrect if unchanged
→ direct evidence
```

Unjustified changes are removed or separately authorized. Selective revert testing is used where causal necessity cannot otherwise be established confidently.

### Surgical Determinacy Audit

At exact candidate head, the audit confirms:

```text
requirement preserved
change hypothesis validated
required outcome achieved
every material changed boundary causally justified
protected surfaces preserved
structural change budget respected or formally reopened
incidental findings excluded unless causally authorized
unauthorized scope expansion = zero
unjustified architecture/contract/dependency change = zero
```

This closes the loop between the frozen pre-change model and the actual final diff.

## Universal adaptation architecture

### Project Discovery

Discovery inspects repository facts before planning. Unknown material facts remain `UNRESOLVED`.

### Project Adapter

Preferred path:

```text
.governance/PROJECT_ADAPTER.md
```

The adapter maps universal capabilities to real repository commands and boundaries. It may describe one project or multiple monorepo components and records a last verified SHA so stale assumptions can be detected.

The adapter may also record execution orchestrator, AI policy authority, capability-mapping owner, budget/model-route approval authority, usage-ledger authority, receipt lookup method, independent-context mechanism, and provider-bypass policy. It records authority locations and evidence mechanisms, not provider credentials or duplicate usage transactions.

## Change Tier and Release Intent architecture

Change Tier scales governance depth:

- `T1_LOCAL` — local behavior;
- `T2_BOUNDARY` — contracts/interfaces/data/auth/dependency boundaries;
- `T3_SYSTEM` — cross-boundary/persistence/async/provider/security/end-to-end behavior;
- `T4_RELEASE` — staging/production readiness and protected release gates.

Release Intent remains separate:

- `CHANGE_ONLY`;
- `STAGING_READY`;
- `PRODUCTION_READY`.

Complexity and readiness claim are different questions. Surgical causality applies at every tier.

## Agent architecture

GCU roles are vendor-neutral responsibility boundaries:

- **Scout** — read-only discovery and adapter verification;
- **Planner** — preserves requirements and freezes determinacy, scope, checklist, acceptance, and Test Areas;
- **Builder** — implements only the governed bounded change;
- **Challenger** — attempts to falsify requirement interpretation, causality, scope, proof, and readiness;
- **Verifier** — executes active Test Areas and records direct evidence;
- **Auditor** — inspects the exact candidate head;
- **Release Authority** — provides protected merge/deploy/release authorization.

If Builder and Auditor share a context, the result is `SELF_AUDIT`, not independent. Changing model capability inside the same Builder context does not create independence.

**Release Authority is not model-dispatched.** It remains a human or repository-controlled authorization responsibility. A model cannot approve its own protected operation.

## LLM-agnostic architecture

GCU separates protocol semantics from installation mechanics:

```text
SKILL.md
  canonical protocol

GLOBAL_AGENT_RULE.md
  canonical persistent invocation obligation

vendor adapter
  maps that obligation into Claude Code, ChatGPT, Codex-style agents,
  local harnesses, multi-agent runtimes, or other execution surfaces

PROJECT_ADAPTER.md
  maps universal GCU requirements to repository-specific truth
```

Vendor-specific adapters may change **how the protocol is invoked**, not the protocol itself.

This allows the same requirement, change contract, evidence, and audit semantics to survive model or tool changes.

## Execution Control Plane architecture

GCU may run inside a larger execution platform. Authority remains separated:

```text
GCU
→ emits provider-neutral role/workload/capability context

Execution orchestrator
→ owns task/run state, approvals, escalation, human-wait lifecycle

AI policy authority
→ owns provider/model resolution, credentials, budget enforcement,
   authoritative usage accounting and policy decisions

GCU evidence
← retains durable task/run/routing/approval/budget/usage references
```

Contract:

```text
gcu-execution-control/1.0.0
```

GCU MUST NOT choose a provider or concrete model as an execution side effect, store provider credentials, silently escalate, duplicate the authoritative usage ledger, or model-dispatch Release Authority.

Capability floors are provider-neutral minimums (`ECONOMY`, `STANDARD`, `ADVANCED`, `PREMIUM`), not model aliases.

## Persistent usage architecture

When an execution control plane is present, GCU evidence may retain:

```text
orchestrator task/run refs
routing-decision refs
approval/escalation refs
budget-envelope ref
usage-receipt refs
execution-cost status
provider/model bypass result
```

These are references to authoritative execution evidence. GCU does not copy provider credentials or create a competing billing ledger.

**Execution-resource cost** consumed by coding agents remains separate from `EXTERNAL CALL / COST` evidence produced by the software under test.

## Production correctness architecture

### Production Spine

For cross-boundary production work, trace the real path from entry through auth/validation, service boundaries, persistence/jobs/providers, normalization/decision, rendering/publication/delivery, and terminal retrieval.

### Producer → Contract → Consumer

Every material handoff must preserve required fields/semantics, validate before governed side effects, retain identity where authorization matters, and prevent malformed data from becoming valid-looking defaults.

### Single validated object

Where continuity is governed:

```text
assemble complete object
→ validate complete object
→ retain/freeze validated object where applicable
→ persist/advance/render/publish/authorize/consume that object
```

### Evidence preservation

External/raw evidence follows a provenance-preserving chain through governed artifact/reference, real normalizer, validated contract, canonical persistence, and downstream consumer.

## Proof architecture

### Test Area Map

Proof is capability-based rather than framework-based:

`STRUCTURE`, `UNIT`, `CONTRACT`, `INTEGRATION`, `END_TO_END / ACCEPTANCE`, `DATA / MIGRATION`, `SECURITY / PRIVACY`, `RELIABILITY / RECOVERY`, `EXTERNAL CALL / COST`, `PERFORMANCE / RESOURCE`, `COMPATIBILITY`, and `RELEASE / DEPLOYMENT`.

Only applicable areas activate. Unknown remains `UNRESOLVED`.

### Acceptance architecture

Freeze acceptance before implementation when correctness depends on a real path. Real production/project modules must execute, with controlled dependencies below the boundary being proven.

False-PASS proof—fabricated success, always-valid validators, pre-seeded terminal state, hardcoded call counts, or mocks above the claimed boundary—is rejected.

### Sequential Evidence Gates

Ordered work progresses:

```text
inspect
→ define proof
→ reproduce failure when safe/feasible
→ implement bounded section
→ narrow verify
→ section audit
→ continue only on PASS
```

Later work cannot silently invalidate earlier governed evidence.

### Challenger and terminal architecture

The Challenger attempts to falsify the requirement interpretation, causal model, change budget, proof, negative paths, and readiness claim.

For staging/production claims, terminal proof must show the same governed execution reaches the final user/business result. Intermediate green states do not substitute for terminal proof.

## Release architecture

A scoped change PASS, system readiness, audit state, and release authorization are separate states.

For `PRODUCTION_READY`, applicable persistence, auth/tenant, secrets, contracts, production adapters, durability/recovery, external-call controls, execution-control evidence, canonical artifacts, downstream consumers, terminal delivery/retrieval, observability, rollback, exact-head CI, machine gate, audit, Surgical Determinacy, and release authorization must be proven.

A machine gate evaluates machine-enforceable conditions against the exact candidate head. Agent prose or confidence cannot override it.

If code is verified but a mandatory external condition is unavailable, the truthful state is:

```text
CODE VERIFIED / GOVERNANCE HOLD
```

## Governed learning architecture

When `gcu-learning-memory/1.0.0` is present, approved practices may be recalled as `ADVISORY_ONLY`. Current user instruction, repository authority, the frozen change contract, and current evidence always outrank memory.

A producing run may emit evidence-linked lesson candidates but cannot auto-promote its own candidate into an approved practice.

## Design boundary

v2.3 deliberately stops adding controls after the pre-change determinacy gate and post-change surgical audit.

It does not require:

- per-line causal paperwork;
- arbitrary diff-size limits;
- separate minimality/scope/necessity/drift approval gates;
- mandatory multi-agent execution for small changes;
- mathematical proofs of minimality.

Those would create diminishing returns and process weight without equivalent correctness gains.

The architectural target is therefore:

> **Determine surgically before coding. Prove the real system after coding. Audit that nothing unnecessary entered the exact candidate head.**
