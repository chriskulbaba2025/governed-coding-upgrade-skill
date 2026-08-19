---
name: governed-coding-upgrade
description: >-
  LLM-agnostic governed execution, surgical change control, testing, audit, and production-readiness protocol for software changes across project types.
---

# Governed Coding Upgrade Skill v2.3.0 — Surgical Determinacy

**Version:** 2.3.0  
**Machine-facing skill name:** `governed-coding-upgrade`  
**Status:** Governing execution skill

## Governing purpose

Governed Coding Upgrade (GCU) turns intentional software changes into an evidence-based lifecycle without assuming a language, framework, CI provider, cloud, repository shape, coding agent, model provider, or billing system.

v2.3 retains the v2.2 production-correctness, universal Project Orchestration, execution-control, learning-memory, sequential-evidence, terminal-readiness, and exact-head controls. It adds **Surgical Determinacy**: preserve the requested requirement, prove the relevant change hypothesis, freeze the smallest causally justified architectural surface, fail closed on scope expansion, and audit the actual candidate diff for causal necessity.

GCU is LLM-agnostic. Vendor-specific installation files are adapters to this protocol; they do not change its governing semantics.

```text
INTAKE
→ PREFLIGHT
→ PROJECT DISCOVERY / ADAPTER CHECK
→ REQUIREMENT PRESERVATION
→ SURGICAL CHANGE DETERMINACY GATE
→ CHANGE TIER + RELEASE INTENT
→ AGENT / EXECUTION-CONTROL CHECKS when applicable
→ PRODUCTION SPINE / CONTRACT MAP when applicable
→ ACCEPTANCE FREEZE
→ FROZEN CHECKLIST + TEST AREA MAP
→ SEQUENTIAL BUILD / VERIFY
→ CAUSAL NECESSITY AUDIT
→ CHALLENGER / CROSS-SECTION REVIEW
→ TERMINAL-PATH / SYSTEM READINESS when applicable
→ MACHINE GATE
→ INDEPENDENT EXACT-HEAD AUDIT + SURGICAL DETERMINACY AUDIT
→ CORRECT / RE-AUDIT
→ CLOSE
```

The design intentionally uses **one strong pre-change determinacy gate and one strong post-change surgical audit**. Sub-controls provide evidence to those two controls; they are not separate mandatory lifecycle gates.

## 1. Authority and mandatory invocation

Resolve conflicts in this order:

1. platform, safety, legal, privacy, and security constraints;
2. explicit current user instruction and authorization boundaries;
3. repository governance and security rules;
4. product, API, schema, persistence, data, compatibility, and release contracts;
5. protected invariants and reference artifacts;
6. this skill;
7. repository Project Adapter / legacy Governed Change Profile;
8. frozen Surgical Change Contract, FROZEN CHECKLIST, Test Area Map, and acceptance contract;
9. implementation notes.

A lower layer cannot override a higher layer.

Invoke GCU for intentional changes to source, tests, schemas, APIs, dependencies, executable configuration, migrations, persistence, jobs, external integrations, security controls, infrastructure, build/release logic, generated production artifacts, or runtime behavior.

Read-only inspection does not require the full lifecycle unless repository governance says otherwise. Read-only discovery also does not create permission to edit.

No qualifying implementation begins before the applicable preflight, Requirement Preservation, and Surgical Change Determinacy obligations pass.

## 2. Repository preflight, Project Discovery, and Project Adapter

Before editing, verify directly:

```text
repository root
branch
exact starting SHA
working-tree status
remote identity when relevant
active PR when relevant
governing sources
Project Adapter / Governed Change Profile
authorization boundaries
execution orchestrator / AI policy authority when applicable
```

Starting-SHA mismatch is a stop condition. Never discard pre-existing user work without authorization.

### Project Discovery

Inspect only facts relevant to the change, including when applicable:

- repository/workspace/monorepo/component boundaries;
- languages, runtimes, package/build systems;
- applications, services, libraries, CLIs, workers, infrastructure, data pipelines, databases, plugins, generated systems, and other project kinds;
- public interfaces and runtime entry points;
- test frameworks and commands;
- CI/CD, release, rollback, and recovery mechanisms;
- persistence, migrations, queues, caches, artifacts, and background jobs;
- authentication, authorization, tenant/account, privacy, and secret boundaries;
- external providers, paid/side-effecting calls, and controlled-test seams;
- execution orchestrator, AI policy authority, route/usage authority, and independent-context mechanism;
- protected/generated paths and repository-specific governance.

