---
name: governed-coding-upgrade
description: >-
  Universal governed execution, testing, audit, and production-readiness protocol for coding changes across project types.
---

# Governed Coding Upgrade Skill v2.2.0 — Universal Project Orchestration

**Version:** 2.2.0  
**Machine-facing skill name:** `governed-coding-upgrade`  
**Status:** Governing execution skill

## Governing purpose

Governed Coding Upgrade (GCU) turns software changes into an evidence-based lifecycle without assuming a language, framework, CI provider, cloud, repository shape, or agent runtime.

v2.2 preserves the v2.1 production-correctness and sequential-evidence controls and adds:

- Project Discovery;
- a reusable Project Adapter;
- Change Tier scaling;
- optional agent orchestration;
- a capability-based Test Area Map;
- monorepo/multi-component selection;
- durable change workspaces for interruption and agent handoff.

Standard lifecycle:

```text
INTAKE
→ PREFLIGHT
→ PROJECT DISCOVERY / ADAPTER CHECK
→ CHANGE TIER + RELEASE INTENT
→ AGENT ROSTER when useful
→ PRODUCTION SPINE / CONTRACT MAP when applicable
→ ACCEPTANCE FREEZE
→ FROZEN CHECKLIST + TEST AREA MAP
→ SEQUENTIAL BUILD / VERIFY
→ CHALLENGE
→ TERMINAL-PATH / SYSTEM READINESS when applicable
→ MACHINE GATE
→ EXACT-HEAD AUDIT
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
8. frozen checklist, Test Area Map, and acceptance contract;
9. implementation notes.

A lower layer cannot override a higher layer.

## 2. Mandatory invocation

Invoke this skill for intentional changes to source, tests, schemas, APIs, dependencies, executable configuration, migrations, persistence, jobs, external integrations, security controls, infrastructure, build/release logic, generated production artifacts, or runtime behavior.

Read-only inspection does not require the full lifecycle unless repository governance says otherwise.

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
```

Starting-SHA mismatch is a stop condition. Never discard pre-existing user work without authorization.

### Dirty-tree continuation

When the user explicitly asks to continue the same correction, preserve valid existing work: inspect status and diff, map changes to checklist IDs, correct in place, and do not reset merely to create a clean baseline.

### Interrupted-agent resume

After an agent/API/terminal interruption, resume the same repository and branch, inspect HEAD/diff/change workspace/checklist/test evidence, identify the last directly proven section, preserve valid work, and continue from the first unproven or failing section.

Repository state and recorded evidence outrank agent memory.

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

It may describe a single project or multiple components in a monorepo.

Record, when applicable:

```text
project/component kinds and roots
build/runtime/test systems
commands by universal test area
protected/generated paths
migration/persistence/recovery policies
security/privacy/tenant boundaries
external-call and controlled-test policy
release/CI/rollback methods
terminal promises
repository-specific stop conditions
last verified SHA
```

If a material adapter fact is stale or unsupported, re-verify it or mark it `UNRESOLVED`.

The existing `.governance/GOVERNED_CHANGE_PROFILE.md` remains compatible. Repositories may keep it, migrate it into the Project Adapter, or use both while transitioning.

## 6. Change Tier

Declare one Change Tier based on affected boundaries and proof depth:

- `T1_LOCAL` — contained local behavior; no governed external/persistent boundary change.
- `T2_BOUNDARY` — contract, schema, API, public interface, dependency boundary, auth rule, or producer/consumer handoff changes.
- `T3_SYSTEM` — cross-boundary, persistence, async, external-provider, security-sensitive, multi-component, or end-to-end behavior.
- `T4_RELEASE` — the requested result includes staging/production readiness or repository release gates.

Change Tier controls governance depth. It does not replace Release Intent.

Do not classify a complex change as T1 merely to reduce testing.

## 7. Release intent

Declare exactly one before implementation:

- `CHANGE_ONLY` — prove the scoped change only.
- `STAGING_READY` — prove the scoped change plus governed staging conditions.
- `PRODUCTION_READY` — prove the complete production path through the terminal user/business promise and all applicable system-readiness conditions.

A green scoped change cannot be silently upgraded into production readiness.

## 8. Agent orchestration

GCU defines roles, not a required agent product.

Standard roles:

- **Scout** — read-only repository discovery and adapter verification by default.
- **Planner** — freezes scope, contracts, checklist, agent roster, and Test Area Map.
- **Builder** — implements governed sections only.
- **Challenger** — tries to falsify assumptions, acceptance design, and proof.
- **Verifier** — runs active test areas and records direct evidence.
- **Auditor** — inspects the exact candidate head.
- **Release Authority** — provides required protected-operation authorization.

