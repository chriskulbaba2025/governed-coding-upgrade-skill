---
name: governed-coding-upgrade
description: >-
  Mandatory governed execution and production-closure protocol for any task that
  changes source code, tests, schemas, dependencies, configuration,
  infrastructure-as-code, build/release logic, migrations, or runtime behavior.
  Use for features, defects, refactors, upgrades, migrations, security fixes,
  corrective work, and production-readiness closure. Requires verified starting
  state, frozen checklist IDs, direct executable proof, real-path acceptance with
  controlled dependencies, fail-closed negative proof, exact-head independent
  audit, governed correction, and evidence-based closure before merge or release.
---

# Governed Coding Upgrade Skill v1.1.0 — Production Closure

**Version:** 1.1.0  
**Status:** Governing execution skill  
**Machine-facing skill name:** `governed-coding-upgrade`  
**Compatibility:** The invocation name remains stable across versions.  
**Scope:** Any repository change that can alter executable behavior, runtime contracts, build/release behavior, tests, schemas, dependencies, infrastructure-as-code, configuration, persistence, or generated application output.

## 0. Governing intent

This skill converts coding work from an informal edit/test cycle into a deterministic governed change protocol.

Every ordinary governed change follows:

**INTAKE → PREFLIGHT → PROFILE → FROZEN CHECKLIST → BUILD → VERIFY → EXACT-HEAD AUDIT → CORRECT → RE-AUDIT → CLOSE**

When the user asks to finish a production-readiness correction, close all known defects, make the complete path work, or continue until clean, activate **PRODUCTION CLOSURE MODE**:

**INTAKE → PREFLIGHT → CLOSURE CHECKLIST → PROVE FAILURES → IMPLEMENT REPOSITORY-OWNED DEPENDENCIES → INTEGRATED VERIFY → EXACT-HEAD AUDIT → CONSOLIDATED CORRECTION → RE-AUDIT → CLOSE**

The skill has six non-negotiable properties:

1. Scope is explicit and frozen before implementation.
2. Completion is proved by executable evidence, not prose or confidence.
3. Acceptance exercises the real production implementation with controlled dependencies.
4. Repository-owned missing infrastructure is implementation work, not a final blocker.
5. The implementation cannot authorize its own release.
6. A change is not complete until the exact final head is independently audited.

Speed is optimized by reducing rediscovery, fragmented fixes, repeated prompts, avoidable correction rounds, and manual checks. Speed never overrides product, security, data, evidence, compatibility, rollback, cost, or release invariants.

---

# 1. Mandatory invocation rule

Invoke this skill for any intentional change to:

- application or service code;
- tests or acceptance harnesses;
- APIs or schemas;
- database schemas or migrations;
- persistence or durable job state;
- dependencies or lockfiles;
- executable configuration;
- infrastructure-as-code;
- CI/CD, build, packaging, deployment, or release logic;
- security controls;
- data transformations;
- generated application/report behavior;
- defect corrections and production-readiness work.

Do not bypass governance because the change appears small.

Read-only inspection or explanation does not require the full lifecycle unless repository governance says otherwise.

---

# 2. Authority and precedence

Resolve authority in this order before editing:

1. Platform, safety, legal, privacy, and security constraints.
2. Explicit user instruction for the current task and authorization boundaries.
3. Repository governance and security rules.
4. Product, API, schema, persistence, data, compatibility, and release contracts.
5. Protected invariants, golden masters, and reference artifacts.
6. This skill.
7. Repository Governed Change Profile.
8. Frozen checklist.
9. Implementation notes or model suggestions.

A lower-level instruction cannot override a higher-level rule.

When authoritative sources conflict and the conflict changes implementation or proof requirements, use the blocked protocol.

---

# 3. Governed Change Profile

Use the first repository-governed location that fits local conventions. If none exists, prefer:

```text
.governance/GOVERNED_CHANGE_PROFILE.md
```

