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

v2.3 retains the v2.2 universal project-orchestration and production-correctness controls and adds **Surgical Determinacy**: requirement preservation, causal change planning, structural change budgets, fail-closed scope expansion, causal-necessity auditing, and exact-head surgical audit.

GCU is LLM-agnostic. Vendor-specific installation files are adapters to this protocol; they do not change its governing semantics.

Standard lifecycle:

```text
INTAKE
→ PREFLIGHT
→ PROJECT DISCOVERY / ADAPTER CHECK
→ REQUIREMENT PRESERVATION
→ SURGICAL CHANGE DETERMINACY GATE
→ CHANGE TIER + RELEASE INTENT
→ AGENT ROSTER when useful
→ EXECUTION CONTROL PLANE CHECK when present
→ PRODUCTION SPINE / CONTRACT MAP when applicable
→ ACCEPTANCE FREEZE
→ FROZEN CHECKLIST + TEST AREA MAP
→ SEQUENTIAL BUILD / VERIFY
→ CAUSAL NECESSITY AUDIT
→ CHALLENGE
→ TERMINAL-PATH / SYSTEM READINESS when applicable
→ MACHINE GATE
→ EXACT-HEAD AUDIT + SURGICAL DETERMINACY AUDIT
→ CORRECT / RE-AUDIT
→ CLOSE
```

## 1. Authority

Resolve conflicts in this order:

1. platform, safety, legal, privacy, and security constraints;
2. explicit current user instruction and authorization boundaries;
3. repository governance and security rules;
4. product, API, schema, persistence, data, compatibility, and release contracts;
5. protected invariants and reference artifacts;
6. this skill;
7. repository Project Adapter / Governed Change Profile;
8. frozen Surgical Change Contract, checklist, Test Area Map, and acceptance contract;
9. implementation notes.

A lower layer cannot override a higher layer.

An external execution orchestrator or AI policy authority may constrain whether/how an AI execution occurs, but it does not override GCU scope, proof, audit, or release-readiness obligations. GCU likewise cannot override a denied budget, route, approval, security, or tenant-policy decision from a higher applicable control plane.

## 2. Mandatory invocation

Invoke this skill for intentional changes to source, tests, schemas, APIs, dependencies, executable configuration, migrations, persistence, jobs, external integrations, security controls, infrastructure, build/release logic, generated production artifacts, or runtime behavior.

Read-only inspection does not require the full lifecycle unless repository governance says otherwise.

No qualifying implementation begins before the Requirement Preservation and Surgical Change Determinacy obligations are satisfied at the depth appropriate to the Change Tier.

## 3. Repository preflight

Before editing, verify:

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

### Dirty-tree continuation

When the user explicitly asks to continue the same correction, preserve valid existing work: inspect status and diff, map changes to checklist IDs and the frozen Surgical Change Contract, correct in place, and do not reset merely to create a clean baseline.

### Interrupted-agent resume

After an agent/API/terminal interruption, resume the same repository and branch, inspect HEAD/diff/change workspace/checklist/Surgical Change Contract/test evidence, identify the last directly proven section, preserve valid work, and continue from the first unproven or failing obligation.

Repository state and recorded evidence outrank agent memory.

When an execution control plane supplies durable task/run/routing/usage references, preserve those references across resume; do not reconstruct or silently replace them from conversational memory.

## 4. Project Discovery

GCU adapts to the repository; it does not force the repository into one stack model.

Before planning, discover directly supported facts relevant to the change:

- repository, workspace, monorepo, and component boundaries;
- languages, runtimes, package/build systems;
- applications, services, libraries, CLIs, workers, infrastructure, data pipelines, and other project kinds;
- public interfaces and runtime entry points;
- test frameworks and existing test commands;
- CI/CD and release mechanisms;
- persistence, migrations, queues, caches, artifacts, and background jobs;
- authentication, authorization, tenant/account, privacy, and secret boundaries;
- external providers, paid/side-effecting calls, and controlled-test seams;
- execution orchestrator, AI policy authority, model-route/usage authority, and worker boundary when applicable;
- rollback/recovery mechanisms;
- protected/generated paths and repository-specific governance.

Unknown material facts are `UNRESOLVED`, never guessed.

Use `docs/UNIVERSAL_PROJECT_MODEL.md` for the universal model.