One agent or human may hold several roles when safe. Do not create multiple agents merely to create activity.

For T1 work, one agent may perform Scout + Planner + Builder + Verifier + audit. If the same agent audits its own work, label the result `SELF_AUDIT`; do not call it independent.

For T3/T4 work, prefer separate contexts for challenge, terminal verification, and audit when practical or required by repository governance.

Parallel agents are allowed only for genuinely independent, non-overlapping sections with explicit boundary ownership, shared-contract handling, merge order, and integration ownership.

See `docs/AGENT_ORCHESTRATION.md` and `templates/AGENT_ROSTER_TEMPLATE.md`.

## 9. Governed change workspace

For material or interruptible work, prefer:

```text
.governance/changes/<CHANGE-ID>/
  INTAKE.md
  DISCOVERY.md
  CHECKLIST.md
  AGENT_ROSTER.md
  TEST_AREA_MAP.md
  EVIDENCE.md
  AUDIT.md
```

Small T1 changes may use a reduced record if repository governance permits it.

The workspace exists so another agent/session can resume from evidence rather than hidden conversational state.

See `templates/CHANGE_WORKSPACE_TEMPLATE.md`.

## 10. Universal Test Area Map

GCU uses capability-based test areas instead of assuming folders, commands, or frameworks.

Areas:

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

For each change, create or record a Test Area Map with `ACTIVE`, justified `N/A`, or `UNRESOLVED` state plus the real command/mechanism and required positive/negative proof.

A missing command is not automatically N/A.

The Project Adapter supplies stable repository commands. The per-change map selects only the areas affected by the change and release claim.

See `docs/TEST_AREAS.md` and `templates/TEST_AREA_MAP_TEMPLATE.md`.

## 11. Production Spine gate

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

## 12. Producer → Contract → Consumer map

For each material runtime handoff record:

| Producer | Produced object/state | Contract/schema | Validation point | Consumer | Consumer requirements | Failure result | Proof |
|---|---|---|---|---|---|---|---|

Rules:

- producer emits the fields/semantics the consumer requires;
- validation happens before governed persistence, transition, rendering, publication, authorization, exposure, or irreversible side effects;
- consumer uses the validated object/state rather than an ungoverned reconstruction when continuity is required;
- defaults cannot convert malformed usable data into valid-looking empty data;
- tenant/account/security identity remains attached across authorization-relevant boundaries;
- an escaped producer/consumer defect requires correction of implementation and proof map.

## 13. Freeze scope and FROZEN CHECKLIST

Define explicit permitted and prohibited files/boundaries. Create a frozen checklist before implementation.

Preferred path:

```text
.governance/changes/<CHANGE-ID>/CHECKLIST.md
```

Every checklist item has a stable ID, one observable requirement, exact boundary, positive proof, negative proof when applicable, real-path acceptance proof when applicable, protected invariant, exact failure result, final evidence, and binary status.

No aspirational requirements, hidden requirements, prose-only proof, or `A OR B` result when one governed result is required.

## 14. Acceptance contract freeze

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

Reject proof that depends on unconditional assertions, always-valid validators, fabricated normalized success replacing the real producer, pre-seeded terminal/intermediate states that bypass the path under proof, persistence doubles that bypass required semantics, unused counters, comments/test names/source searches as sole evidence, hardcoded external-call/cost claims, local substitutes for mandatory exact-head CI, or mocks placed above the production boundary being proved.

A false-PASS test is a defect in the proof system.

## 15. Sequential Evidence Gate

For ordered work:

```text
INSPECT
→ DEFINE PROOF
→ REPRODUCE FAILURE when safe/feasible
→ IMPLEMENT COMPLETE SECTION
→ NARROW VERIFY
→ SECTION AUDIT
→ AUTO-CONTINUE ON PASS
```

A section passes only when the requirement, real path where applicable, direct positive proof, required negative proof, and affected earlier boundaries pass.

Correct failed sections before dependent work proceeds. Routine SECTION PASS does not require user approval unless the next action crosses an explicit authorization boundary.

## 16. Balanced verification

Use three layers:

1. narrow active test-area checks after each section;
2. affected integration/contract/security/etc. checks only when a changed boundary can invalidate them;
3. one terminal verification after all sections pass: cross-section review, all mandatory active test areas, acceptance/regression, static/build/security/persistence/recovery as applicable, scope/diff checks, and machine gate when required.

Do not run the most expensive suite after every isolated section unless governance requires it.

## 17. Real production path acceptance

Acceptance proves the real project behavior, not a hand-written imitation.

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

## 18. Evidence preservation

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

## 19. External-call contract

Tests and CI use zero live paid/provider/model calls unless explicitly authorized.