Unknown material facts are `UNRESOLVED`, never guessed or converted to N/A.

### Project Adapter

Preferred path:

```text
.governance/PROJECT_ADAPTER.md
```

Use `templates/PROJECT_ADAPTER_TEMPLATE.md`.

The Project Adapter maps universal GCU capabilities to repository truth: components/roots, build/runtime/test commands, protected/generated paths, persistence/recovery rules, security/privacy/tenant boundaries, external-call policy, execution-control authority, release/CI/rollback methods, terminal promises, repository-specific stop conditions, and last verified SHA.

It may describe a single project or multiple components in a monorepo. If a material fact is stale or unsupported, re-verify it or mark it `UNRESOLVED`.

The legacy `.governance/GOVERNED_CHANGE_PROFILE.md` remains compatible.

### Dirty-tree continuation

When explicitly continuing the same correction, preserve valid existing work. Inspect status/diff, map work to the frozen requirement and checklist, correct in place, and do not reset merely to obtain a clean baseline.

### Interrupted-agent resume

After an agent/API/terminal interruption, resume from repository truth: current branch/HEAD, diff, durable change workspace, frozen Surgical Change Contract, checklist, Test Area Map, and evidence. Preserve valid completed work and continue from the first unproven or failing obligation.

Repository state and recorded evidence outrank agent memory. Durable execution-control task/run/routing/usage references must be preserved rather than reconstructed from conversation.

## 3. Requirement Preservation

Before choosing an implementation, preserve the actual requested outcome.

Record:

```text
Original requested outcome
Faithful governed interpretation
Explicit exclusions / non-goals
Observable acceptance condition
```

The governed interpretation must remain implementation-independent and must not silently add requirements, architecture, cleanup, or adjacent scope.

A precise implementation of the wrong interpretation is a governance failure.

The Challenger later asks whether the result solves the original request or merely the Planner's reformulation.

## 4. Surgical Change Determinacy Gate

The Builder MUST NOT edit governed production code until this gate passes.

Freeze one Surgical Change Contract, preferably from `templates/SURGICAL_CHANGE_CONTRACT_TEMPLATE.md`.

Required fields:

```text
required outcome
direct supporting evidence
change hypothesis + predicted effect
causal boundary
expected change surface
protected surface
structural change budget
acceptance proof
scope-expansion conditions
```

### Change hypothesis

For a defect, state why current behavior differs from required behavior. For an intentional capability upgrade, state which system boundary must change to create the requested result.

Status is exactly one of:

```text
PROVEN
DISPROVEN
UNRESOLVED
```

Do not implement while a material causal fact is `UNRESOLVED`. If the hypothesis is disproven, replace it with a directly supported hypothesis before implementation.

### Expected and protected surface

Freeze:

```text
REQUIRED — modules/contracts/components directly supported as necessary
EXPECTED — symbols/functions when genuinely determinable before implementation
PROHIBITED — unrelated boundaries, contracts, public behavior, and protected paths
```

Do not invent symbol-level precision that evidence does not support. Exact changed symbols are still inspected after implementation.

Everything outside the justified causal chain is protected by default unless the contract explicitly says otherwise.

### Structural change budget

The structural change budget measures architectural surface, not textual size.

Use applicable dimensions such as:

```text
production modules
public contracts
schemas
persistence boundaries
dependencies
external integrations
configuration surfaces
new abstractions
migrations
bounded test surfaces
```

Do **not** use maximum lines changed, arbitrary diff-size limits, maximum function count, or code-golf minimality as proxies for surgicality. A larger causally necessary change can be surgical; a tiny bypass can be unsafe.

### Discovery does not create authorization

A newly discovered defect, cleanup opportunity, refactor, dependency issue, security hardening opportunity, naming problem, duplicate, or adjacent feature does not enter the active change merely because it is useful, nearby, inexpensive, or in a file already being edited.

“Useful,” “related,” “cleaner,” “safer,” and “while we are here” are not causal authorization.

Record incidental findings separately.

### Fail-closed expansion rule

If implementation requires a material boundary outside the frozen contract or exceeds a structural-budget dimension:

```text
STOP
→ do not modify the newly discovered boundary
→ preserve the evidence
→ reopen the Surgical Change Determinacy Gate
→ prove the additional boundary is causally necessary
→ update expected/protected surface, budget, and proof
→ continue only after the gate passes again
```

The discovery means the original determinacy model may have been incomplete; it is not permission to broaden implementation automatically.

## 5. Change Tier, Release Intent, and Agent orchestration

### Change Tier

Declare one:

- `T1_LOCAL` — contained local behavior; no governed external/persistent boundary change.
- `T2_BOUNDARY` — contract, schema, API, public interface, dependency boundary, auth rule, or producer/consumer handoff change.
- `T3_SYSTEM` — cross-boundary, persistence, async, external-provider, security-sensitive, multi-component, or end-to-end behavior.
- `T4_RELEASE` — requested result includes staging/production readiness or protected release gates.

Change Tier controls governance depth. Surgical causal justification applies at every tier; simple T1 work may use a compact record, not a weaker causal standard.

Do not misclassify complex work as T1 to reduce testing.

### Release Intent

Declare exactly one:

- `CHANGE_ONLY`
- `STAGING_READY`
- `PRODUCTION_READY`

Release Intent controls the readiness claim. A green scoped change cannot silently become production readiness.

### Agent orchestration

Roles are responsibilities, not model brands:

- **Scout** — read-only discovery and adapter verification;
- **Planner** — requirement, determinacy, scope, contract, checklist, and test planning;
- **Builder** — bounded implementation;
- **Challenger** — falsifies assumptions, causal scope, proof, and readiness claims;
- **Verifier** — executes active proof areas;
- **Auditor** — inspects the actual candidate head;
- **Release Authority** — controls protected merge/deploy/release authorization.

One context may hold several roles when safe. Do not multiply agents without value.

If Builder and Auditor are the same agent/context, report `SELF_AUDIT`. A stronger or different model in the same Builder context does not create audit independence. Where repository governance requires independent Auditor/Challenger separation, establish a genuinely separate context/assignment.

Parallel agents are allowed only for genuinely independent non-overlapping sections with explicit boundary ownership, shared-contract handling, merge order, and integration ownership.

**Release Authority is not an AI model-execution role.** A human or repository-controlled authority owns it. An execution-control adapter MUST reject attempts to model-dispatch `RELEASE_AUTHORITY` as permission for a model to authorize its own protected operation.

## 6. Execution control plane integration and governed learning

### Execution control plane integration

When present, use:

```text
gcu-execution-control/1.0.0
```

GCU governs the change lifecycle. It does not become a second model router, credential broker, billing system, or orchestration ledger.

Provider-neutral execution context may include change/repository/SHA, Change Tier, Release Intent, role, workload class, capability floor, independence requirement, section/gate, authorization boundary, budget-envelope reference, and escalation reason.

AI-executable roles are limited to `SCOUT`, `PLANNER`, `BUILDER`, `CHALLENGER`, `VERIFIER`, and `AUDITOR`. Capability floors are `ECONOMY`, `STANDARD`, `ADVANCED`, and `PREMIUM` and are minimum capability requests, not provider/model aliases.

Rules:

- GCU MUST NOT select a concrete provider/model as an execution side effect.
- GCU MUST NOT store provider credentials.
- GCU MUST NOT silently escalate to a more capable or more expensive model.
- GCU MUST NOT maintain a second authoritative execution-usage/billing ledger.
- An external orchestrator may own task/run/approval/escalation state.
- An AI policy authority may own provider/model resolution, credentials, budget enforcement, and authoritative usage accounting.
- Returned task/run, route, approval, budget-envelope, and usage-receipt references become governed evidence when applicable.
- Required independent Auditor/Challenger separation remains a context requirement, not a model-capability claim.

When capability is insufficient, record an escalation request rather than silently switching models. Allowed reasons remain `CAPABILITY_INSUFFICIENT`, `INDEPENDENCE_REQUIRED`, `CONTEXT_LIMIT`, `REPEATED_PROOF_FAILURE`, `POLICY_REQUIREMENT`, and `MATERIAL_AMBIGUITY`.

A denied or expired route/approval is not permission to fallback.

#### Execution cost versus product external-call cost

Keep two domains separate:

1. **Product external-call cost** — calls made by the software under test; governed by the External-call contract and `EXTERNAL CALL / COST` Test Area.
2. **Execution-resource cost** — model usage consumed by coding agents; authoritative pricing/enforcement/accounting belongs to the execution control plane when present.

Hardcoded execution-cost claims are not evidence. Preserve durable references needed for reconciliation without duplicating an authoritative provider billing transaction.

### Governed learning memory

When `gcu-learning-memory/1.0.0` is available, preflight may recall only active approved practices relevant to the repository/component. Recalled practices are `ADVISORY_ONLY` and never outrank current user instruction, repository authority, the frozen Surgical Change Contract, or current evidence.

After a truthful terminal state, a run may emit evidence-linked lesson candidates. A failed/blocked run may produce a known-failure candidate, but not a positive best-practice claim merely because an implementation was attempted.

The producing GCU run MUST NOT auto-promote its own candidate into an `ApprovedPractice`; promotion requires separate validation and explicit approval.

## 7. Governed workspace, FROZEN CHECKLIST, and Test Area Map

For material or interruptible work, prefer:

```text
.governance/changes/<CHANGE-ID>/
  INTAKE.md
  DISCOVERY.md
  SURGICAL_CHANGE.md
  CHECKLIST.md
  AGENT_ROSTER.md
  TEST_AREA_MAP.md
  EVIDENCE.md
  AUDIT.md
  LEARNING.md when applicable
```

Small T1 changes may use a reduced package when repository governance permits, but Requirement Preservation and Surgical Determinacy still apply.

When execution-control receipts exist, retain only durable references and safe policy status needed for reconciliation. Do not copy provider credentials, sensitive prompts, secrets, or duplicate billing transactions into GCU evidence.

### FROZEN CHECKLIST

Every checklist item has a stable ID, one observable requirement, exact boundary, positive proof, negative proof when applicable, real-path acceptance proof when applicable, protected invariant, exact failure result, final evidence, and binary status.

No aspirational requirements, hidden requirements, prose-only proof, or `A OR B` result when one governed result is required.

### Universal Test Area Map

Select only applicable areas and record `ACTIVE`, justified `N/A`, or `UNRESOLVED` plus the real command/mechanism and required positive/negative proof:

- `STRUCTURE`
- `UNIT`
- `CONTRACT`
- `INTEGRATION`
- `END_TO_END / ACCEPTANCE`
- `DATA / MIGRATION`
- `SECURITY / PRIVACY`
- `RELIABILITY / RECOVERY`
- `EXTERNAL CALL / COST`
- `PERFORMANCE / RESOURCE`
- `COMPATIBILITY`
- `RELEASE / DEPLOYMENT`

A missing command is not automatically N/A.

## 8. Production correctness contracts

### Production Spine gate

For T3/T4 cross-boundary production work, trace the real path before implementation:

```text
entry
→ authentication/authorization when applicable
→ validation
→ application/service boundary
→ persistence/durable state
→ job/orchestration when applicable
→ external service/model when applicable
→ normalization/contract validation
→ decision/transformation
→ rendering/publication/delivery
→ final retrieval or business-visible terminal result
```

For each hop record production module, input/output contract, state/artifact, failure behavior, retry/idempotency effect, tenant/account implication, and direct proof. Do not implement while a material required spine hop is unresolved.

### Producer → Contract → Consumer map

For each material handoff prove that the producer emits what the consumer requires, validation occurs before governed persistence/transition/rendering/publication/authorization/exposure/irreversible side effects, the consumer uses the validated state when continuity matters, defaults do not convert malformed usable data into valid-looking empty data, and authorization-relevant identity remains attached.

An escaped producer/consumer defect requires correction of both implementation and proof map.

### Single validated-object rule

For governed persistence, lifecycle, rendering, publication, authorization, delivery, or exposure:

```text
assemble complete object
→ validate complete object
→ retain/freeze validated object when applicable
→ persist/advance/render/publish/authorize/consume that validated object
```

Do not validate a partial object and add required fields afterward. Do not validate object A and consume an independently reconstructed object B where continuity is governed. Malformed usable states fail closed.

### Evidence preservation

When raw/external evidence drives decisions, preserve the governed chain:

```text
raw response/reference
→ governed raw artifact/reference
→ real normalizer/adapter
→ validated evidence contract
→ persisted canonical evidence
→ downstream consumer
```