## 5. Project Adapter

Preferred path:

```text
.governance/PROJECT_ADAPTER.md
```

Use `templates/PROJECT_ADAPTER_TEMPLATE.md`.

The Project Adapter stores repository facts that should not be rediscovered or hard-coded into the universal skill. It maps GCU capabilities to real repository commands and boundaries.

Record, when applicable:

```text
project/component kinds and roots
build/runtime/test systems
commands by universal test area
protected/generated paths
migration/persistence/recovery policies
security/privacy/tenant boundaries
external-call and controlled-test policy
execution orchestrator / AI policy authority
execution-control contract/version
capability mapping owner
budget/model-route approval authority
usage-ledger authority and receipt lookup method
independent-context mechanism
release/CI/rollback methods
terminal promises
repository-specific stop conditions
last verified SHA
```

If a material adapter fact is stale or unsupported, re-verify it or mark it `UNRESOLVED`.

The existing `.governance/GOVERNED_CHANGE_PROFILE.md` remains compatible.

## 6. Requirement Preservation

Before choosing an implementation, preserve the actual requested outcome.

Record:

```text
Original requested outcome
Faithful governed interpretation
Explicit exclusions / non-goals
Observable acceptance condition
```

The governed interpretation must remain implementation-independent and must not silently add scope.

A precise implementation of the wrong interpretation is a governance failure.

The Challenger later verifies that the implementation solves the original requirement rather than only the Planner's reformulation.

## 7. Surgical Change Determinacy Gate

The Builder MUST NOT edit governed production code until this gate passes.

Freeze one bounded Surgical Change Contract, preferably from `templates/SURGICAL_CHANGE_CONTRACT_TEMPLATE.md`.

The contract contains:

```text
required outcome
supporting direct evidence
change hypothesis and predicted effect
causal boundary
expected change surface
protected surface
structural change budget
acceptance proof
scope-expansion conditions
```

### Change hypothesis

For a defect, state why current behavior differs from the required behavior. For an intentional capability upgrade, state what system boundary must change to create the requested result.

Classify the hypothesis:

```text
PROVEN
DISPROVEN
UNRESOLVED
```

Do not implement while a material causal fact is `UNRESOLVED`.

### Expected change surface

Use:

```text
REQUIRED — modules/contracts/components directly supported as necessary
EXPECTED — symbols/functions when genuinely determinable before implementation
PROHIBITED — unrelated boundaries, contracts, public behavior, and protected paths
```

Do not invent symbol-level precision that the evidence does not support. Exact changed symbols are still inspected after implementation.

### Protected surface

Everything outside the justified causal chain is protected by default unless the frozen contract explicitly says otherwise.

Protected surfaces may include public contracts, schemas, persistence, auth/tenant rules, unrelated features, dependencies, configuration, release behavior, and upstream/downstream components.

### Structural change budget

Freeze architectural surface, not textual size.

Budget dimensions may include:

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

Do not use maximum lines changed, arbitrary diff size, or function-count limits as a proxy for surgicality.

### Discovery does not create authorization

A newly discovered defect, cleanup opportunity, refactor, dependency issue, hardening opportunity, naming problem, duplicated logic, or adjacent feature does not enter the active change merely because it is useful, nearby, inexpensive, or in a file already being edited.

“Useful,” “related,” “cleaner,” “safer,” and “while we are here” are not sufficient causal justification.

Record incidental findings separately.

### Scope-expansion stop condition

If implementation requires touching a material boundary outside the frozen contract or exceeding a structural budget dimension:

```text
STOP
→ do not modify the new boundary
→ record direct evidence
→ reopen the Surgical Change Determinacy Gate
→ prove the additional boundary is causally necessary
→ update the frozen surface / protected surface / budget / proof as required
→ continue only after the gate passes again
```

Discovery is evidence that the original determinacy model may have been incomplete; it is not permission to broaden implementation automatically.

## 8. Change Tier

Declare one Change Tier:

- `T1_LOCAL` — contained local behavior; no governed external/persistent boundary change.
- `T2_BOUNDARY` — contract, schema, API, public interface, dependency boundary, auth rule, or producer/consumer handoff changes.
- `T3_SYSTEM` — cross-boundary, persistence, async, external-provider, security-sensitive, multi-component, or end-to-end behavior.
- `T4_RELEASE` — requested result includes staging/production readiness or repository release gates.