Where applicable define operation identity, request/task ID persistence, timeout, retry classification, attempt/budget ceiling, backoff, cancellation, resume/recovery, task reuse, duplicate-charge prevention, controlled dependency, and measured call/cost counters.

A retryable failure after task creation must not create a second paid task unless the provider contract explicitly requires it.

Controlled tests should isolate real credentials where technically feasible and fail unexpected live execution.

## 20. Single validated-object rule

For governed persistence, lifecycle, rendering, publication, authorization, delivery, or exposure:

```text
assemble complete object
→ validate complete object
→ retain/freeze validated object when applicable
→ persist/advance/render/publish/authorize/consume that validated object
```

Do not validate a partial object and add required fields afterward. Do not validate object A and consume an independently reconstructed object B when continuity is governed.

Malformed usable states fail closed.

## 21. Negative-path proof

Where failure behavior matters, prove applicable dimensions:

```text
operation fails with governed classification
AND
persisted state equals governed failure state
AND
prohibited later events do not exist
AND
prohibited later calls equal zero
AND
prohibited artifacts/writes do not exist
AND
protected prior state remains unchanged when required
```

An exception alone is insufficient.

## 22. Challenger gate

Before terminal verification for T2+ work, and earlier when risk warrants it, challenge the proof system.

Ask:

- What assumption could make this PASS false?
- What downstream consumer is unproved?
- What negative path, compatibility case, migration, auth/tenant boundary, retry/recovery path, or terminal state is missing?
- Is any mock above the boundary being claimed?
- Is the Project Adapter stale or overgeneralized?
- Would the same evidence still pass if the defect remained?

Record actionable findings. Correct proof defects before terminal acceptance.

## 23. Production Closure Mode

Use when known production-readiness defects collectively block one end-to-end path.

One closure package may include request/config persistence, source contracts, production adapters, artifact integrity, validation gates, durable jobs, restart/recovery, retries, idempotency, cancellation, replay/cache paths, publication, terminal retrieval, authorization/tenant isolation, and negative proof when required.

Repository-owned required infrastructure is implementation work, not a final blocker. A genuine external blocker is outside repository control and cannot be safely created or simulated.

Complete repository-controlled work first.

## 24. Durable-job contract

For background/asynchronous work, persist enough state before asynchronous acceptance to resume the exact operation without reconstructing required inputs from defaults.

Prove fresh-process recovery, governed retry budget/classification, task reuse, duplicate-work prevention, cancellation propagation, and zero prohibited side effects after abort where applicable.

## 25. Cross-section review

After sections pass, inspect each edge:

```text
upstream governed output → contract/validation → downstream consumer
```

Confirm the consumer receives the governed result, does not bypass validation, and does not mutate required fields after proof. Correct defects in the owning section and rerun affected later areas.

## 26. Terminal-path gate

For `STAGING_READY` or `PRODUCTION_READY`, identify the terminal user/business promise and prove the same governed execution reaches it.

Intermediate states such as compiled, authenticated, queued, rendered, or approved are not terminal when later required persistence, authorization, publication, delivery, or retrieval remains.

```text
real entry
→ governed intermediate boundaries
→ terminal state/artifact
→ final retrieval/observable outcome
```

## 27. Change PASS is not Production Ready

Report separately:

```text
CHANGE RESULT: PASS / BLOCKED
CHANGE TIER: T1_LOCAL / T2_BOUNDARY / T3_SYSTEM / T4_RELEASE
RELEASE INTENT: CHANGE_ONLY / STAGING_READY / PRODUCTION_READY
SYSTEM READINESS: NOT ASSESSED / BLOCKED / READY
```

### Full-system production-readiness gate

For `PRODUCTION_READY`, verify every applicable responsibility: real production composition, persistence/migrations, authentication/authorization/tenant isolation, secrets handling, executable contracts, production adapters with controlled acceptance dependencies, durable jobs/recovery/retry/idempotency/cancellation, external-call cost controls, canonical artifact/evidence integrity, governed downstream consumers, rendering/publication/delivery/final retrieval, negative cross-account access when applicable, required observability, rollback/recovery, no fabricated success on the proven path, no remaining repository-controlled blocker, exact-head CI, machine gate, audit, and required authorization.

`N/A` requires direct evidence.

## 28. Machine release gate

The coding agent is not the release authority. A repository gate such as `change:release-gate` evaluates machine-enforceable conditions against the exact candidate head and exits non-zero for failed, missing, stale, or unprovable mandatory conditions.

Agent prose, confidence, or local substitutes cannot override the gate.

When mandatory exact-head CI is temporarily unavailable while controlled local verification passes, report:

```text
CODE VERIFIED / GOVERNANCE HOLD
```

## 29. Independent exact-head audit