Prove provenance, field preservation, validation, canonical persistence, governed consumer loading, and that replay/cache/fallback paths cannot bypass validation or fabricate evidence.

## 9. Acceptance and verification

### Acceptance contract freeze

Before T3/T4 production implementation, and before any lower-tier change whose correctness depends on a real path, freeze:

```text
entry boundary
real project modules executed
controlled dependency seam
production validators/contracts
persisted state/artifacts inspected
terminal positive result
negative/fail-closed result
prohibited later calls/events/writes
external-call ceiling
exact verification command
```

When safe and feasible, obtain failing proof before the implementation intended to make it pass.

### False-PASS scan

Reject proof based on unconditional assertions, always-valid validators, fabricated normalized success replacing the real producer, pre-seeded terminal/intermediate state that bypasses the path, persistence doubles that bypass required semantics, unused counters, comments/test names/source searches as sole evidence, hardcoded call/cost claims, local substitutes for mandatory exact-head CI, or mocks above the production boundary being proved.

A false-PASS test is a defect in the proof system.

### Sequential Evidence Gate

For ordered work:

```text
INSPECT
→ DEFINE PROOF
→ REPRODUCE FAILURE when safe/feasible
→ IMPLEMENT COMPLETE BOUNDED SECTION
→ NARROW VERIFY
→ SECTION AUDIT
→ AUTO-CONTINUE ON PASS
```

A section passes only when requirement, determinacy boundary, real path where applicable, direct positive proof, required negative proof, and affected earlier boundaries pass. Correct failed sections before dependent work proceeds.

Routine SECTION PASS does not require user approval unless the next action crosses an authorization boundary or requires determinacy to be reopened. A route escalation, human-wait state, budget approval, denied control-plane decision, or scope expansion is not eligible for silent auto-continuation.

### Balanced verification

Use three layers:

1. narrow active test-area checks after each section;
2. affected integration/contract/security/etc. checks only where a changed boundary can invalidate them;
3. one terminal verification after all sections pass: cross-section review, all mandatory active Test Areas, acceptance/regression, static/build/security/persistence/recovery as applicable, scope/diff/surgical checks, and machine gate where required.

Do not run the most expensive suite after every isolated section unless governance requires it.

### Real production path acceptance

Acceptance proves real project behavior, not a hand-written imitation. Prefer real project modules with controlled dependencies below the boundary being proved, production validators/contracts, real normalization/persistence/artifact boundaries, and the real orchestrator/UI/API/CLI/job path.

Controlled fixtures may emulate external responses. Real modules being claimed must execute. Measure exact calls/writes/tasks where retries, idempotency, cost, polling, or side effects matter.

### Negative-path proof

Where failure behavior matters, prove applicable dimensions:

```text
operation fails with governed classification
AND persisted state equals governed failure state
AND prohibited later events do not exist
AND prohibited later calls equal zero
AND prohibited artifacts/writes do not exist
AND protected prior state remains unchanged when required
```

An exception alone is insufficient.

### External-call contract

Tests and CI use zero live paid/provider/model calls unless explicitly authorized.

Where applicable define operation identity, request/task ID persistence, timeout, retry classification, attempt/budget ceiling, backoff, cancellation, resume/recovery, task reuse, duplicate-charge prevention, controlled dependency, and measured call/cost counters.

A retryable failure after paid task creation must not create a second paid task unless the provider contract requires it. Controlled tests should isolate real credentials where technically feasible and fail unexpected live execution.

This External-call contract governs calls made by the **software under test**. Coding-agent/model execution-resource cost is governed separately by the Execution control plane integration contract when present.

### Durable-job contract

For background/asynchronous work, persist enough state before asynchronous acceptance to resume the exact operation without reconstructing required inputs from defaults.

Prove fresh-process recovery, retry budget/classification, task reuse, duplicate-work prevention, cancellation propagation, and zero prohibited side effects after abort where applicable.

When an orchestrator owns coding-agent task/run durability, GCU records durable task/run references and verifies correlation continuity rather than creating a competing execution ledger.

## 10. Causal Necessity Audit and incidental findings

After implementation and before terminal completion, audit every material changed production boundary.

Required mapping:

```text
Requirement ID
→ material changed boundary
→ why the preserved requirement would remain incorrect if that boundary were unchanged
→ direct evidence
```

A material change that cannot be causally mapped is not justified merely because tests pass. Remove it or create a separately authorized governed change.

Do not require blind per-line revert testing. Use selective revert testing where causal necessity is disputed, coupled changes obscure necessity, or direct evidence is insufficient.

The pre-change structural budget limits expected architectural surface; the post-change Causal Necessity Audit proves actual surface.

Incidental findings remain outside the active change unless direct evidence proves they are required for the frozen outcome **and** the determinacy gate is reopened before modifying the new boundary.

## 11. Challenger gate, cross-section review, and terminal truth

### Challenger gate

Before terminal verification for T2+ work, and earlier when risk warrants it, challenge:

- original requirement versus governed interpretation;
- change hypothesis and causal boundary;
- structural budget and every reopen event;
- incidental-finding adoption;
- false-PASS risks;
- missing downstream consumers, compatibility cases, migrations, auth/tenant boundaries, retry/recovery, negative paths, and terminal states;
- mocks above the claimed boundary;
- whether evidence would still pass if the governed defect remained;
- whether execution-control authority is duplicated or bypassed;
- whether audit independence is being confused with model capability.

Correct actionable determinacy or proof defects before terminal acceptance.

### Cross-section review

Inspect each edge:

```text
upstream governed output → contract/validation → downstream consumer
```

Confirm no validation bypass, no prohibited post-validation mutation, no later-section escape from the frozen determinacy boundary, and correct shared-component integration.

When execution control is active, also verify continuity:

```text
GCU context
→ orchestrator task/run/approval
→ AI policy route/budget decision
→ authoritative usage receipt
→ returned GCU evidence reference
```

### Terminal-path gate

For `STAGING_READY` or `PRODUCTION_READY`, identify the terminal user/business promise and prove the **same governed execution** reaches it:

```text
real entry
→ governed intermediate boundaries
→ terminal state/artifact
→ final retrieval/observable outcome
```

Compiled, authenticated, queued, rendered, or approved are not terminal when required persistence, authorization, publication, delivery, or retrieval remains.

## 12. Change PASS is not Production Ready

Report separately:

```text
CHANGE RESULT: PASS / BLOCKED
CHANGE TIER: T1_LOCAL / T2_BOUNDARY / T3_SYSTEM / T4_RELEASE
RELEASE INTENT: CHANGE_ONLY / STAGING_READY / PRODUCTION_READY
SURGICAL DETERMINACY: PASS / BLOCKED
EXECUTION CONTROL PLANE: PASS / N/A / BLOCKED
EXECUTION COST STATUS: WITHIN_BUDGET / BLOCKED / UNAVAILABLE / N/A
SYSTEM READINESS: NOT ASSESSED / BLOCKED / READY
```

### Full-system production-readiness gate

For `PRODUCTION_READY`, verify every applicable responsibility: real production composition, persistence/migrations, authentication/authorization/tenant isolation, secrets handling, executable contracts, production adapters with controlled acceptance dependencies, durable jobs/recovery/retry/idempotency/cancellation, product external-call cost controls, execution-control authority/receipts when applicable, canonical evidence/artifact integrity, governed downstream consumers, rendering/publication/delivery/final retrieval, negative cross-account access when applicable, required observability, rollback/recovery, no fabricated success, no remaining repository-controlled blocker, exact-head CI, machine gate, Surgical Determinacy Audit, exact-head audit, and required release authorization.

`N/A` requires direct evidence.

### Production Closure Mode

Use when known production-readiness defects collectively block one end-to-end path. Repository-owned required infrastructure is implementation work, not a final blocker. A genuine external blocker is outside repository control and cannot be safely created or simulated.

Production Closure does not waive Surgical Determinacy. Each correction boundary must be causally justified inside the closure objective. Complete repository-controlled work first.

A required external execution-policy authorization or unavailable mandatory policy service may create `GOVERNANCE HOLD`; it does not turn an unexecuted route into PASS.

## 13. Machine release gate and Independent exact-head audit

### Machine release gate

The coding agent is not Release Authority. A repository gate such as `change:release-gate` evaluates machine-enforceable conditions against the exact candidate head and exits non-zero for failed, missing, stale, or unprovable mandatory conditions.