Change Tier controls governance depth. It does not replace Release Intent.

The Surgical Change Determinacy Gate applies at every tier; documentation depth may scale down for a simple T1 change, but causal justification does not disappear.

Do not classify complex work as T1 merely to reduce testing.

## 9. Release Intent

Declare exactly one before implementation:

- `CHANGE_ONLY` — prove the scoped change only.
- `STAGING_READY` — prove the scoped change plus governed staging conditions.
- `PRODUCTION_READY` — prove the complete production path through the terminal user/business promise and all applicable system-readiness conditions.

A green scoped change cannot be silently upgraded into production readiness.

## 10. Agent orchestration

GCU defines roles, not a required agent product.

Standard roles:

- **Scout** — read-only discovery and adapter verification by default.
- **Planner** — preserves requirement and freezes determinacy, scope, contracts, checklist, roster, and Test Area Map.
- **Builder** — implements governed sections only inside the frozen determinacy boundary.
- **Challenger** — tries to falsify requirement interpretation, causal assumptions, scope, proof, and readiness claims.
- **Verifier** — runs active test areas and records direct evidence.
- **Auditor** — inspects the exact candidate head.
- **Release Authority** — provides required protected-operation authorization.

One agent or human may hold several roles when safe. Do not create multiple agents merely to create activity.

For T1 work, one context may perform multiple roles. If Builder and Auditor are the same agent/context, label the result `SELF_AUDIT`; do not call it independent.

For T3/T4 work, prefer separate contexts for challenge, terminal verification, and audit when practical or required.

Parallel agents are allowed only for genuinely independent, non-overlapping sections with explicit boundary ownership, shared-contract handling, merge order, and integration ownership.

**Release Authority is not an AI model-execution role.** A human or repository-controlled authority may hold that responsibility. An execution-control adapter MUST reject attempts to model-dispatch `RELEASE_AUTHORITY` as though a model could authorize its own protected operation.

See `docs/AGENT_ORCHESTRATION.md`.

## 11. Execution control plane integration

When a coding agent runs behind an execution orchestrator or AI policy authority, use:

```text
gcu-execution-control/1.0.0
```

GCU owns the change-governance lifecycle. It does not become a second model router, credential broker, billing system, or orchestration ledger.

Provider-neutral execution context may include:

```text
change_id
repository / branch / candidate_sha
change_tier
release_intent
role
workload_class
capability_floor
independence_required
section_or_gate
authorization_boundary
budget_envelope_ref when supplied
escalation_reason when applicable
```

AI-executable roles are limited to:

```text
SCOUT
PLANNER
BUILDER
CHALLENGER
VERIFIER
AUDITOR
```

Capability floors are `ECONOMY`, `STANDARD`, `ADVANCED`, and `PREMIUM`.

Rules:

- GCU MUST NOT select a concrete provider/model as an execution side effect.
- GCU MUST NOT store provider credentials.
- GCU MUST NOT silently escalate to a more capable or more expensive model.
- GCU MUST NOT maintain a second authoritative execution-usage/billing ledger.
- Returned task/run, route, approval, budget-envelope, and usage-receipt references become governed evidence when applicable.
- A stronger model in the same Builder context does not create independent audit.

When capability is insufficient, record an escalation request rather than switching models directly. Allowed reasons remain:

```text
CAPABILITY_INSUFFICIENT
INDEPENDENCE_REQUIRED
CONTEXT_LIMIT
REPEATED_PROOF_FAILURE
POLICY_REQUIREMENT
MATERIAL_AMBIGUITY
```

A denied or expired route/approval is not permission to fallback.

### Execution cost versus product external-call cost

Keep two domains separate:

1. **Product external-call cost** — provider/API/model calls made by the software under test; governed through the `EXTERNAL CALL / COST` Test Area and external-call contract.
2. **Execution-resource cost** — model usage consumed by coding agents; authoritative pricing/enforcement/accounting remains with the execution control plane when present.

Recommended evidence includes task/run references, routing decisions, approval/escalation references, budget envelope, usage-receipt references, execution-cost status, and provider/model bypass checks.