The auditor inspects the actual candidate commit, not the Builder report alone.

Verify exact SHA, exact-head CI where required, scope, checklist IDs, active Test Area Map, real acceptance behavior, negative state/calls/writes, Production Spine, contract map, false-PASS scan, validated-object continuity, terminal/system-readiness claims, external-call evidence, protected invariants, complete diff, machine gate, and truthful authorization/release state.

Return PASS only when every mandatory condition for the declared result is directly proven. Otherwise return BLOCKED or GOVERNANCE HOLD with exact failed evidence.

If the Builder and Auditor are the same agent/context, label the audit `SELF_AUDIT`; it does not satisfy a repository rule requiring independence.

## 30. Correction and escaped-proof regression

On failure, map to the owning checklist ID/boundary/test area, correct the smallest governed boundary, repair direct proof first when the claim was unproven, rerun narrow and affected checks, then terminal verification and exact-head audit.

If a production defect escaped earlier green proof, fix both the production defect and the proof system that allowed the false PASS. A producer/consumer escape updates the contract map and acceptance harness.

## 31. Governed states

- `SECTION PASS`
- `CODE VERIFIED`
- `STAGING CANDIDATE`
- `CODE VERIFIED / GOVERNANCE HOLD`
- `RELEASE READY`
- `BLOCKED`

Never infer merge, deployment, activation, or release authorization from green tests.

## 32. New-application vertical-spine rule

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

## 33. Monorepo and multi-component rule

For each change:

1. identify affected components from the Project Adapter/discovery;
2. identify shared contracts and consumers;
3. select narrow tests from affected components;
4. run shared-boundary tests when they can be invalidated;
5. defer unrelated expensive full-workspace tests until terminal verification unless repository governance requires otherwise;
6. prove cross-component handoffs for T2+ changes.

Do not assume the repository root is the only build/test boundary.

## 34. Automation and efficiency

Automate stable repeatable rules where feasible: project discovery facts, adapter staleness checks, preflight, protected-work checks, permitted/prohibited diff, invariants, schema/migration checks, generated artifacts, external-call guards, test-area commands, affected integration, full regression, production acceptance, recovery tests, exact-head CI lookup, PR state, machine release gate, and final evidence collection.

Default WIP: one active governed change, one active correction package, zero unplanned files unless explicitly authorized.

## 35. Mandatory final report

```text
GOVERNED CHANGE REPORT
Skill version: 2.2.0
Change ID:
Change Tier:
Release intent:
Objective:
Repository:
Project Adapter version / verified SHA:
Starting SHA:
Final SHA:
PR:
Exact files changed:
Agent roster / audit separation:

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
External-call evidence:
Working tree / PR / release state:

CHANGE RESULT: PASS / BLOCKED
SYSTEM READINESS: NOT ASSESSED / BLOCKED / READY
FINAL STATUS: CODE VERIFIED / STAGING CANDIDATE / GOVERNANCE HOLD / RELEASE READY / BLOCKED
```

No prose-only completion, hidden failed requirements, confidence in place of proof, local substitute for mandatory exact-head CI, or unearned release claim.

## 36. Global invocation contract

A reliable installation includes a global/project rule equivalent to:

```text
For every qualifying coding change, invoke governed-coding-upgrade before editing.
Inspect the repository and verify the Project Adapter. Classify Change Tier and Release
Intent. Select only applicable Test Areas, but do not convert unknowns into N/A. Use
agent roles when they improve separation; do not multiply agents without value. Trace
Production Spine and Producer → Contract → Consumer handoffs for cross-boundary work.
Freeze acceptance before implementation. Reject false-PASS proof. Execute dependent
sections sequentially. Challenge the proof before terminal acceptance. Do not call a
scoped PASS production-ready without terminal-path and full-system readiness proof.
Do not claim RELEASE READY unless required machine gate, exact-head CI, audit, and
authorization pass.
```

## 37. Self-check

Before final closure, verify from evidence that starting state, pre-existing work, Project Discovery, adapter validity, Change Tier, Release Intent, agent-role truthfulness, active Test Area Map, Production Spine, contract map, acceptance freeze, false-PASS scan, frozen scope, sequential section proof, challenge findings, real-path acceptance, controlled external-call evidence, fail-closed paths, validated-object continuity, repository-owned requirements, durability/recovery, cross-section integration, terminal promise, system readiness when claimed, protected invariants, exact changed-file scope, complete diff, machine gate, exact-head CI, audit separation/result, escaped-proof correction, and truthful release state satisfy the declared result.

If controlled code verification passes but a mandatory external release condition is unavailable, report `CODE VERIFIED / GOVERNANCE HOLD`. If any repository-controlled mandatory condition is unproved or failed, report `BLOCKED`.