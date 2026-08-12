---
name: governed-coding-upgrade
description: >-
  Mandatory governed execution and production-closure protocol for coding changes.
  Requires verified starting state, frozen checklist IDs, sequential evidence gates,
  real-production-path acceptance with controlled dependencies, fail-closed proof,
  balanced machine verification, exact-head independent audit, and a non-overridable
  terminal release gate before governed completion.
---

# Governed Coding Upgrade Skill v1.2.0 — Sequential Evidence Gates

**Version:** 1.2.0  
**Status:** Governing execution skill  
**Machine-facing skill name:** `governed-coding-upgrade`  
**Compatibility:** Backward-compatible with v1.x invocation and repository profiles.  
**Scope:** Any repository change that can alter source code, tests, schemas, dependencies, executable configuration, infrastructure-as-code, build/release logic, migrations, persistence, runtime contracts, generated application output, or production behavior.

## 0. Governing intent

This skill converts coding work from an informal edit/test loop into a deterministic governed change protocol.

Ordinary governed changes follow:

**INTAKE → PREFLIGHT → PROFILE → FROZEN CHECKLIST → BUILD → VERIFY → EXACT-HEAD AUDIT → CORRECT → RE-AUDIT → CLOSE**

When the user asks to finish production readiness, close all known defects, make the complete path work, or continue until clean, activate **PRODUCTION CLOSURE MODE**:

**INTAKE → PREFLIGHT → CLOSURE CHECKLIST → SEQUENTIAL EVIDENCE GATES → CROSS-SECTION VERIFY → TERMINAL MACHINE GATE → EXACT-HEAD AUDIT → CORRECT → RE-AUDIT → CLOSE**

The skill has eight non-negotiable properties:

1. Scope is explicit and frozen before implementation.
2. Every requirement has a stable checklist ID and direct executable proof.
3. Complex closure work is evaluated section by section before later sections proceed.
4. Acceptance executes the real production implementation with controlled dependencies.
5. Malformed or missing governed evidence fails closed rather than being fabricated or silently downgraded.
6. Repository-owned missing infrastructure is implementation work, not a final blocker.
7. The implementation cannot authorize its own release or override a failed machine gate.
8. Governed completion requires the exact final head to satisfy every mandatory release condition.

Speed is improved by reducing rediscovery, fragmented fixes, repeated broad regression runs, avoidable correction rounds, and manual checks. Speed never overrides product, security, privacy, data, evidence, compatibility, rollback, cost, release, or authorization invariants.

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

Read-only inspection or explanation does not require the full lifecycle unless repository governance says otherwise.

---

# 2. Authority and precedence

Resolve authority in this order before editing:

1. Platform, safety, legal, privacy, and security constraints.
2. Explicit user instruction and current authorization boundaries.
3. Repository governance and security rules.
4. Product, API, schema, persistence, data, compatibility, and release contracts.
5. Protected invariants, golden masters, and reference artifacts.
6. This skill.
7. Repository Governed Change Profile.
8. Frozen checklist.
9. Implementation notes or model suggestions.

A lower-level instruction cannot override a higher-level rule.

When authoritative sources conflict and the conflict changes implementation or proof, use the blocked protocol.

---

# 3. Governed Change Profile

Use the repository's governed location. If none exists, prefer:

```text
.governance/GOVERNED_CHANGE_PROFILE.md
```

Required fields where applicable:

```text
Repository root:
Primary branch:
Runtime/build system:
Test framework:
Narrow-test command:
Affected-integration command:
Acceptance/integration command:
Full-regression command:
Type/static/build commands:
Scope/diff check:
Security/secret scan:
Generated-artifact check:
Migration policy:
Persistence policy:
Live external-call policy:
Controlled-test credential policy:
Terminal machine-gate command:
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

Use `PRODUCTION_CLOSURE` when a set of known production-readiness defects collectively prevents one real end-to-end path from satisfying its contracts.

Do not split one production-path root cause into artificial future work merely to obtain PASS.

---

# 5. Gate 0 — Intake

Before code changes:

- [ ] State one measurable objective.
- [ ] Classify the change.
- [ ] Identify governing sources.
- [ ] Identify protected invariants.
- [ ] Identify upstream and downstream boundaries.
- [ ] Determine whether executable behavior changes.
- [ ] Determine migration or compatibility obligations.
- [ ] Determine whether live external services are permitted.
- [ ] Determine whether merge/deploy/release is authorized.
- [ ] For production closure, enumerate all currently known blockers on the same path.

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

## 6.1 Dirty-tree continuation

A dirty tree is not automatically a blocker when the user explicitly asks to continue the active correction and the modifications belong to that correction.

Then:

1. capture `git status`, `git diff --stat`, and complete `git diff`;
2. map each existing modification to checklist IDs;
3. preserve valid work;
4. correct invalid work in place;
5. do not reset or stash merely to manufacture a clean baseline.

Unexplained or unrelated dirty-tree conflicts remain blockers.

## 6.2 Interrupted-agent resume

If the coding agent, API connection, terminal session, or response is interrupted during a governed run:

1. resume the same repository and branch;
2. inspect current HEAD, working tree, task state, checklist state, and available test evidence;
3. determine the last section that has direct PASS evidence;
4. preserve completed valid work;
5. continue from the first unproven or failing section;
6. do not restart the whole change merely because the conversational response was interrupted.

A response interruption is not proof that repository work was lost.

---

# 7. Gate 2 — Freeze scope

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

For `PRODUCTION_CLOSURE`, a repository-owned missing boundary discovered during implementation may be added only when strictly required to satisfy an already-governed production-path requirement. Version the checklist before modifying newly authorized scope.

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

# 9. Sequential Evidence Gate

For any change with multiple ordered sections, checklist groups, architectural boundaries, or closure responsibilities, execute them sequentially.

For each section:

```text
INSPECT
→ DEFINE PROOF
→ REPRODUCE FAILURE when safe/feasible
→ IMPLEMENT COMPLETE SECTION
→ NARROW VERIFY
→ SECTION AUDIT
→ AUTO-CONTINUE ON PASS
```

## 9.1 Inspect before editing

Before changing a section:

1. trace the existing real production/runtime path;
2. identify the exact defect or prove existing compliance;
3. identify the smallest architectural boundary that owns it;
4. verify the proposed change does not violate earlier passed sections.

Do not make speculative changes.

## 9.2 Define proof first

Before implementation, define the exact assertion or machine check that will prove the section. Add or correct the narrow regression proof when technically feasible.

## 9.3 Section PASS rule

A section is PASS only when all are true from evidence:

```text
requirement satisfied == true
real governed path exercised == true where applicable
direct positive proof exists == true
required negative proof exists == true
earlier passed sections remain intact == true
unresolved defect inside section == false
```

If PASS, automatically continue to the next section without asking for routine approval.

If FAIL, correct the same section and rerun its proof. Do not proceed while it remains failed.

Stop only for a genuine governance, authorization, safety, or external blocker.

---

# 10. Balanced machine verification cadence

Do not run the most expensive verification suite after every small section unless a governing contract requires it.

Use three layers:

## Layer A — Section checks

After each section, run the narrowest executable tests that directly prove that section and its negative path.

## Layer B — Affected integration checks

Run affected integration/acceptance checks when a section crosses or changes an already-passed boundary. Re-run only the earlier sections that could materially be invalidated.

## Layer C — Terminal verification

After all sections pass:

1. run cross-section integration review;
2. run full acceptance/integration;
3. run full regression;
4. run type/static/build/security checks as applicable;
5. run persistence/migration/recovery checks as applicable;
6. run invariant and scope checks;
7. inspect the complete diff;
8. run the terminal machine release gate.

This balance reduces cycle time without weakening final acceptance.

---

# 11. Real production path acceptance

Acceptance must prove production behavior, not a hand-written imitation.

When external providers are involved, prefer:

```text
real production adapter/service
+
injected controlled transport/client
+
production validator
+
real normalization/artifact/persistence boundary
+
real orchestrator/web/service path
```

Controlled fixtures may emulate provider responses. The adapter/service/orchestrator under test must be production code.

Do not fabricate a successful normalized result and inject it downstream as proof that the production adapter works.

Measure exact call counts whenever idempotency, retry, paid tasks, polling, writes, or side effects matter.

---

# 12. Controlled external-call and credential isolation

Live paid/provider/LLM calls are zero in tests and CI unless explicitly authorized by the frozen checklist and governing sources.

Controlled verification must not accidentally inherit workstation or CI secrets.

Where technically possible:

1. inject controlled transports/clients below the production adapter boundary;
2. unset, shadow, or sandbox real provider credentials for controlled acceptance processes;
3. fail the test if a real network/provider path is attempted unexpectedly;
4. measure controlled and live call counts from the transport/client boundary rather than hardcoding zero;
5. record any accidental external call as an incident and rerun governed verification under isolated credentials.

A prompt prohibition alone is not sufficient protection when machine isolation is feasible.

---

# 13. Validation-before-transition

Whenever an artifact or contract controls persistence, lifecycle advancement, rendering, publication, or exposure:

```text
assemble complete object
→ validate complete object
→ freeze/retain validated object when applicable
→ persist/advance/use that validated object
```

Do not validate a partial object and add production fields afterward.

If a downstream consumer must receive the validated model, prove exact identity, equality, or canonical immutable hash as appropriate.

Malformed `AVAILABLE`, `PARTIAL`, `SUCCESS`, `READY`, or equivalent usable states must fail closed rather than being converted into defaults or silently downgraded.

Missing planned evidence must not be invented as a legitimate unavailable/not-connected state unless that state was actually produced by the governed collection path.

---

# 14. Negative-path and fail-closed proof

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

# 15. Production Closure Mode

Production Closure Mode exists when repeated partial audits would otherwise rediscover repository-owned missing boundaries.

## 15.1 One closure package

Convert all known defects on the same production path into one bounded checklist. Typical responsibilities include:

- complete request/config persistence;
- source-specific contract validation;
- real production adapters with controlled transports;
- artifact integrity and provenance;
- validation before persistence/state transition;
- finalization gates;
- complete validated render/view model;
- durable job execution;
- restart/recovery;
- retry classification;
- task/payment idempotency;
- abort/cancellation propagation;
- replay/cache execution;
- model-client budget/retry controls tested with fake clients;
- publication/terminal state;
- actual web/API path;
- negative proofs.

Only include responsibilities required by governing contracts for the path being closed.

## 15.2 Repository-owned work is not a final blocker

When already required by the governed production contract, these are implementation work rather than final blockers:

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

## 15.3 Genuine external blocker

A genuine external blocker exists only when the remaining dependency cannot be created or simulated from the repository without an unavailable or prohibited external action, for example:

- unavailable credentials/account authorization;
- destructive production mutation without authorization;
- deployment or merge authorization explicitly withheld;
- mandatory external CI or platform capability currently unavailable;
- a live proof explicitly forbidden when no controlled boundary can establish the required repository behavior.

Complete all repository-controlled work first and report the smallest remaining external action.

---

# 16. Durability, restart, retry, idempotency, and abort

When the path includes background work or paid/task-based providers, add checklist IDs for applicable responsibilities:

- durable execution identity and status;
- persisted checkpoints;
- recovery after process restart;
- zero repeat calls for completed steps unless explicitly governed;
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

# 17. Cross-section integration review

After all sequential sections PASS but before terminal release verification, inspect interactions between adjacent and dependent sections.

For each dependency edge, verify that the downstream section consumes the exact governed output of the upstream section and does not bypass its validation or mutate it after proof.

If a cross-section defect is found:

1. assign it to the owning checklist ID/section;
2. correct that section;
3. rerun its narrow proof;
4. rerun affected later sections;
5. repeat cross-section review;
6. then run terminal verification.

Do not open a new work package for an integration defect created by the current closure package.

---

# 18. Verification matrix

Run every applicable row. `N/A` requires evidence that the repository/change has no such responsibility.

| Responsibility | Required result |
|---|---|
| Preflight | exact repo/branch/SHA/tree verified |
| Sequential section checks | PASS |
| Affected integration | PASS where required |
| Acceptance/integration | PASS |
| Negative-path proof | PASS where applicable |
| Full regression | PASS when suite exists |
| Static/type/build | PASS when configured |
| Schema/contract validation | PASS when applicable |
| Migration/persistence | PASS when applicable |
| Restart/recovery | PASS when applicable |
| Idempotency/retry/abort | PASS when applicable |
| Credential isolation/live-call guard | PASS when external services exist |
| Security/secret scan | PASS when applicable |
| Protected invariants | PASS |
| Generated artifacts | PASS |
| Scope/permitted files | PASS |
| Prohibited files | untouched |
| Complete diff review | PASS |
| Terminal machine release gate | PASS when configured/required |
| Exact-head CI | PASS when required |

Any required failure means governed closure is incomplete.

---

# 19. Scope-check contract

Compare the complete changed-file set from starting SHA to final head against the frozen boundary.

Required proof:

```text
unexpected changed files == 0
prohibited changed files == 0
```

Do not rely only on `git status`; committed out-of-scope files must also be detected.

---

# 20. Terminal machine release gate

Stable release conditions must be mechanically enforced when technically reasonable.

Preferred repository command:

```text
change:release-gate
```

or a repository-native equivalent such as:

```text
npm run change:release-gate
```

The terminal machine gate should verify all mandatory release conditions that can be checked locally or through repository APIs, including as applicable:

```text
exact branch and final SHA
clean/protected working-tree state
frozen scope compliance
unexpected files == 0
prohibited files == 0
required section checks PASS
acceptance PASS
full regression PASS
schema/contract checks PASS
restart/recovery/idempotency checks PASS
live provider/LLM policy PASS
controlled-test call counters valid
protected invariants PASS
complete diff reviewed/recorded
required exact-head CI PASS
independent exact-head audit PASS or audit evidence attached by the governed mechanism
PR/release state truthful
```

Rules:

- exit `0` means every machine-enforceable required condition passed;
- non-zero means `BLOCKED` or `GOVERNANCE HOLD` according to cause;
- the coding agent may not override a failed gate with prose, confidence, local substitutes, or environmental explanations;
- if exact-head CI is mandatory but unavailable, local exact-head commands may prove code quality but do not satisfy the CI requirement;
- the correct state in that case is `CODE VERIFIED / GOVERNANCE HOLD`, not final governed PASS;
- rerun the gate against the unchanged exact SHA when the external dependency becomes available.

Use `templates/MACHINE_RELEASE_GATE_TEMPLATE.md` when adopting this control.

---

# 21. Independent exact-head audit

The implementation pass cannot self-authorize release.

The audit runs in a separate review context that did not author the changes and begins from repository evidence, not the implementation report.

The auditor verifies:

- exact final SHA;
- required exact-head CI;
- changed-file scope;
- prohibited files untouched;
- each checklist ID maps to implementation and direct proof;
- sequential sections were closed before later dependent sections proceeded;
- acceptance executes the real governed path with controlled dependencies;
- failure proofs include state and prohibited side effects;
- order/count/hash/identity claims are exact when governed;
- credential isolation/live-call evidence is measured rather than hardcoded;
- protected invariants remain intact;
- migrations/recovery obligations pass;
- no unmet requirement is hidden as a limitation;
- machine release-gate result is truthful;
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

# 22. Correction protocol

If audit or machine gate returns blocked:

1. reproduce failed IDs;
2. correct missing/false proof first when appropriate;
3. correct implementation only as required by governed evidence;
4. rerun the owning section's narrow proof;
5. rerun affected later sections;
6. rerun the complete terminal verification matrix;
7. rerun scope check and inspect the correction diff;
8. commit/push under repository governance;
9. audit the corrected exact head independently.

For ordinary changes, one consolidated correction round is the default target; a second round requires process review.

For `PRODUCTION_CLOSURE`, process review does not end the objective. Continue correcting repository-owned failed IDs until PASS or a genuine external blocker is proved.

---

# 23. Close and release states

Use precise states rather than forcing every outcome into PASS/BLOCKED.

## SECTION PASS

A sequential section has direct evidence and may advance.

## CODE VERIFIED

Local/controlled production acceptance and required local verification pass at the exact candidate head.

## STAGING CANDIDATE

Code verification passes and repository governance permits staging validation, but merge/release closure is not yet authorized or complete.

## GOVERNANCE HOLD

Repository code may be verified, but a mandatory external governance condition such as exact-head CI is unavailable or not yet satisfied.

## RELEASE READY

Every required checklist item, terminal machine gate, exact-head CI, independent audit, repository state, and authorization prerequisite passes.

If explicit merge approval is still required, report:

```text
READY FOR MERGE — NOT MERGED
```

Never infer merge/deploy/release authorization from successful tests.

---

# 24. Blocked protocol

Stop and return `BLOCKED` for a material condition the governed run cannot safely resolve, including:

- wrong repository/branch or starting SHA mismatch;
- unexplained dirty-tree conflict;
- authoritative source conflict;
- unresolved product/contract decision requiring user authority;
- required implementation would alter a prohibited invariant/file without scope authorization;
- destructive migration or production mutation lacks authorization;
- security boundary cannot be preserved;
- proof requires a prohibited live call and no controlled repository boundary can establish behavior;
- required external credential/account authorization is unavailable;
- exact-head audit cannot be established where mandatory.

Do not use `BLOCKED` merely because repository-owned infrastructure must be added.

When code verification is complete but only a temporary mandatory external release condition is unavailable, prefer `GOVERNANCE HOLD` over claiming a code defect.

Return:

```text
BLOCKED or GOVERNANCE HOLD
Reason:
Failed/affected checklist ID or release condition:
Exact evidence:
Repository-controlled work completed:
Smallest external decision/action required:
```

---

# 25. Automation requirements

Automate stable repeatable rules where technically reasonable:

- repo/branch/SHA preflight;
- dirty-tree/protected-work check;
- permitted/prohibited diff check;
- invariant/golden/reference hash checks;
- schema and migration checks;
- generated-artifact checks;
- secret/live-call scans;
- controlled credential isolation;
- section-level narrow verification;
- affected-integration verification;
- full regression;
- production-path acceptance;
- restart/recovery tests;
- exact-head CI lookup;
- PR state checks;
- terminal machine release gate;
- final evidence collection.

Preferred responsibility interface when repository conventions permit:

```text
change:preflight
change:test
change:affected
change:acceptance
change:scope-check
change:verify
change:release-gate
change:audit-support
```

Any failure exits non-zero.

---

# 26. Efficiency and WIP rules

Persist stable repository facts in the Governed Change Profile to avoid repeated discovery.

Execution prompts contain only current scope, governing sources, checklist IDs, executable proof, boundaries, required commands, authorization locks, and final output.

Exclude future work, motivational prose, optional cleanup, repeated architecture summaries, and confidence scores used as proof.

Default WIP:

```text
active governed change packages: 1
active correction package: 1
unplanned changed files: 0
```

Balanced verification is mandatory for multi-section closure: narrow checks per section, affected integration when needed, one complete terminal verification after all sections pass.

---

# 27. Process performance record

When comparable baseline data exists, record:

```text
Change ID:
Change class:
Baseline active cycle time:
Actual active cycle time:
Cycle-time reduction:
First-pass section pass rate:
Correction rounds:
False-positive proofs found:
Unplanned files changed:
Preventable broad-suite reruns:
Interrupted-session recovery events:
Accidental external-call incidents:
Repeated manual check to automate next:
```

Default adoption target: at least 55% lower active cycle time than a comparable fragmented process, without weakening acceptance quality.

Do not claim speed improvement without measurement.

---

# 28. Mandatory final report

Use evidence, not narrative completion claims:

```text
GOVERNED CHANGE REPORT