Hardcoded execution-cost claims are not evidence.

See `docs/EXECUTION_CONTROL_PLANE_INTEGRATION.md`.

## 12. Governed learning memory integration

When `gcu-learning-memory/1.0.0` is available, preflight may recall only active approved practices relevant to the current repository/component.

Recalled practices are `ADVISORY_ONLY` and never outrank current user instruction, repository governance, the frozen Surgical Change Contract, or current evidence.

A producing run may emit evidence-linked lesson candidates after a truthful terminal state, but it MUST NOT auto-promote its own candidate into an ApprovedPractice without separate validation and explicit approval.

A failed/blocked run may produce a known-failure candidate but not a positive best-practice claim merely because an implementation was attempted.

See `docs/GOVERNED_LEARNING_LOOP.md`.

## 13. Governed change workspace

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

Small T1 changes may use a reduced record if repository governance permits it, but requirement preservation and determinacy still apply.

The workspace exists so another agent/session can resume from evidence rather than hidden conversational state.

See `templates/CHANGE_WORKSPACE_TEMPLATE.md`.

## 14. Universal Test Area Map

GCU uses capability-based test areas instead of assuming folders, commands, or frameworks:

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

For each change, record `ACTIVE`, justified `N/A`, or `UNRESOLVED` plus real command/mechanism and required positive/negative proof.

A missing command is not automatically N/A.

See `docs/TEST_AREAS.md`.

## 15. Production Spine gate

For T3/T4 cross-boundary production work, trace the real path before implementation:

```text
user/UI/API/CLI/event entry
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

For each hop record production module, input/output contract, state/artifact, failure behavior, retry/idempotency effect, tenant/account implication, and direct proof.

Do not implement while a material spine hop required by the declared result is unresolved.

## 16. Producer → Contract → Consumer map

For each material runtime handoff record:

| Producer | Produced object/state | Contract/schema | Validation point | Consumer | Consumer requirements | Failure result | Proof |
|---|---|---|---|---|---|---|---|

Rules:

- producer emits fields/semantics the consumer requires;
- validation happens before governed persistence, transition, rendering, publication, authorization, exposure, or irreversible effects;
- consumer uses the validated object/state rather than an ungoverned reconstruction when continuity is required;
- defaults cannot convert malformed usable data into valid-looking empty data;
- identity remains attached across authorization-relevant boundaries;
- escaped producer/consumer defects require correction of implementation and proof map.

## 17. Freeze scope and FROZEN CHECKLIST

Create a frozen checklist before implementation. Scope must be consistent with the Surgical Change Contract.

Every checklist item has a stable ID, one observable requirement, exact boundary, positive proof, negative proof when applicable, real-path acceptance proof when applicable, protected invariant, exact failure result, final evidence, and binary status.

No aspirational requirements, hidden requirements, prose-only proof, or `A OR B` result when one governed result is required.

## 18. Acceptance contract freeze

Before T3/T4 production implementation, and before lower-tier work whose correctness depends on a real path, freeze:

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

Reject proof based on unconditional assertions, always-valid validators, fabricated normalized success replacing the real producer, pre-seeded terminal/intermediate states that bypass the path, persistence doubles that bypass required semantics, unused counters, comments/test names/source searches as sole evidence, hardcoded external-call/cost claims, local substitutes for mandatory exact-head CI, or mocks above the production boundary being proved.

A false-PASS test is a defect in the proof system.

## 19. Sequential Evidence Gate

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

A section passes only when requirement, real path where applicable, direct positive proof, required negative proof, determinacy boundary, and affected earlier boundaries pass.

Correct failed sections before dependent work proceeds.

Routine SECTION PASS does not require user approval unless the next action crosses an explicit authorization boundary or determinacy must be reopened.

## 20. Balanced verification

Use three layers:

1. narrow active test-area checks after each section;
2. affected integration/contract/security/etc. checks only when a changed boundary can invalidate them;
3. one terminal verification after all sections pass: cross-section review, mandatory active test areas, acceptance/regression, static/build/security/persistence/recovery as applicable, scope/diff checks, surgical determinacy, and machine gate when required.

Do not run the most expensive suite after every isolated section unless governance requires it.

## 21. Real production path acceptance

Acceptance proves real project behavior, not a hand-written imitation.

Preferred shape:

```text
real project adapter/service/module
+
controlled dependency below that boundary
+
production validator/contract
+
real normalization/persistence/artifact boundary
+
real orchestrator/UI/API/CLI/job path
```

Controlled fixtures may emulate external responses. Real modules being claimed must execute.

Measure exact calls/writes/tasks when retries, idempotency, cost, polling, or side effects matter.

## 22. Evidence preservation

When external/raw evidence drives decisions, preserve:

```text
raw response/reference
→ governed raw artifact/reference
→ real normalizer/adapter
→ validated evidence contract
→ persisted canonical evidence
→ downstream consumer
```

Prove provenance, field preservation, validation, canonical persistence, governed consumer loading, and that fallback/replay/cache paths cannot bypass validation or fabricate evidence.

Execution-control usage receipts are references to authoritative execution evidence; they do not replace the product evidence chain under test.

## 23. External-call contract

Tests and CI use zero live paid/provider/model calls unless explicitly authorized.

Where applicable define operation identity, request/task ID persistence, timeout, retry classification, attempt/budget ceiling, backoff, cancellation, resume/recovery, task reuse, duplicate-charge prevention, controlled dependency, and measured call/cost counters.

A retryable failure after task creation must not create a second paid task unless the provider contract requires it.

Controlled tests should isolate real credentials where feasible and fail unexpected live execution.

## 24. Single validated-object rule

For governed persistence, lifecycle, rendering, publication, authorization, delivery, or exposure:

```text
assemble complete object
→ validate complete object
→ retain/freeze validated object when applicable
→ persist/advance/render/publish/authorize/consume that validated object
```

Do not validate a partial object and add required fields afterward. Do not validate object A and consume independently reconstructed object B when continuity is governed.

Malformed usable states fail closed.

## 25. Negative-path proof

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

For execution-control integration, applicable negative proof includes denied/expired escalation not falling back, budget denial before execution, provider/model bypass rejection, missing mandatory usage receipt blocking closure, and Release Authority rejection from AI execution.

## 26. Causal Necessity Audit

After implementation and before terminal completion, audit every material changed production boundary.

Required mapping:

```text
Requirement ID
→ material changed boundary
→ why the preserved requirement would remain incorrect if this boundary were unchanged
→ direct evidence
```

A change that cannot be causally mapped is not justified merely because tests pass.

Remove it, or create a separately authorized governed change.

Do not require blind per-line revert testing. Use selective revert testing when causal necessity is disputed, coupled changes obscure necessity, or direct evidence is insufficient.

The Causal Necessity Audit complements the structural change budget: budget controls expected surface before implementation; necessity proves actual surface afterward.

## 27. Incidental finding rule

Incidental findings remain outside the active change unless direct evidence proves they are causally required for the frozen outcome and the determinacy gate is reopened before modifying the newly required boundary.

Do not absorb work because it is easy, related, nearby, already-open, quality-improving, or technically desirable.

Record useful findings separately for future triage.

## 28. Challenger gate

Before terminal verification for T2+ work, and earlier when risk warrants it, challenge the proof system and determinacy model.

Ask:

- Does the governed interpretation still match the original requested outcome?
- What assumption could make the change hypothesis wrong?
- Is the causal boundary broader than direct evidence requires?
- Did any budget expansion occur without a prior determinacy reopen?
- Did discovery silently become authorization for incidental work?
- What downstream consumer is unproved?
- What negative path, compatibility case, migration, auth/tenant boundary, retry/recovery path, or terminal state is missing?
- Is any mock above the boundary being claimed?
- Would the same evidence still pass if the governed defect remained?
- Is audit independence being confused with model capability?

Record actionable findings. Correct proof/determinacy defects before terminal acceptance.

## 29. Production Closure Mode

Use when known production-readiness defects collectively block one end-to-end path.

One closure package may include request/config persistence, source contracts, production adapters, artifact integrity, validation gates, durable jobs, restart/recovery, retries, idempotency, cancellation, replay/cache paths, publication, terminal retrieval, authorization/tenant isolation, and negative proof when required.

Production Closure does not waive Surgical Determinacy. Each correction boundary must remain causally justified within the closure objective.

Repository-owned required infrastructure is implementation work, not a final blocker. A genuine external blocker is outside repository control and cannot be safely created or simulated.

A required external execution-policy authorization or unavailable mandatory policy service may create `GOVERNANCE HOLD`; it does not convert an unexecuted route into PASS.

## 30. Durable-job contract

For background/asynchronous work, persist enough state before asynchronous acceptance to resume the exact operation without reconstructing required inputs from defaults.

Prove fresh-process recovery, governed retry budget/classification, task reuse, duplicate-work prevention, cancellation propagation, and zero prohibited side effects after abort where applicable.

When an orchestrator owns agent task/run durability, GCU records its references and verifies correlation continuity rather than creating a competing ledger.

## 31. Cross-section review

After sections pass, inspect each edge:

```text
upstream governed output → contract/validation → downstream consumer
```

Confirm the consumer receives the governed result, does not bypass validation, and does not mutate required fields after proof. Correct defects in the owning section and rerun affected later areas.

Also confirm later sections did not create unplanned changes outside the frozen determinacy boundary.

## 32. Terminal-path gate

For `STAGING_READY` or `PRODUCTION_READY`, identify the terminal user/business promise and prove the same governed execution reaches it.

Intermediate states such as compiled, authenticated, queued, rendered, or approved are not terminal when later required persistence, authorization, publication, delivery, or retrieval remains.

```text
real entry
→ governed intermediate boundaries
→ terminal state/artifact
→ final retrieval/observable outcome
```

## 33. Change PASS is not Production Ready

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

For `PRODUCTION_READY`, verify every applicable responsibility: real production composition, persistence/migrations, authentication/authorization/tenant isolation, secrets handling, executable contracts, production adapters with controlled acceptance dependencies, durable jobs/recovery/retry/idempotency/cancellation, product external-call cost controls, execution-control-plane authority/receipts when applicable, canonical artifact/evidence integrity, governed downstream consumers, rendering/publication/delivery/final retrieval, negative cross-account access when applicable, required observability, rollback/recovery, no fabricated success on the proven path, no remaining repository-controlled blocker, exact-head CI, machine gate, audit, Surgical Determinacy Audit, and required authorization.

`N/A` requires direct evidence.

## 34. Machine release gate

The coding agent is not the release authority. A repository gate such as `change:release-gate` evaluates machine-enforceable conditions against the exact candidate head and exits non-zero for failed, missing, stale, or unprovable mandatory conditions.

Agent prose, confidence, or local substitutes cannot override the gate.

When mandatory exact-head CI is temporarily unavailable while controlled local verification passes, report:

```text
CODE VERIFIED / GOVERNANCE HOLD
```

A model route, stronger model, or AI-generated release recommendation cannot substitute for Release Authority.

## 35. Independent exact-head audit

The auditor inspects the actual candidate commit, not the Builder report alone.

Verify:

- exact SHA and exact-head CI when required;
- preserved original requirement;
- frozen Surgical Change Contract and reopen history;
- actual changed-file and material changed-symbol surface;
- structural change budget versus actual surface;
- Causal Necessity Audit mappings;
- incidental findings and their disposition;
- protected surfaces/invariants;
- checklist IDs and active Test Area Map;
- real acceptance behavior and negative state/calls/writes;
- Production Spine and contract map;
- false-PASS scan and validated-object continuity;
- terminal/system-readiness claims;
- product external-call evidence;
- execution-control task/run/routing/approval/budget/usage references when applicable;
- complete diff, machine gate, and truthful authorization/release state.

### Surgical Determinacy Audit

Return surgical PASS only when all mandatory conditions hold:

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

If Builder and Auditor are the same agent/context, label the audit `SELF_AUDIT`. A different model in the same Builder context does not change that classification.

## 36. Correction and escaped-proof regression

On failure, map to the owning requirement/checklist ID, causal boundary, and test area. Correct the smallest governed boundary supported by evidence, repair direct proof first when the claim was unproven, rerun narrow and affected checks, then terminal verification and exact-head audit.

A correction is not permission to broaden scope. If the required correction crosses an unplanned boundary, reopen the Surgical Change Determinacy Gate before modifying it.

If a production defect escaped earlier green proof, fix both the production defect and the proof system that allowed the false PASS. A producer/consumer escape updates the contract map and acceptance harness.

If an escaped defect proves the original causal hypothesis was incomplete, update the determinacy evidence and add regression proof that would fail under the escaped condition.

This is the escaped-proof regression rule.

## 37. Governed states

- `SECTION PASS`
- `CODE VERIFIED`
- `STAGING CANDIDATE`
- `CODE VERIFIED / GOVERNANCE HOLD`
- `RELEASE READY`
- `BLOCKED`

Never infer merge, deployment, activation, model-route approval, budget approval, or release authorization from green tests.

## 38. New-application vertical-spine rule

For a new application or major greenfield subsystem, prove one real vertical slice early:

```text
one real entry
→ auth/tenant boundary when applicable
→ one persisted/domain operation
→ one real processing/service path
→ one terminal output/retrieval path
→ controlled acceptance PASS
```

Do not build many isolated green components while the first end-to-end slice remains unproven.

The vertical-spine rule does not authorize unrelated framework or architecture work outside the current governed slice.

## 39. Monorepo and multi-component rule

For each change:

1. identify affected components from the Project Adapter/discovery;
2. identify shared contracts and consumers;
3. freeze the causal component surface in the Surgical Change Contract;
4. select narrow tests from affected components;
5. run shared-boundary tests when they can be invalidated;
6. defer unrelated expensive full-workspace tests until terminal verification unless required;
7. prove cross-component handoffs for T2+ changes.

Do not assume the repository root is the only build/test boundary.

## 40. Automation and efficiency

Automate stable repeatable rules where feasible: project discovery facts, adapter staleness checks, preflight, protected-work checks, determinacy artifact presence, structural-budget versus actual-boundary checks, permitted/prohibited diff, invariants, schema/migration checks, generated artifacts, external-call guards, execution-control contract/version checks, route/approval/usage-receipt correlation, test-area commands, affected integration, full regression, production acceptance, recovery tests, exact-head CI lookup, PR state, machine release gate, and final evidence collection.

Do not create automation that rewards smaller line counts at the expense of causal correctness.

Default WIP: one active governed change, one active correction package, zero unplanned files unless the determinacy gate is formally reopened or separate authorization is granted.

## 41. Mandatory final report

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

No prose-only completion, hidden failed requirements, confidence in place of proof, local substitute for mandatory exact-head CI, or unearned release claim.

## 42. Global invocation contract

A reliable installation includes a persistent rule equivalent to `GLOBAL_AGENT_RULE.md`:

```text
For every qualifying coding change, invoke governed-coding-upgrade before editing.
Run Project Discovery. Preserve the requirement. Pass the Surgical Change Determinacy
Gate. Discovery does not create authorization. Reopen the gate before any causal scope
expansion. Use applicable Test Areas and real-path proof. Run Causal Necessity Audit,
Challenger, terminal verification when applicable, machine gate, exact-head audit and
Surgical Determinacy Audit. Never claim release readiness without required proof and
authorization.
```

Vendor-specific installation adapters may change how this rule is supplied to the agent, but not what it means.

## 43. Self-check

Before final closure, verify from evidence that starting state, pre-existing work, Project Discovery, adapter validity, Requirement Preservation, change hypothesis, Surgical Change Determinacy Gate, causal boundary, protected surface, structural change budget, any gate reopen history, incidental-finding disposition, Change Tier, Release Intent, agent-role truthfulness, execution-control authority separation when applicable, capability/escalation decisions, budget/route approvals, durable usage-receipt references, provider/model bypass checks, audit-context independence, active Test Area Map, Production Spine, contract map, acceptance freeze, false-PASS scan, frozen scope, sequential section proof, Causal Necessity Audit, challenge findings, real-path acceptance, controlled product external-call evidence, fail-closed paths, validated-object continuity, repository-owned requirements, durability/recovery, cross-section integration, terminal promise, system readiness when claimed, protected invariants, exact changed-file/material-symbol scope, complete diff, Surgical Determinacy Audit, machine gate, exact-head CI, audit separation/result, escaped-proof correction, and truthful release state satisfy the declared result.

If controlled code verification passes but a mandatory external release or execution-policy condition is unavailable, report `CODE VERIFIED / GOVERNANCE HOLD`. If any repository-controlled mandatory condition is unproved or failed, report `BLOCKED`.