The profile records repository-specific facts rather than hard-coding them into this skill.

Required fields where applicable:

```text
Repository root:
Primary branch:
Runtime/build system:
Test framework:
Narrow-test command:
Acceptance/integration command:
Full-regression command:
Type/static/build commands:
Scope/diff check:
Security/secret scan:
Migration policy:
Persistence policy:
Live external-call policy:
CI exact-head verification method:
Merge/release authorization rule:
Rollback/recovery mechanism:
Protected invariant registry:
Canonical governance sources:
```

Unknown facts are `UNRESOLVED`, never guessed.

Protected invariant classes include interface, data, state, security, evidence, output, compatibility, cost/external, release, and performance.

---

# 4. Change classification

Choose one primary class:

- `DEFECT`
- `FEATURE`
- `REFACTOR`
- `MIGRATION`
- `DEPENDENCY`
- `SECURITY`
- `PERFORMANCE`
- `CONFIGURATION`
- `CORRECTION`
- `PRODUCTION_CLOSURE`

Use `PRODUCTION_CLOSURE` when the task is to close a set of known production-readiness defects that collectively prevent a real end-to-end path from satisfying its contracts.

Do not split one production-path root cause into artificial future work merely to obtain a PASS.

---

# 5. Gate 0 — Intake

Before code changes:

- [ ] State one measurable objective.
- [ ] Classify the change.
- [ ] Identify governing sources.
- [ ] Identify protected invariants.
- [ ] Identify upstream and downstream boundaries.
- [ ] Determine whether executable behavior changes.
- [ ] Determine whether migrations or compatibility obligations exist.
- [ ] Determine whether live external services are permitted.
- [ ] Determine whether merge/deploy/release is authorized.
- [ ] For production closure, enumerate all currently known blockers on the same production path.

Production closure objective form:

```text
Make <production path> satisfy <governing contracts> from <entry boundary>
through <terminal boundary>, and prove it with deterministic controlled tests.
```

---

# 6. Gate 1 — Repository preflight

Verify actual repository state:

```text
Repository root:
Current branch:
HEAD SHA:
Working tree status:
Remote identity when relevant:
Active PR when relevant:
Governance sources:
Governed Change Profile:
```

Rules:

- Starting SHA mismatch is a stop condition.
- Never infer repository identity when it can be inspected.
- Never reset, discard, overwrite, stage, or commit pre-existing user work without authorization.

## 6.1 Dirty-tree continuation rule

A dirty working tree is not automatically a blocker when the user explicitly asks to continue the current correction and the modifications belong to that correction.

In that case:

1. capture `git status`, `git diff --stat`, and complete `git diff`;
2. map each existing modification to a checklist ID;
3. preserve valid work;
4. correct invalid work in place;
5. do not create an artificial clean baseline by resetting or stashing the user's active correction.

An unexplained or unrelated dirty-tree conflict remains a blocker.

---

# 7. Gate 2 — Freeze the scope

Group confirmed requirements sharing the same responsibility, contract, state transition, schema, storage path, adapter boundary, API surface, security boundary, acceptance harness, or failure mode.

Define:

```text
Permitted files:
- exact files or bounded path patterns

Prohibited files:
- protected files or path patterns
```

A permitted pattern must be narrow enough to detect unrelated edits.

For ordinary changes, unresolved architecture decisions affecting implementation must equal zero before build.

For `PRODUCTION_CLOSURE`, a repository-owned missing boundary discovered during implementation may be added to the closure checklist when it is strictly required to satisfy an already-governed production-path requirement. It is not deferred merely because it requires a new schema, migration, table, worker, validator, transport abstraction, endpoint, cache, or test harness.

---

# 8. Gate 3 — Frozen checklist

Create the checklist before new implementation.

Preferred path when no stronger convention exists:

```text
.governance/changes/<CHANGE-ID>_CHECKLIST.md
```

Every item contains:

| Field | Requirement |
|---|---|
| ID | Stable identifier |
| Requirement | One observable behavior or repository condition |
| Boundary | Exact file/function/module/schema/config surface |
| Positive proof | Exact assertion, command, artifact, state, output, or diff evidence |
| Negative proof | Required when failure/absence matters |
| Acceptance proof | Real-path proof where applicable |
| Protected invariant | Preserved or intentionally versioned invariant |
| Failure result | Exact fail-closed result |
| Final evidence | Evidence required in the close report |
| Status | `[ ]` or `[x]` only |

Checklist rules:

- one behavior per item;
- no aspirational language;
- no item without direct proof;
- no proof based only on comments, test names, source searches, or green CI;
- no `A OR B` when only one governed result is correct;
- no hidden requirements outside checklist IDs;
- no moving governing requirements into `known limitations`.

Observable requirement form:

```text
Given <precondition>, when <operation>, then <exact result>,
and <prohibited result> does not occur.
```

---

# 9. Gate 4 — Proof-first build

Required order:

1. Re-run preflight.
2. Add or correct direct proof for each checklist item.
3. Reproduce each defect with a failing proof when technically safe and feasible.
4. Implement the complete frozen checklist.
5. Run narrow tests until green.
6. Run acceptance/integration against the real production path.
7. Run type/static/security/build checks where applicable.
8. Run persistence/migration/recovery checks where applicable.
9. Run full regression.
10. Run protected-invariant checks.
11. Run scope check.
12. Inspect the complete diff.
13. Commit/push according to repository governance.

Do not return a completion report while a required item is open or failing.

---

# 10. Real production path acceptance

Acceptance must prove production behavior, not a hand-written imitation.

When external providers are involved, prefer:

```text
real production adapter
+
injected controlled transport/client
+
production validator
+
real normalization/artifact/persistence boundary
+
real orchestrator/service boundary
```

Controlled fixtures may emulate provider responses. The adapter/orchestrator under test must be the production implementation.

Do not fabricate a successful normalized result and inject it downstream as proof that the production adapter works.

Measure exact call counts whenever idempotency, retry, paid tasks, polling, writes, or side effects matter.

Live paid/provider/LLM calls are zero in tests and CI unless explicitly authorized by the frozen checklist and governing sources.

---

# 11. Validation-before-transition rule

Whenever an artifact or contract controls persistence, lifecycle advancement, rendering, publication, or exposure:

```text
assemble complete object
→ validate complete object
→ persist/advance/use the validated object
```

Do not validate a partial object and add production fields afterward.

If a renderer or downstream consumer must receive the validated model, prove exact equality or identity at that boundary.

Malformed `AVAILABLE`, `SUCCESS`, `READY`, or equivalent states must fail closed rather than being promoted into usable canonical evidence.

---

# 12. Negative-path and fail-closed proof

For governed failure behavior, prove all applicable dimensions:

```text
operation rejects/fails with governed classification
AND
persisted state equals governed failure state
AND
prohibited later events do not exist
AND
prohibited later calls equal zero
AND
prohibited artifacts/writes do not exist
AND
protected prior state remains unchanged where required
```

Throwing an exception alone is insufficient.

Every confirmed production defect and every independently discovered false-positive proof adds a permanent regression test or executable guard when technically feasible.

---

# 13. Production Closure Mode

Production Closure Mode exists for work where repeated partial audits would otherwise keep rediscovering repository-owned missing boundaries.

## 13.1 Single closure package

Convert all known defects on the same production path into one bounded checklist. Typical closure responsibilities include:

- complete request/config persistence;
- source-specific contract validation;
- real production adapters with controlled transports;
- artifact integrity and provenance;
- finding/score/output validation before state transition;
- finalization gates;
- complete validated render/view model;
- durable job execution;
- restart/recovery;
- retry classification;
- task/payment idempotency;
- abort/cancellation propagation;
- replay/cache execution;
- live-client budget and retry controls tested with fake clients;
- publication/terminal state;
- actual web/API path;
- negative proofs.