Skill version: 1.2.0
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

SECTIONS
[x] SECTION/CHANGE-ID — PASS — exact evidence
[ ] SECTION/CHANGE-ID — FAIL — exact evidence

VERIFICATION
[x] preflight — PASS — evidence
[x] sequential narrow checks — PASS — evidence
[x] affected integration — PASS/N/A — evidence
[x] production acceptance — PASS/N/A — evidence
[x] negative proofs — PASS/N/A — evidence
[x] persistence/recovery/idempotency — PASS/N/A — evidence
[x] full regression — PASS/N/A — evidence
[x] credential isolation/live-call guard — PASS/N/A — evidence
[x] invariant checks — PASS — evidence
[x] scope check — PASS — unexpected 0; prohibited 0
[x] terminal machine release gate — PASS/BLOCKED/N/A — command + exit code
[x] exact-head CI — PASS/BLOCKED/N/A — exact SHA

AUDIT
Independent exact-head audit: PASS/BLOCKED
Audit head SHA:
Correction rounds:

EXTERNAL EFFECTS
Controlled provider calls:
Live provider calls:
Controlled model calls:
Live LLM calls:
Paid task calls:
Production mutations:

REPOSITORY STATE
Working tree:
PR state:
Merge/deploy/release state:
Rollback/recovery state:

FINAL STATUS:
SECTION PASS / CODE VERIFIED / STAGING CANDIDATE / GOVERNANCE HOLD / RELEASE READY / BLOCKED
```

Rules:

- no prose-only completion claim;
- no confidence percentage in place of proof;
- no hidden failed requirement under `known limitations`;
- no final governed PASS/RELEASE READY while a required machine or external release condition is open;
- no local substitute for mandatory exact-head CI;
- no claim of merge/deploy/release unless it actually occurred.

---

# 29. Global invocation contract

A skill is not reliably installed unless the coding environment also contains a global/project rule equivalent to:

```text
For every qualifying coding change, invoke and obey `governed-coding-upgrade`
before editing. For multi-section production closure, execute sections
sequentially: inspect → define proof → implement → narrow verify → section audit
→ automatically continue on PASS. Use controlled dependencies below real
production boundaries, isolate real credentials in controlled tests, and run
full regression once after all sections and cross-section checks pass. Do not
claim RELEASE READY unless the configured terminal machine release gate exits 0,
required exact-head CI passes, and the independent exact-head audit passes.
Do not merge/deploy/release without authorization.
```

---

# 30. Self-check before final closure

Every required answer must be YES from evidence:

```text
Was the exact starting state verified?
Was pre-existing work protected?
Was scope/checklist frozen?
Were multi-section changes closed sequentially?
Does every checklist ID have direct proof?
Did acceptance execute the real production implementation with controlled dependencies?
Were real credentials isolated from controlled acceptance where feasible?
Were live-call counts measured rather than hardcoded?
Did malformed/negative paths fail closed where applicable?
Were repository-owned dependencies implemented rather than relabeled as blockers?
Were restart/recovery/idempotency/abort obligations proved where applicable?
Were cross-section interactions verified?
Were protected invariants preserved?
Were unexpected changed files exactly zero?
Was the complete diff inspected?
Did the terminal machine release gate pass when required?
Did required exact-head CI pass for this exact final SHA?
Was the exact final head independently audited?
Were audit failures corrected and re-audited?
Is merge/deploy/release state reported truthfully?
Are all required checklist items PASS?
```

If code checks pass but a mandatory external release condition is temporarily unavailable, report `CODE VERIFIED / GOVERNANCE HOLD`.

If any repository-controlled required answer is NO, final status is `BLOCKED`.