Agent prose, confidence, stronger-model output, or local substitutes cannot override it.

When controlled code verification passes but mandatory exact-head external proof is temporarily unavailable, report:

```text
CODE VERIFIED / GOVERNANCE HOLD
```

### Independent exact-head audit

The Auditor inspects the actual candidate commit, not the Builder report alone.

Verify exact SHA, exact-head CI where required, preserved requirement, frozen Surgical Change Contract and reopen history, actual changed-file/material-symbol surface, structural budget versus actual surface, Causal Necessity Audit mappings, incidental findings, protected invariants, checklist IDs, active Test Area Map, real acceptance behavior, negative state/calls/writes, Production Spine, contract map, False-PASS scan, validated-object continuity, terminal/system-readiness claims, product external-call evidence, execution-control task/run/routing/approval/budget/usage references when applicable, complete diff, machine gate, and truthful authorization/release state.

If Builder and Auditor share the same context, label the result `SELF_AUDIT`; it does not satisfy a repository requirement for independence.

### Surgical Determinacy Audit

At the exact candidate head, require:

```text
Requirement preserved: PASS
Change hypothesis validated: PASS
Required outcome achieved: PASS
Material changed boundaries causally justified: PASS
Protected surfaces preserved: PASS
Structural change budget respected or formally reopened: PASS
Incidental findings excluded unless causally authorized: PASS
Unauthorized scope expansion: ZERO
Unjustified architectural change: ZERO
Unjustified contract change: ZERO
Unjustified dependency change: ZERO
```

Any mandatory failure blocks governed completion.

## 14. Correction and escaped-proof regression

On failure, map to the owning requirement/checklist ID, causal boundary, and Test Area. Correct the smallest governed boundary supported by evidence, repair direct proof first when the claim was unproven, rerun narrow and affected checks, then terminal verification and exact-head audit.

Correction does not authorize scope expansion. If the correction crosses an unplanned boundary, reopen the Surgical Change Determinacy Gate before modifying it.

If a production defect escaped earlier green proof, fix both the production defect and the proof system that allowed false PASS. A producer/consumer escape updates the contract map and acceptance harness.

If an execution-control defect escaped proof, correct both the integration and the receipt/approval/bypass proof that allowed it.

If an escaped defect proves the original causal hypothesis incomplete, update determinacy evidence and add a regression that would fail under the escaped condition. This is the **escaped-proof regression** rule.

## 15. Greenfield, monorepo, and automation rules

### New-application vertical-spine rule

For a new application or major greenfield subsystem, prove one real vertical slice early:

```text
one real entry
→ auth/tenant boundary when applicable
→ one persisted/domain operation
→ one real processing/service path
→ one terminal output/retrieval path
→ controlled acceptance PASS
```

Do not build many isolated green components while the first end-to-end slice remains unproven. The vertical-spine rule does not authorize unrelated framework or architecture work outside the current slice.

### Monorepo and multi-component rule

Identify affected components from discovery/Project Adapter, shared contracts and consumers, causal component surface, narrow tests, shared-boundary tests that can be invalidated, and cross-component handoffs for T2+ work. Defer unrelated expensive workspace tests until terminal verification unless repository governance requires them earlier.

Do not assume repository root is the only build/test boundary.

### Automation and efficiency

Automate stable rules where feasible: adapter staleness, preflight, determinacy-artifact presence, structural-budget versus actual-boundary checks, permitted/prohibited diff, invariants, schema/migration checks, generated artifacts, external-call guards, execution-control version/receipt correlation, Test Area commands, affected integration, full regression, production acceptance, recovery tests, exact-head CI lookup, PR state, machine release gate, and final evidence collection.

Do not create automation that rewards smaller line counts at the expense of causal correctness.

Default WIP: one active governed change, one active correction package, zero unplanned files unless determinacy is formally reopened or separate authorization is granted.

## 16. Governed states, final report, and self-check

Governed states:

- `SECTION PASS`
- `CODE VERIFIED`
- `STAGING CANDIDATE`
- `CODE VERIFIED / GOVERNANCE HOLD`
- `RELEASE READY`
- `BLOCKED`

Never infer merge, deployment, activation, model-route approval, budget approval, or release authorization from green tests.

### Mandatory final report