Only include responsibilities required by the product/repository contracts for the path being closed.

## 13.2 Repository-owned work is not a final blocker

The following phrases describe implementation work when the repository owns the boundary:

```text
requires DB migration
requires a new table
requires durable job state
requires source-specific schema
requires transport abstraction
requires validation module
requires endpoint
requires replay cache
requires model-client interface
requires budget gate
requires integration harness
requires recovery test
requires negative proof
```

Do not end a production-closure run with one of these as the sole blocker. Implement the required repository-owned boundary within governed scope.

## 13.3 Genuine external blockers

A final blocker is valid only when the remaining dependency cannot be created or simulated from the repository without an unavailable or prohibited external action, for example:

- unavailable credentials or account authorization;
- destructive production mutation without authorization;
- deployment or merge authorization explicitly withheld;
- a live paid provider proof explicitly forbidden and no controlled boundary can prove the repository behavior;
- an external platform capability outside repository control.

Complete every repository-controlled item first and report the smallest external action required.

## 13.4 Keep-going rule

Within Production Closure Mode, continue through repository-controlled failures:

```text
inspect
→ prove failure
→ implement
→ narrow verify
→ integrated verify
→ regression
→ exact-head audit
→ consolidated correction
→ re-audit
```

until either:

1. all closure checklist items PASS; or
2. a genuine external blocker is proved.

Do not hand ordinary repository-owned implementation gaps back to the user as a new discovery-only report.

If more than one correction round is required, perform a short process review identifying why the prior proof/checklist missed the issue, update the governed checklist if necessary, then continue the same closure objective. Do not weaken acceptance criteria.

---

# 14. Durability, restart, retry, idempotency, and abort extension

When the governed path includes background work or paid/task-based providers, add applicable checklist IDs for:

- durable execution identity and status;
- persisted checkpoints;
- recovery after process restart;
- zero repeat calls for already completed steps unless explicitly governed;
- retryable versus terminal failure classification;
- retry-budget exhaustion;
- provider task/request ID persistence before later retryable operations;
- duplicate paid-task prevention;
- AbortSignal/cancellation propagation through polling and transports;
- zero prohibited side effects after abort.

Required recovery proof pattern:

```text
start
→ persist checkpoint
→ destroy first worker/process instance
→ construct new instance
→ reload durable state
→ resume
→ complete
```

Use controlled dependencies, not live paid calls.

---

# 15. Verification matrix

Run every applicable row. `N/A` requires evidence that the repository/change has no such responsibility.

| Responsibility | Required result |
|---|---|
| Preflight | exact repo/branch/SHA/tree verified |
| Narrow tests | PASS |
| Acceptance/integration | PASS |
| Negative-path proof | PASS where applicable |
| Full regression | PASS when suite exists |
| Static/type/build | PASS when configured |
| Schema/contract validation | PASS when applicable |
| Migration/persistence | PASS when applicable |
| Restart/recovery | PASS when applicable |
| Idempotency/retry/abort | PASS when applicable |
| Security/secret scan | PASS when applicable |
| Protected invariants | PASS |
| Generated artifacts | PASS |
| Live external-call policy | PASS |
| Scope/permitted files | PASS |
| Prohibited files | untouched |
| Complete diff review | PASS |
| Exact-head CI | PASS when CI exists |

Any required failure means the change is incomplete.

---

# 16. Scope-check contract

Compare the complete changed-file set from starting SHA to final head against the frozen boundary.

Required proof:

```text
unexpected changed files == 0
prohibited changed files == 0
```

Do not rely only on `git status`; committed out-of-scope files must also be detected.

---

# 17. Independent exact-head audit

The implementation pass cannot self-authorize release.

The audit runs in a separate review context that did not author the changes and begins from repository evidence, not the implementation report.

The auditor verifies:

- exact final SHA;
- exact-head CI when applicable;
- changed-file scope;
- prohibited files untouched;
- each checklist ID maps to implementation and direct proof;
- acceptance executes the real governed path with controlled dependencies;
- failure proofs include persisted state and prohibited side effects;
- order/count/hash/identity claims are exact when governed;
- protected invariants remain intact;
- migrations/recovery obligations pass;
- no prohibited live provider/paid/LLM call occurred;
- no unmet governing requirement is hidden as a limitation;
- merge/release authorization is truthful.

Audit result is exactly:

```text
PASS
```

or:

```text
BLOCKED
Failed checklist IDs:
Evidence:
Smallest required correction:
```

No `PASS WITH NOTES` or `MOSTLY PASS`.

---

# 18. Correction protocol

If audit returns `BLOCKED`:

1. reproduce failed IDs;
2. correct missing/false proof first when appropriate;
3. correct implementation only as required by governed evidence;
4. re-run the complete applicable verification matrix;
5. re-run scope check;
6. inspect the correction diff;
7. commit/push under repository governance;
8. audit the corrected exact head independently.

For ordinary changes, one consolidated correction round is the default target; a second round requires process review.

For `PRODUCTION_CLOSURE`, process review does not end the objective. After reviewing why the prior closure proof missed the issue, continue correcting repository-owned failed IDs until PASS or a genuine external blocker is proved.

---

# 19. Close and release gate

A governed change is complete only when:

- [ ] every required checklist ID is PASS;
- [ ] every applicable verification responsibility is PASS;
- [ ] changed-file scope is exact;
- [ ] protected invariants are preserved or explicitly versioned;
- [ ] exact-head CI passes when required;
- [ ] independent exact-head audit returns PASS;
- [ ] repository/PR state matches the reported SHA;
- [ ] rollback/recovery obligations are satisfied;
- [ ] working tree is clean except explicitly protected pre-existing work;
- [ ] final evidence report is complete;
- [ ] merge/release authorization is satisfied.

If explicit merge approval is required, stop after audit PASS with:

```text
READY FOR MERGE — NOT MERGED
```

Never infer merge/deploy/release authorization from successful tests.

---

# 20. Blocked protocol

Stop and return `BLOCKED` for a material condition the current governed run cannot safely resolve, including:

- wrong repository/branch or starting SHA mismatch;
- unexplained dirty-tree conflict;
- authoritative source conflict;
- unresolved product/contract decision requiring user authority;
- required implementation would alter a prohibited invariant/file without scope authorization;
- destructive migration or production mutation lacks authorization;
- security boundary cannot be preserved;
- proof requires a prohibited live call and no controlled repository boundary can establish the required behavior;
- required external credential/account authorization is unavailable;
- exact-head audit/CI cannot be established where mandatory;
- merge/deploy/release authorization is absent for that action.

Do not use the blocked protocol merely because repository-owned infrastructure must be added to satisfy an already-governed requirement.

Return:

```text
BLOCKED
Reason:
Failed/affected checklist ID:
Exact evidence:
Repository-controlled work completed:
Smallest external decision/action required:
```

---

# 21. Automation requirements

Automate stable repeatable rules where technically reasonable:

- repo/branch/SHA preflight;
- dirty-tree/protected-work check;
- permitted/prohibited diff check;
- invariant/golden/reference hash checks;
- schema and migration checks;
- generated-artifact checks;
- secret/live-call scans;
- full regression;
- production-path acceptance;
- restart/recovery tests;
- exact-head CI lookup;
- PR state checks;
- final evidence collection.

Preferred responsibility interface when repository conventions permit:

```text
change:preflight
change:test
change:acceptance
change:scope-check
change:verify
change:audit-support
```

Any failure exits non-zero.

---

# 22. Efficiency and work-in-progress rules

Persist stable repository facts in the Governed Change Profile to avoid repeated discovery.

Execution prompts contain only current scope, governing sources, checklist IDs, executable proof, boundaries, required commands, and final output.

