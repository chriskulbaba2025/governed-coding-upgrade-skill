---
name: governed-coding-upgrade
description: >-
  Governed execution and production-readiness protocol for coding changes.
---

# Governed Coding Upgrade Skill v2.1.0 — Production Spine + Sequential Evidence

**Version:** 2.1.0  
**Machine-facing skill name:** `governed-coding-upgrade`  
**Status:** Governing execution skill

## Governing purpose

GCU turns coding changes into a deterministic, evidence-based lifecycle. It preserves the v1.2 sequential execution, interruption-resume, balanced verification, Production Closure, machine-gate, and Governance Hold controls, while adding the v2 production-correctness model.

Standard lifecycle:

```text
INTAKE
→ PREFLIGHT
→ RELEASE INTENT
→ PRODUCTION SPINE / CONTRACT MAP when applicable
→ ACCEPTANCE FREEZE
→ FROZEN CHECKLIST
→ SEQUENTIAL BUILD / VERIFY
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
7. repository Governed Change Profile;
8. frozen checklist and acceptance contract;
9. implementation notes.

A lower layer cannot override a higher layer.

## 2. Mandatory invocation

Invoke this skill for intentional changes to source, tests, schemas, APIs, dependencies, executable configuration, migrations, persistence, jobs, external integrations, security controls, infrastructure, build/release logic, or production behavior.

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
Governed Change Profile
authorization boundaries
```

Starting-SHA mismatch is a stop condition. Never discard pre-existing user work without authorization.

### Dirty-tree continuation

When the user explicitly asks to continue the same correction, preserve valid existing work: inspect status and diff, map changes to checklist IDs, correct in place, and do not reset merely to create a clean baseline.

### Interrupted-agent resume

After an agent/API/terminal interruption, resume the same repository and branch, inspect HEAD/diff/checklist/test evidence, identify the last directly proven section, preserve valid work, and continue from the first unproven or failing section.

## 4. Release intent

Declare exactly one before implementation:

- `CHANGE_ONLY` — prove the scoped change only.
- `STAGING_READY` — prove the scoped change plus governed staging conditions.
- `PRODUCTION_READY` — prove the complete production path through the terminal user/business promise and all applicable system-readiness conditions.

A green scoped change cannot be silently upgraded into production readiness.

## 5. Governed Change Profile

Use the repository’s governed location or `.governance/GOVERNED_CHANGE_PROFILE.md`.

Record applicable facts:

```text
repository/build/runtime/test systems
narrow and affected-integration commands
acceptance and full-regression commands
static/type/build/security commands
scope/diff and generated-artifact checks
migration and persistence/recovery policies
external-call policy and controlled-test policy
release-intent policy
production-spine record path
Producer → Contract → Consumer map path
acceptance-freeze path
false-PASS scan method
terminal promise definition
full-system readiness method
machine-gate command
exact-head CI verification
merge/release authorization
rollback/recovery mechanism
protected invariants
canonical governance sources
```

Unknown material facts are `UNRESOLVED`, never guessed.

## 6. Production Spine gate

For cross-boundary production work, trace the real path before implementation:

```text
user/UI/API entry
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

For each hop record the production module, input/output contract, state/artifact, failure behavior, retry/idempotency effect, tenant/account implication, and direct proof.

Do not implement while a material production-spine hop required by the declared release intent is unresolved. A green isolated component does not prove the spine.

## 7. Producer → Contract → Consumer map

For each material runtime handoff record:

| Producer | Produced object/state | Contract/schema | Validation point | Consumer | Consumer requirements | Failure result | Proof |
|---|---|---|---|---|---|---|---|

Rules:

- producer must actually emit the fields/semantics the consumer requires;
- validation happens before governed persistence, transition, rendering, publication, authorization, exposure, or irreversible side effects;
- consumer uses the validated object/state rather than an ungoverned reconstruction when exact continuity is required;
- defaults cannot convert malformed usable data into valid-looking empty data;
- tenant/account/security identity remains attached across authorization-relevant boundaries;
- an escaped producer/consumer defect requires correction of both implementation and proof map.

## 8. Freeze scope and checklist

Define explicit permitted and prohibited files. Create a frozen checklist before implementation. Preferred path:

```text
.governance/changes/<CHANGE-ID>_CHECKLIST.md
```

Every checklist item has a stable ID, one observable requirement, exact boundary, positive proof, negative proof when applicable, real-path acceptance proof, protected invariant, exact failure result, final evidence, and binary status.

No aspirational requirements, hidden requirements, prose-only proof, or `A OR B` result when one governed result is required.

## 9. Acceptance contract freeze

Before production implementation, freeze:

```text
entry boundary
real production modules executed
controlled dependency seam
production validators/contracts
persisted state/artifacts inspected
terminal positive result
negative/fail-closed result
prohibited later calls/events/writes
external-call ceiling
exact verification command
```

When safe and technically feasible, obtain failing proof before the implementation intended to make it pass.

### False-PASS scan

Reject proof that depends on unconditional assertions, always-valid validators, fabricated normalized success replacing the production producer, pre-seeded terminal/intermediate states that bypass the path under proof, persistence doubles that bypass required persistence semantics, unused counters, comments/test names/source searches as sole evidence, hardcoded external-call/cost claims, local substitutes for mandatory exact-head CI, or mocks placed above the production boundary being proved.

A false-PASS test is a defect in the proof system.

## 10. Sequential Evidence Gate

For ordered multi-section work:

```text
INSPECT
→ DEFINE PROOF
→ REPRODUCE FAILURE when safe/feasible
→ IMPLEMENT COMPLETE SECTION
→ NARROW VERIFY
→ SECTION AUDIT
→ AUTO-CONTINUE ON PASS
```

A section passes only when the requirement, real path where applicable, direct positive proof, required negative proof, and affected earlier boundaries all pass. Correct failed sections before dependent work proceeds. Routine section PASS does not require user approval unless the next action crosses an explicit authorization boundary.

## 11. Balanced verification

Use three layers:

1. narrow section checks;
2. affected integration checks only when a boundary can be invalidated;
3. one terminal verification after all sections pass: cross-section review, full acceptance, full regression, static/type/build/security checks, persistence/recovery checks, invariant/scope checks, complete diff review, and machine gate.

Do not run the most expensive suite after every isolated section unless governance requires it.

## 12. Real production path acceptance

Acceptance proves production behavior, not a hand-written imitation.

Preferred shape:

```text
real production adapter/service
+
controlled dependency below that boundary
+
production validator
+
real normalization/persistence/artifact boundary
+
real orchestrator/web/service path
```

Controlled fixtures may emulate external responses. Production modules being claimed must execute. Do not inject fabricated successful normalized output downstream as proof the producer works.

Measure exact calls/writes/tasks when retries, idempotency, cost, polling, or side effects matter.

## 13. Evidence preservation

When external/raw evidence drives decisions, preserve:

```text
raw response/reference
→ governed raw artifact
→ real production normalizer/adapter
→ validated evidence contract
→ persisted canonical evidence
→ downstream decision/render consumer
```

Prove provenance, field preservation, validation, canonical persistence, governed consumer loading, and that fallback/replay/cache paths cannot bypass validation or fabricate evidence.

## 14. External-call contract

Tests and CI use zero live paid/provider/model calls unless explicitly authorized.

Where applicable define operation identity, task/request ID persistence, timeout, retry classification, attempt/budget ceiling, backoff, cancellation, resume/recovery, task reuse, duplicate-charge prevention, controlled dependency, and measured call/cost counters.

A retryable failure after task creation must not create a second paid task unless the provider contract explicitly requires it.

Controlled tests should isolate real credentials where technically feasible and fail unexpected live execution.

## 15. Single validated-object rule

For governed persistence, lifecycle, rendering, publication, authorization, delivery, or exposure:

```text
assemble complete object
→ validate complete object
→ retain/freeze validated object when applicable
→ persist/advance/render/publish/authorize/consume that validated object
```

Do not validate a partial object and add required fields afterward. Do not validate object A and consume an independently reconstructed object B when continuity is governed.

Malformed usable states fail closed. Missing planned evidence is not invented as a legitimate unavailable state unless the governed collection path actually produced that state.

## 16. Negative-path proof

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

## 17. Production Closure Mode

Use when known production-readiness defects collectively block one end-to-end path.

One closure package may include request/config persistence, source contracts, production adapters, artifact integrity, validation gates, durable jobs, restart/recovery, retries, idempotency, cancellation, replay/cache paths, publication, terminal retrieval, authorization/tenant isolation, and negative proof when required by governing contracts.

Repository-owned required infrastructure is implementation work, not a final blocker. A genuine external blocker is outside repository control and cannot be safely created or simulated, such as unavailable account authorization, prohibited destructive production action, mandatory external platform outage, or withheld merge/deployment authorization.

Complete repository-controlled work first.

## 18. Durable-job contract

For background/asynchronous work, persist enough state before asynchronous acceptance to resume the exact operation without reconstructing required inputs from defaults. Applicable data includes operation identity, tenant/account identity, normalized request/config, checkpoint/state, external task IDs, retry classification, artifact references, and terminal/failure result.

Prove recovery from a fresh process/runtime, zero repeat calls for completed steps unless governed, retry classification/budget, task reuse, duplicate-work prevention, cancellation propagation, and zero prohibited side effects after abort.

## 19. Cross-section review

After sections pass, inspect each edge:

```text
upstream governed output → contract/validation → downstream consumer
```

Confirm the consumer receives the exact governed result, does not bypass validation, and does not mutate required fields after proof. Correct defects in the owning section and rerun affected later sections.

## 20. Terminal-path gate

For `STAGING_READY` or `PRODUCTION_READY`, identify the terminal user/business promise and prove the same governed execution reaches it.

Intermediate states such as authenticated, queued, rendered, or approved are not terminal when later required authorization, persistence, publication, delivery, or retrieval remains.

```text
real entry
→ governed intermediate boundaries
→ terminal state/artifact
→ final retrieval/observable outcome
```

## 21. Change PASS is not Production Ready

Report separately:

```text
CHANGE RESULT: PASS / BLOCKED
RELEASE INTENT: CHANGE_ONLY / STAGING_READY / PRODUCTION_READY
SYSTEM READINESS: NOT ASSESSED / BLOCKED / READY
```

### Full-system production-readiness gate

For `PRODUCTION_READY`, verify every applicable responsibility: real production composition, persistence/migrations, authentication/authorization/tenant isolation, secrets handling, executable contracts, production adapters with controlled acceptance dependencies, durable jobs/recovery/retry/idempotency/cancellation, external-call cost controls, canonical artifact/evidence integrity, governed downstream consumers, rendering/publication/delivery/final retrieval, negative cross-account access when applicable, required observability, rollback/recovery, no fabricated success on the proven path, no remaining repository-controlled blocker, exact-head CI, machine gate, independent audit, and required authorization.

`N/A` requires direct evidence.

## 22. Machine release gate

The coding agent is not the release authority. A repository gate such as `change:release-gate` evaluates machine-enforceable conditions against the exact candidate head and exits non-zero for failed, missing, stale, or unprovable mandatory conditions.

Agent prose, confidence, local substitutes, or environmental explanations cannot override the gate.

When mandatory exact-head CI is temporarily unavailable while controlled local verification passes, report:

```text
CODE VERIFIED / GOVERNANCE HOLD
```

Local reruns do not substitute for mandatory exact-head CI.

## 23. Independent exact-head audit

The auditor inspects the actual candidate commit, not the implementation report alone. Verify exact SHA, exact-head CI, scope, every checklist ID, real acceptance behavior, negative state/calls/writes, production spine, contract map, false-PASS scan, validated-object continuity, terminal-path/system-readiness claims, measured external-call evidence, protected invariants, complete diff, machine gate, and truthful authorization/release state.

Return PASS only when every mandatory condition for the declared result is directly proven; otherwise return BLOCKED or GOVERNANCE HOLD with exact failed evidence.

## 24. Correction and escaped-proof regression

On failure, map to the owning checklist ID/boundary, correct the smallest governed boundary, repair direct proof first when the claim was unproven, rerun narrow and affected checks, then terminal verification and exact-head audit.

For ordinary changes, one consolidated correction round is the default target; a second requires process review. Production Closure continues through repository-owned failures until PASS or a genuine external blocker.

If a production defect escaped earlier green proof, fix both the production defect and the proof system that allowed the false PASS. A producer/consumer escape updates the contract map and acceptance harness.

## 25. Governed states

- `SECTION PASS`
- `CODE VERIFIED`
- `STAGING CANDIDATE`
- `CODE VERIFIED / GOVERNANCE HOLD`
- `RELEASE READY`
- `BLOCKED`

Never infer merge, deployment, activation, or release authorization from green tests.

## 26. New-application vertical-spine rule

For a new application or major greenfield subsystem, prove one real vertical slice early:

```text
one real entry
→ auth/tenant boundary when applicable
→ one persisted domain operation
→ one real processing/service path
→ one terminal output/retrieval path
→ controlled acceptance PASS
```

Do not build many isolated green components while the first end-to-end slice remains unproven.

## 27. Automation and efficiency

Automate stable repeatable rules where feasible: preflight, protected-work checks, permitted/prohibited diff, invariants, schema/migration checks, generated artifacts, external-call guards, section tests, affected integration, full regression, production acceptance, recovery tests, exact-head CI lookup, PR state, machine release gate, and final evidence collection.

Default WIP: one active governed change, one active correction package, zero unplanned files.

Balanced verification and interruption resume reduce cycle time without weakening proof.

## 28. Mandatory final report

```text
GOVERNED CHANGE REPORT
Skill version: 2.1.0
Change ID:
Change class:
Release intent:
Objective:
Repository:
Starting SHA:
Final SHA:
PR:
Exact files changed:

Production spine: PASS/N/A — evidence
Contract map: PASS/N/A — evidence
Acceptance freeze: PASS/N/A — evidence
False-PASS scan: PASS — evidence
Terminal-path gate: PASS/N/A — evidence
Full-system readiness: PASS/N/A — evidence

Checklist/section results:
Verification commands/results:
Scope result:
Machine gate:
Exact-head CI:
Independent exact-head audit:
External-call evidence:
Working tree / PR / release state:

CHANGE RESULT: PASS / BLOCKED
SYSTEM READINESS: NOT ASSESSED / BLOCKED / READY
FINAL STATUS: CODE VERIFIED / STAGING CANDIDATE / GOVERNANCE HOLD / RELEASE READY / BLOCKED
```

No prose-only completion, hidden failed requirements, confidence in place of proof, local substitute for mandatory exact-head CI, or unearned release claim.

## 29. Global invocation contract

A reliable installation includes a global/project rule equivalent to:

```text
For every qualifying coding change, invoke governed-coding-upgrade before editing.
Declare release intent. Trace the production spine and Producer → Contract → Consumer
handoffs for cross-boundary work. Freeze acceptance before implementation. Reject
false-PASS proof. Execute multi-section work sequentially. Use controlled dependencies
below real production boundaries. Do not call a scoped PASS production-ready without
terminal-path and full-system readiness proof. Do not claim RELEASE READY unless the
machine gate, exact-head CI, independent audit, and authorization pass.
```

## 30. Self-check

Before final closure, verify from evidence that starting state, pre-existing work, release intent, production spine, contract map, acceptance freeze, false-PASS scan, frozen scope, sequential section proof, real production acceptance, controlled external-call evidence, fail-closed paths, validated-object continuity, repository-owned requirements, durability/recovery, cross-section integration, terminal promise, system readiness when claimed, protected invariants, exact changed-file scope, complete diff, machine gate, exact-head CI, independent audit, escaped-proof correction, and truthful release state all satisfy the declared result.

If controlled code verification passes but a mandatory external release condition is unavailable, report `CODE VERIFIED / GOVERNANCE HOLD`. If any repository-controlled mandatory condition is unproved or failed, report `BLOCKED`.