```text
GOVERNED CHANGE REPORT
Skill version: 2.3.0
Change ID:
Change Tier:
Release intent:
Original requested outcome:
Governed interpretation:
Repository:
Project Adapter version / verified SHA:
Starting SHA:
Final SHA:
PR:
Exact files changed:
Agent roster / audit separation:

Requirement Preservation: PASS/BLOCKED — evidence
Surgical Change Determinacy Gate: PASS/BLOCKED — evidence
Change hypothesis: PROVEN/DISPROVEN/UNRESOLVED — evidence
Structural change budget: PASS/REOPENED-AND-PASS/BLOCKED — evidence
Causal Necessity Audit: PASS/BLOCKED — evidence
Incidental findings adopted without causal authorization: 0 / count
Surgical Determinacy Audit: PASS/BLOCKED — evidence

Execution control plane: PASS/N/A/BLOCKED — evidence
Execution-control contract/version:
Orchestrator task/run refs:
Routing-decision refs:
Escalation/approval refs:
Budget-envelope ref:
Usage-receipt refs:
Execution cost status: WITHIN_BUDGET / BLOCKED / UNAVAILABLE / N/A
Provider/model bypass check:

Production spine: PASS/N/A — evidence
Contract map: PASS/N/A — evidence
Acceptance freeze: PASS/N/A — evidence
False-PASS scan: PASS — evidence
Challenger gate: PASS/N/A — evidence
Test Area Map: PASS — evidence
Terminal-path gate: PASS/N/A — evidence
Full-system readiness: PASS/N/A — evidence

Checklist/section results:
Verification commands/results:
Scope result:
Machine gate:
Exact-head CI:
Audit: INDEPENDENT / SELF_AUDIT / N/A — result
Product external-call evidence:
Working tree / PR / release state:

CHANGE RESULT: PASS / BLOCKED
SYSTEM READINESS: NOT ASSESSED / BLOCKED / READY
FINAL STATUS: CODE VERIFIED / STAGING CANDIDATE / GOVERNANCE HOLD / RELEASE READY / BLOCKED
```

Do not duplicate an authoritative provider billing transaction in the final report; preserve receipt references and the evidence needed for reconciliation.

No prose-only completion, hidden failed requirements, confidence in place of proof, local substitute for mandatory exact-head CI, or unearned release claim.

### Global invocation contract

A reliable installation supplies an equivalent of `GLOBAL_AGENT_RULE.md` in the persistent instruction layer:

```text
For every qualifying coding change, invoke governed-coding-upgrade before editing.
Run Project Discovery. Preserve the requirement. Pass the Surgical Change Determinacy
Gate. Discovery does not create authorization. Reopen the gate before causal scope
expansion. Use applicable Test Areas and real-path proof. Run the Causal Necessity
Audit, Challenger, terminal verification when applicable, Machine release gate,
Independent exact-head audit, and Surgical Determinacy Audit. Never claim release
readiness without required proof and authorization.
```

Vendor-specific adapters may change how this rule is installed, not what it means.

### Self-check

Before closure, verify from evidence: starting state; pre-existing work; Project Discovery; adapter validity; Requirement Preservation; change hypothesis; Surgical Change Determinacy Gate; causal boundary; expected/protected surfaces; structural budget and reopen history; incidental-finding disposition; Change Tier; Release Intent; agent-role truthfulness; execution-control authority separation, capability/escalation decisions, budget/route approvals, usage-receipt references, provider/model bypass and audit-context independence when applicable; active Test Area Map; Production Spine; Producer → Contract → Consumer map; Acceptance contract freeze; False-PASS scan; FROZEN CHECKLIST; Sequential Evidence Gate; Causal Necessity Audit; Challenger gate; Real production path acceptance; Negative-path proof; External-call contract; Durable-job contract; Single validated-object rule; Evidence preservation; cross-section integration; Terminal-path gate; Full-system production-readiness gate when claimed; protected invariants; exact changed-file/material-symbol scope; complete diff; Surgical Determinacy Audit; Machine release gate; exact-head CI; Independent exact-head audit / SELF_AUDIT truth; escaped-proof regression; and truthful release state.

If controlled code verification passes but a mandatory external release or execution-policy condition is unavailable, report `CODE VERIFIED / GOVERNANCE HOLD`. If any repository-controlled mandatory condition is failed or unproved, report `BLOCKED`.