Exclude future work, motivational prose, optional cleanup, repeated architecture summaries, and confidence scores used as proof.

Default WIP:

```text
active governed change packages: 1
active correction package: 1
unplanned changed files: 0
```

---

# 23. Process performance record

When comparable baseline data exists, record:

```text
Change ID:
Change class:
Baseline active cycle time:
Actual active cycle time:
Cycle-time reduction:
First-pass checklist pass rate:
Correction rounds:
False-positive proofs found:
Unplanned files changed:
Preventable CI reruns:
Repeated manual check to automate next:
```

Default adoption target: at least 55% lower active cycle time than the prior comparable fragmented process, without weakening acceptance quality.

Do not claim speed improvement without measurement.

---

# 24. Mandatory final report

Use evidence, not narrative completion claims:

```text
GOVERNED CHANGE REPORT

Skill version: 1.1.0
Change ID:
Change class:
Objective:
Repository:
Starting branch:
Starting SHA:
Final SHA:
PR:

Exact files changed:
- ...

CHECKLIST
[x] CHANGE-ID-01 — PASS — exact evidence
[ ] CHANGE-ID-02 — FAIL — exact evidence

VERIFICATION
[x] preflight — PASS — evidence
[x] narrow tests — PASS — command/result
[x] acceptance — PASS/N/A — evidence
[x] negative proofs — PASS/N/A — evidence
[x] persistence/migration/recovery — PASS/N/A — evidence
[x] full regression — PASS/N/A — evidence
[x] invariant checks — PASS — evidence
[x] scope check — PASS — unexpected 0; prohibited 0
[x] exact-head CI — PASS/N/A — exact SHA

AUDIT
Independent exact-head audit: PASS/BLOCKED
Audit head SHA:
Correction rounds:

EXTERNAL EFFECTS
Live provider calls:
Live LLM calls:
Paid task calls:
Production mutations:

REPOSITORY STATE
Working tree:
PR state:
Merge/deploy/release state:
Rollback/recovery state:

FINAL STATUS:
PASS — READY FOR AUTHORIZED MERGE/RELEASE
or
BLOCKED — exact failed IDs and genuine external evidence
```

Rules:

- no prose-only completion claim;
- no confidence percentage in place of proof;
- no hidden failed requirement under `known limitations`;
- no PASS while a required item is open or failing;
- no claim of merge/deploy/release unless it actually occurred.

---

# 25. Production closure prompt template

Use [`templates/PRODUCTION_CLOSURE_TEMPLATE.md`](templates/PRODUCTION_CLOSURE_TEMPLATE.md) when a repository has accumulated multiple production-readiness defects and the objective is to close the real path rather than perform another discovery-only audit.

---

# 26. Global invocation contract

A skill is not reliably installed unless the coding environment also contains a global/project rule equivalent to:

```text
For every task that changes code, tests, schemas, dependencies, executable
configuration, infrastructure-as-code, build/release logic, migrations, or
runtime behavior, invoke and obey `governed-coding-upgrade` before editing.
For production-readiness closure, do not stop on repository-owned missing
infrastructure; implement and prove the governed path until PASS or a genuine
external blocker remains. Do not merge/deploy/release without authorization.
```

---

# 27. Self-check before PASS

Every required answer must be YES from evidence:

```text
Was the exact starting state verified?
Was pre-existing work protected?
Was scope/checklist frozen?
Does every checklist ID have direct proof?
Did acceptance execute the real production implementation with controlled dependencies?
Did malformed/negative paths fail closed where applicable?
Were repository-owned dependencies implemented rather than relabeled as blockers?
Were restart/recovery/idempotency/abort obligations proved where applicable?
Were protected invariants preserved?
Were unexpected changed files exactly zero?
Was the complete diff inspected?
Was the exact final head independently audited?
Were audit failures corrected and re-audited?
Is merge/deploy/release state reported truthfully?
Are all required checklist items PASS?
```

If any required answer is NO, final status is `BLOCKED`.