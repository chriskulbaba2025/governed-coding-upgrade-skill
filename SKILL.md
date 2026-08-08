---
name: governed-coding-upgrade
description: >-
  Mandatory governed execution protocol for any task that changes source code,
  tests, schemas, dependencies, configuration, infrastructure-as-code, build
  logic, migrations, or generated application behavior. Use for features, bug
  fixes, refactors, upgrades, migrations, performance work, security fixes,
  dependency changes, and corrective work. Requires frozen scope, checklist
  IDs, direct proof, verification gates, exact-head independent audit,
  controlled correction, and evidence-based closure before merge.
---

# Governed Coding Upgrade Skill

**Version:** 1.0.0  
**Status:** Governing execution skill  
**Scope:** Any repository change that modifies executable behavior, runtime contracts, build/release behavior, tests, schemas, dependencies, infrastructure-as-code, configuration, or generated application output.

## 0. Governing intent

This skill converts coding work from an informal edit/test cycle into a deterministic governed change protocol.

Every governed change MUST move through this sequence:

**INTAKE → PREFLIGHT → PROFILE → FROZEN CHECKLIST → EXECUTION PLAN → BUILD → VERIFY → EXACT-HEAD AUDIT → CORRECT → RE-AUDIT → CLOSE**

The skill has four non-negotiable properties:

1. **Scope is frozen before implementation.**
2. **Completion is proved by executable evidence, not prose.**
3. **The implementation cannot authorize its own release.**
4. **A change is not complete until the exact final head is independently audited.**

Speed is optimized by reducing rediscovery, fragmented fixes, repeated prompts, avoidable correction rounds, and manual checks. Speed NEVER overrides product, security, data, evidence, compatibility, rollback, or release invariants.

---

# 1. Mandatory invocation rule

Invoke this skill whenever the requested task would intentionally change one or more of the following:

- application source code;
- service or library code;
- tests or test harnesses;
- API behavior or schemas;
- database schemas or migrations;
- dependency versions or lockfiles;
- configuration affecting executable behavior;
- infrastructure-as-code;
- CI/CD behavior;
- build, packaging, deployment, or release logic;
- generated runtime artifacts;
- security controls;
- data transformation behavior;
- user-visible application behavior;
- defect corrections;
- refactors that can alter behavior or contracts.

Do NOT bypass this skill because the change appears small.

Read-only inspection, explanation, research, or documentation-only work that cannot affect executable behavior does not require the full execution lifecycle unless repository governance says otherwise.

---

# 2. Authority and precedence

Before editing, resolve authority in this order:

1. Applicable platform, safety, legal, privacy, and security constraints that the coding agent cannot waive.
2. Explicit user instruction for the current task, including scope and authorization boundaries.
3. Repository governance and security rules.
4. Product, API, schema, data, compatibility, and release contracts.
5. Protected invariants and golden/reference artifacts.
6. This skill.
7. The repository's governed change profile.
8. The frozen change checklist.
9. The compiled execution plan.
10. Implementation notes or model suggestions.

A lower-level instruction MUST NOT override a higher-level rule. A user instruction may narrow scope or withhold authorization at any time; it does not silently waive a stricter safety, security, data, or repository requirement. A deliberate governance-rule change must itself be explicitly scoped and governed.

If authoritative sources conflict and the conflict changes implementation or proof requirements, STOP under the blocked protocol.

---

# 3. Core operating rules

Every governed coding change MUST satisfy all of these rules:

- [ ] One measurable change package is active per governed branch/PR unless repository governance explicitly permits otherwise.
- [ ] Exact repository root is verified before editing.
- [ ] Exact starting branch and SHA are recorded.
- [ ] Working-tree state is recorded and unexplained pre-existing changes are protected.
- [ ] Governing documents are identified before implementation.
- [ ] Protected invariants are identified before implementation.
- [ ] One frozen checklist exists before code changes.
- [ ] Every checklist item has a stable ID.
- [ ] Every checklist item describes one observable behavior or one verifiable repository condition.
- [ ] Every checklist item names direct proof.
- [ ] Permitted and prohibited file boundaries are explicit.
- [ ] Scope changes after freeze require reclassification before implementation continues.
- [ ] One consolidated implementation pass is preferred over symptom-by-symptom edits.
- [ ] Verification is run against the actual implementation.
- [ ] Full regression is run when the repository provides a regression suite.
- [ ] Scope is checked against the frozen file boundary.
- [ ] Complete diff is inspected before the implementation commit is considered ready.
- [ ] An independent audit inspects the exact final head.
- [ ] Failed audit IDs are corrected as one consolidated correction package.
- [ ] The corrected exact head is audited again.
- [ ] Merge/release occurs only after all required evidence is PASS and authorization rules are satisfied.
- [ ] The next governed change does not begin until this change is closed or explicitly suspended.

---

# 4. Project adapter layer

The skill is universal because repository-specific facts are loaded into a **Governed Change Profile** rather than hard-coded into the skill.

## 4.1 Profile location

Use the first existing repository-governed location that fits local conventions. If none exists, create:

```text
.governance/GOVERNED_CHANGE_PROFILE.md
```

Creating the profile is governance/setup work. Do not silently add it during a narrowly scoped product change when the permitted-file list does not allow it. In that case, build an in-memory profile for the current change and report that no persistent profile was written.

## 4.2 Required profile fields

The profile MUST record, where applicable:

```text
Repository root:
Primary branch:
Package/build system:
Runtime(s):
Test framework(s):
Static-analysis commands:
Type-check commands:
Build commands:
Narrow-test convention:
Acceptance/integration-test convention:
Full-regression command:
Scope/diff-check convention:
Security/secret-scan convention:
Generated-artifact policy:
Dependency/lockfile policy:
Migration policy:
Live external-call policy:
CI provider and exact-head verification method:
Merge/release authorization rule:
Rollback mechanism:
Protected invariant registry:
Canonical governance sources:
Known repository-specific stop conditions:
```

Unknown fields MUST be marked `UNRESOLVED`, not guessed.

## 4.3 Protected invariant registry

Translate project-specific invariants into generic protected invariant classes.

Examples include:

| Invariant class | Examples |
|---|---|
| Interface | API shape, CLI contract, public function signature |
| Data | schema, migration ordering, serialization, tenant isolation |
| State | lifecycle transitions, idempotency, concurrency behavior |
| Security | auth, authorization, secret handling, sandbox boundaries |
| Evidence | audit artifacts, stored hashes, provenance, logs |
| Output | report templates, golden masters, snapshots, generated assets |
| Compatibility | supported runtime, protocol, dependency, browser, platform |
| Cost/external | paid API calls, provider quotas, LLM calls |
| Release | feature flags, deployment state, rollback target |
| Performance | governed latency, memory, throughput, bundle limits |

A change MAY have zero invariants in a class. It MUST NOT assume an invariant exists without repository evidence.

---

# 5. Change classification

At Gate 0 classify the change so proof is proportionate but governance remains intact.

Choose exactly one primary class:

- **DEFECT** — existing governed behavior is incorrect.
- **FEATURE** — new product/runtime behavior is added.
- **REFACTOR** — internal structure changes while governed external behavior is intended to remain stable.
- **MIGRATION** — data, schema, runtime, platform, framework, or architecture is moved between governed states.
- **DEPENDENCY** — dependency or toolchain version changes.
- **SECURITY** — threat, vulnerability, permission, authentication, authorization, isolation, or secret-handling behavior changes.
- **PERFORMANCE** — governed resource or latency behavior changes.
- **CONFIGURATION** — executable behavior changes through config, CI, build, or infrastructure code.
- **CORRECTION** — a failed governed checklist/audit item is being repaired.

The class changes which proofs are required; it does NOT remove frozen scope, direct evidence, audit, or closure gates.

---

# 6. Gate 0 — Intake and disposition

No code changes.

Complete:

- [ ] State one measurable objective.
- [ ] Classify the change.
- [ ] Identify the requested outcome.
- [ ] Identify governing sources.
- [ ] Identify upstream dependencies.
- [ ] Identify downstream systems/work that must remain untouched.
- [ ] Determine whether executable behavior is expected to change.
- [ ] Determine whether protected outputs or contracts are expected to change.
- [ ] Determine whether a migration or compatibility obligation exists.
- [ ] Determine whether live external services are permitted.
- [ ] Determine whether merge/release is authorized or explicitly prohibited.
- [ ] Identify the baseline for any claimed speed/performance improvement.
- [ ] Stop if a required governing contract is unresolved.

**Required output:** a short disposition containing objective, class, governing sources, expected invariant impact, and any blocking condition.

---

# 7. Gate 1 — Repository preflight

Before editing, verify actual repository state.

Required evidence:

```text
Repository root:
Current branch:
HEAD SHA:
Working tree status:
Remote identity when relevant:
Active PR when relevant:
Governance sources found:
Governed Change Profile found/derived:
```

Rules:

- A starting SHA mismatch is a STOP condition.
- Unexplained dirty-tree changes are a STOP condition unless they can be protected without touching them.
- Never reset, discard, overwrite, stage, or commit pre-existing user work unless explicitly authorized.
- Never infer repository identity from conversation history when the repository can be inspected.

---

# 8. Gate 2 — Scope and architecture resolution

Resolve the implementation boundary before checklist freeze.

## 8.1 One architectural boundary

Group confirmed defects/requirements that share the same relevant boundary:

- responsibility;
- contract;
- state transition;
- schema;
- storage path;
- adapter/provider boundary;
- API surface;
- security boundary;
- build/release boundary;
- acceptance harness;
- failure mode.

Do not send piecemeal symptom fixes when one bounded change can address the same root cause.

## 8.2 File boundary

Define:

```text
Permitted files:
- exact files or bounded path patterns

Prohibited files:
- protected files or path patterns
```

A permitted pattern MUST be narrow enough that unrelated edits can be detected.

## 8.3 Architecture decision rule

Before build begins, unresolved architectural decisions affecting the change MUST equal zero.

If implementation reveals a material architecture decision not represented in the frozen checklist, STOP and reclassify scope.

---

# 9. Gate 3 — Frozen checklist

Create the checklist BEFORE implementation.

Suggested repository path when no stronger convention exists:

```text
.governance/changes/<CHANGE-ID>_CHECKLIST.md
```

## 9.1 Checklist header

```text
Change ID:
Version:
Change class:
Branch:
PR:
Required starting SHA:
Objective:
Governing sources:
Protected invariants:
Permitted files:
Prohibited files:
Baseline metric when applicable:
```

## 9.2 Checklist item contract

Every item MUST contain:

| Field | Requirement |
|---|---|
| ID | Stable identifier |
| Requirement | One observable behavior or repository condition |
| Boundary | Exact file/function/module/schema/config surface |
| Positive proof | Exact assertion, command, artifact, state, output, or diff evidence |
| Negative proof | Required when failure/absence matters |
| Acceptance proof | End-to-end/real-path proof where applicable |
| Protected invariant | Invariant preserved or intentionally versioned |
| Failure result | Exact fail-closed result when applicable |
| Final evidence | Evidence required in the close report |
| Status | `[ ]` or `[x]` only |

## 9.3 Checklist quality rules

- One behavior per item.
- No aspirational wording.
- No item without direct proof.
- No proof based only on comments, test names, source-string searches, or green CI.
- No `A OR B` acceptance when only one governed result is correct.
- No combined checkbox for independent behaviors.
- No optional improvements inside current scope.
- No hidden requirements in prose outside checklist IDs.

## 9.4 Observable language

Prohibited:

```text
improve reliability
make robust
clean up
optimize
handle edge cases
strengthen validation
ensure quality
make deterministic
```

Required form:

```text
Given <precondition>, when <operation>, then <exact observable result>,
and <prohibited result> does not occur.
```

## 9.5 Frozen scope rule

When implementation begins, the checklist is frozen.

A later scope addition requires:

1. STOP;
2. classify it as blocker, in-scope defect, or future change;
3. version the checklist if current scope truly changes;
4. update permitted/prohibited boundaries;
5. update the baseline when the scope change materially affects measurement;
6. restart implementation only from the newly governed scope.

---

# 10. Gate 4 — Compile the execution plan

The implementation instructions MUST be compiled from the frozen checklist, not reconstructed from memory.

Required execution-plan fields:

```text
Repository root
Branch
PR when applicable
Required starting SHA
One objective
Change class
Governing sources
Protected invariants
Permitted files
Prohibited files
Checklist IDs
Required narrow tests
Required acceptance/integration proofs
Required negative-path proofs
Required full regression
Required build/static/type/security checks
Required scope check
Required diff review
Commit policy
Push policy
Exact-head CI requirement
Independent-audit requirement
Merge/release authorization rule
Required final report format
```

Do not include future work, opportunistic refactors, or model-preferred cleanup.

---

# 11. Gate 5 — Build

Follow this order unless a repository-governed migration or security procedure requires a stricter sequence:

1. Re-run preflight and confirm the required starting state.
2. Add or correct proof for each checklist behavior when proof does not already exist.
3. For defect work, reproduce the defect with a failing test/acceptance proof when technically feasible and safe.
4. Record the expected pre-fix failure.
5. Implement only the frozen checklist.
6. Run the narrow verification set until green.
7. Build/update acceptance or integration proof where applicable.
8. Run the governed acceptance path.
9. Run required static analysis/type checks.
10. Run required security and secret checks.
11. Run build/package validation.
12. Run full regression when available.
13. Run migration/compatibility checks when applicable.
14. Run protected-invariant checks.
15. Run scope check.
16. Inspect the complete diff.
17. Confirm no generated/untracked artifact violates policy.
18. Commit/push according to repository governance.

Do NOT produce a completion report while any required checklist item is open or failing.

---

# 12. Proof standard

A checklist item is complete only when direct evidence proves it.

Valid evidence includes:

- exact assertion output;
- exact expected/actual value;
- exact ordered state history;
- persisted database state;
- stored artifact content;
- byte count;
- SHA-256 or repository-governed hash;
- adapter/provider call count;
- artifact write count;
- HTTP status/body/schema result;
- CLI exit code and output;
- database row count/value;
- migration version/state;
- snapshot/golden/reference hash;
- build artifact manifest;
- dependency resolution/lockfile evidence;
- benchmark measurement when performance is governed;
- security scanner result when security is governed;
- exact changed-file list;
- exact-head CI result tied to the final SHA.

Invalid evidence by itself includes:

- comments;
- test names;
- prose claims;
- confidence scores;
- source-code string search;
- green CI without behavior-specific proof;
- manually constructed success summaries;
- unused variables presented as proof;
- broad "works" statements.

---

# 13. Negative-path and fail-closed rules

When a checklist item governs failure behavior, proof MUST show all applicable dimensions:

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

Do not accept a negative-path test that proves only an exception was thrown.

---

# 14. Determinism rules

Where order, exclusivity, identity, or count matters, use exact assertions.

Examples:

```text
actual == expected
actual sequence == exact expected sequence
call count == exact expected count
written artifacts == exact expected set
changed files == permitted changed-file set
```

Do not use containment, partial matching, truthiness, or `A OR B` when the governed contract defines one exact result.

Use deterministic clocks, IDs, random seeds, fixtures, and providers where the repository permits them.

Live paid/external/LLM/provider calls MUST be zero in tests and CI unless the frozen checklist and governing sources explicitly authorize them.

---

# 15. Verification matrix

Run every applicable row. Mark a row `N/A` only with evidence that the repository/change has no such responsibility.

| Verification responsibility | Required result |
|---|---|
| Preflight | exact repo/branch/SHA/tree verified |
| Narrow unit tests | PASS |
| Acceptance/integration | PASS where applicable |
| Negative-path proof | PASS where applicable |
| Full regression | PASS when suite exists |
| Static analysis/lint | PASS when configured |
| Type check | PASS when configured |
| Build/package | PASS when configured |
| Schema validation | PASS when applicable |
| Migration validation | PASS when applicable |
| Compatibility | PASS when applicable |
| Security scan | PASS when configured/relevant |
| Secret scan | PASS when configured/relevant |
| Dependency integrity | PASS when applicable |
| Protected invariant checks | PASS |
| Generated-artifact policy | PASS |
| Live external-call policy | PASS |
| Scope/permitted files | PASS |
| Prohibited files | untouched |
| Complete diff review | PASS |
| Exact-head CI | PASS when CI exists |

Any required verification failure means the change is NOT complete.

---

# 16. Scope-check contract

At minimum, compare the full changed-file set from the starting SHA to final head against the frozen file boundary.

Proof MUST establish:

```text
unexpected changed files == 0
prohibited changed files == 0
```

Do not rely only on `git status`; committed out-of-scope files must also be detected.

If the repository has a reusable scope-check command, use it. Otherwise inspect the diff from the exact starting SHA.

---

# 17. Independent exact-head audit

The implementation pass MUST NOT self-authorize release.

An independent audit MUST inspect the actual final commit/head, not merely the implementation report.

**Independence requirement:** the audit must run in a separate review context that did not author the implementation changes. Acceptable forms include a separate coding-agent context, a dedicated audit agent, an independent reviewer, or a repository/CI audit job that evaluates the frozen checklist against the exact head. The auditor MUST begin from repository evidence and governing sources rather than trusting the implementation report. If no independent review context is available, this gate is unsatisfied and the change MUST NOT be reported as independently audited.

The auditor verifies:

- [ ] repository/PR head equals reported final SHA;
- [ ] CI, when required, ran against that exact SHA;
- [ ] changed files match the frozen scope;
- [ ] prohibited files are untouched;
- [ ] every checklist ID maps to real implementation and real proof;
- [ ] tests assert governed behavior rather than implementation trivia;
- [ ] acceptance executes the real governed path using controlled dependencies;
- [ ] failure behavior proves exact rejection and resulting state/effects;
- [ ] order/count/hash/identity claims are exact when governed;
- [ ] protected invariants are preserved or intentionally versioned by scope;
- [ ] migrations are forward-safe and rollback/recovery obligations are satisfied when applicable;
- [ ] dependency/config changes are actually reflected in resolved state when applicable;
- [ ] no live provider/paid/LLM call violates policy;
- [ ] no out-of-scope generated artifacts are committed;
- [ ] no unmet governing requirement is relabeled as a limitation;
- [ ] the final report is supported by repository evidence;
- [ ] merge/release authorization requirements are satisfied or remain explicitly pending.

Audit result is exactly one of:

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

No `PASS WITH NOTES`, `MOSTLY PASS`, or equivalent status is allowed.

---

# 18. Consolidated correction gate

If audit returns BLOCKED:

- [ ] Correct only failed checklist IDs and dependencies strictly required by those IDs.
- [ ] Start from the exact failed-head SHA.
- [ ] Preserve original frozen scope unless a proven contract defect forces a versioned checklist update.
- [ ] Fix missing/false proof before changing working implementation when the original claim was simply unproven.
- [ ] Do not revisit accepted architecture without direct dependency.
- [ ] Do not add optional improvements.
- [ ] Re-run the complete applicable verification matrix.
- [ ] Re-run scope check.
- [ ] Inspect complete correction diff.
- [ ] Commit/push according to repository governance.
- [ ] Run a new independent audit against the corrected exact head.

Default maximum consolidated correction rounds: **1**.

A required second correction round triggers a process review before more coding. The review MUST identify why the frozen checklist, proof design, or first correction failed to bound the work.

---

# 19. Close and release gate

A governed change may be declared complete only when:

- [ ] every checklist ID is `[x] PASS`;
- [ ] every applicable verification responsibility is PASS;
- [ ] changed-file scope is exact;
- [ ] prohibited files are untouched;
- [ ] protected invariants are preserved or explicitly versioned;
- [ ] exact-head CI passes when required;
- [ ] independent exact-head audit returns PASS;
- [ ] repository/PR state matches the reported SHA;
- [ ] rollback/recovery obligation is satisfied when applicable;
- [ ] working tree is clean except for explicitly protected pre-existing work;
- [ ] final evidence report is complete;
- [ ] merge/release authorization is satisfied.

If the user or governance rules require explicit merge approval, STOP after audit PASS and report **READY FOR MERGE — NOT MERGED**.

Never infer merge authorization from successful tests.

---

# 20. Blocked protocol

Stop implementation immediately when any applicable condition occurs:

- starting SHA mismatch;
- wrong repository or branch;
- unexplained dirty-tree conflict;
- authoritative source conflict;
- required contract/invariant cannot be determined;
- proof cannot be constructed from available repository/runtime evidence;
- implementation requires a prohibited file;
- scope expands materially after freeze;
- protected invariant changes unexpectedly;
- migration requires an unapproved destructive step;
- security boundary cannot be preserved;
- test requires a prohibited live provider/paid/LLM call;
- exact-head CI cannot be tied to the reported commit when required;
- merge/release authorization is absent when required;
- a second correction round would be required;
- user input is required for a materially ambiguous product/contract decision.

Return:

```text
BLOCKED
Reason:
Failed/affected checklist ID:
Exact evidence:
Smallest required decision:
```

Do not guess around a governance conflict.

---

# 21. Defect regression rule

Every confirmed production defect and every independently discovered false-positive proof MUST add a permanent regression test or equivalent permanent executable check when technically feasible.

The regression proof MUST fail against the defective behavior and pass against the corrected behavior, unless reproducing the prior state is unsafe or impossible. If reproduction is impossible, record the exact reason and use the strongest executable surrogate proof available.

---

# 22. Migration-specific extension

For MIGRATION changes, add checklist IDs for every applicable obligation:

- source state identified;
- target state identified;
- compatibility window defined;
- forward migration proved;
- data preservation proved;
- idempotent/retry behavior proved where required;
- partial failure behavior proved;
- rollback or forward-recovery strategy proved;
- old-path removal is separately governed;
- deployment ordering is explicit when multiple components are involved.

Never combine migration execution and irreversible cleanup into one checklist item.

---

# 23. Dependency-upgrade extension

For DEPENDENCY changes, add checklist IDs for:

- requested dependency/version scope;
- manifest change;
- lock/resolved dependency change;
- runtime/build compatibility;
- affected public/deprecated API behavior;
- security/advisory obligation when relevant;
- full regression;
- generated artifact/bundle change when relevant.

Do not treat a manifest edit alone as proof that the dependency upgrade is effective.

---

# 24. Security-change extension

For SECURITY changes, the checklist MUST name the threat/control being changed and prove both:

```text
unauthorized/unsafe path is rejected
AND
authorized/safe path still functions as governed
```

Never weaken security validation to make tests pass.

Security-sensitive secrets, credentials, tokens, or production access MUST NOT be written into reports, fixtures, logs, or committed files.

---

# 25. Performance-change extension

For PERFORMANCE changes, define before implementation:

```text
metric
measurement method
environment/control conditions
baseline
required target
tolerance
regression guard
```

A performance claim without recorded before/after measurement is not proof.

Correctness and protected invariants MUST pass before performance improvement is accepted.

---

# 26. Refactor-specific extension

For REFACTOR changes, the primary governed objective is behavioral preservation.

Proof MUST identify the stable external contract and show that the refactor does not unintentionally change it.

If a behavior change is required, reclassify that checklist item as FEATURE/DEFECT behavior instead of hiding it inside a refactor.

---

# 27. Automation requirements

Repeated repository rules SHOULD become executable checks rather than repeated prompt text.

Automate where technically reasonable:

- repository/branch/SHA preflight;
- clean-tree/protected-work check;
- permitted-file diff check;
- prohibited-file diff check;
- invariant/reference hash checks;
- schema checks;
- migration checks;
- generated-artifact checks;
- secret scans;
- prohibited live-call scans;
- dependency integrity checks;
- full regression sequence;
- work-package acceptance;
- exact-head CI lookup;
- PR open/draft/unmerged state checks;
- final evidence collection.

Manual prose MUST NOT remain the sole enforcement mechanism for a repeatable repository rule once the rule is stable enough to automate.

---

# 28. Reusable command interface

When repository conventions permit, expose a stable command responsibility set. Names may vary, responsibilities may not.

Recommended interface:

```text
change:preflight
change:test
change:acceptance
change:scope-check
change:verify
change:audit-support
```

`change:verify` SHOULD aggregate every applicable verification responsibility for the current repository.

Any failure exits non-zero.

Do not hard-code a universal package manager. Use the repository's actual command system.

---

# 29. Efficiency and context rules

## 29.1 Source-first

Read governing repository sources and the Governed Change Profile before broad rediscovery.

## 29.2 No repeated discovery

Persist stable repository facts in the profile so future changes do not repeatedly rediscover:

- canonical test commands;
- protected invariants;
- standard release rules;
- migration rules;
- provider-call restrictions;
- golden/reference artifacts;
- scope-check commands;
- CI exact-head lookup method;
- rollback convention.

## 29.3 Prompt boundedness

Execution instructions include only:

- current change;
- confirmed blockers;
- required files;
- checklist IDs;
- executable proof;
- required final output.

Exclude:

- future work;
- motivational language;
- broad architecture summaries already stored in sources;
- optional cleanup;
- repeated explanations;
- confidence scores used as substitutes for evidence.

## 29.4 Work-in-progress limit

Default:

```text
active governed change packages: 1
active correction package: 1
unresolved architecture decisions affecting build: 0
unplanned changed files: 0
```

---

# 30. Performance record

After closure, record process performance when comparable baseline data exists.

Required fields:

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

Default acceleration target for teams adopting this skill: **≥55% lower active cycle time compared with the prior comparable unguided or fragmented change process**, measured without weakening acceptance quality.

Do not claim a speed improvement without recorded baseline and actual measurement.

A missed speed target is a process defect to analyze, not permission to skip governance.

---

# 31. Mandatory final report

Return evidence, not narrative completion claims.

Use this format:

```text
CHANGE REPORT

Change ID:
Change class:
Objective:
Repository:
Starting branch:
Starting SHA:
Final SHA:
PR:

Governing sources:
Protected invariants:

Exact files changed:
- path

CHECKLIST
[x] CHANGE-ID-01 — PASS — exact evidence
[ ] CHANGE-ID-02 — FAIL — exact evidence

VERIFICATION
[x] preflight — PASS — evidence
[x] narrow tests — PASS — command/result
[x] acceptance — PASS/N/A — evidence
[x] full regression — PASS/N/A — command/result
[x] static/type/build/security — PASS/N/A — evidence
[x] invariant checks — PASS — evidence
[x] scope check — PASS — unexpected files 0; prohibited files 0
[x] exact-head CI — PASS/N/A — exact SHA evidence

AUDIT
Independent exact-head audit: PASS/BLOCKED
Audit head SHA:
Correction rounds:

REPOSITORY STATE
Working tree:
PR state:
Merge/release state:
Rollback/recovery state:

PERFORMANCE
Baseline active cycle time:
Actual active cycle time:
Measured reduction:
First-pass pass rate:

FINAL STATUS:
PASS — READY FOR AUTHORIZED MERGE/RELEASE
or
PASS — MERGED/RELEASED (only when explicitly authorized and actually completed)
or
BLOCKED — exact failed IDs and evidence
```

Rules:

- No prose-only completion claim.
- No confidence percentage in place of proof.
- No hidden failed requirement under `known limitations`.
- No PASS while any required checklist item is open or failing.
- No claim of merge/release unless it actually occurred.

---

# 32. Checklist template

```markdown
# <CHANGE-ID> Governed Change Checklist

**Version:** 1.0.0
**Change class:**
**Repository:**
**Branch:**
**PR:**
**Required starting SHA:**
**Objective:**
**Governing sources:**
**Protected invariants:**
**Baseline active cycle time:**

## Permitted files

- `path`

## Prohibited files

- `path/**`

## Requirements

### <CHANGE-ID>-AREA-01 — <observable behavior>

- [ ] Requirement:
- [ ] Boundary:
- [ ] Positive proof:
- [ ] Negative proof:
- [ ] Acceptance proof:
- [ ] Protected invariant:
- [ ] Failure result:
- [ ] Final-report evidence:

## Verification

- [ ] Preflight PASS
- [ ] Narrow tests PASS
- [ ] Acceptance/integration PASS or governed N/A
- [ ] Full regression PASS or governed N/A
- [ ] Static/type/build/security checks PASS or governed N/A
- [ ] Protected invariant checks PASS
- [ ] Scope check PASS
- [ ] Complete diff reviewed
- [ ] Exact-head CI PASS or governed N/A
- [ ] Independent audit PASS

## Closure

- [ ] All checklist IDs PASS
- [ ] Final SHA recorded
- [ ] Repository state recorded
- [ ] Rollback/recovery requirement satisfied
- [ ] Merge/release authorization satisfied or explicitly pending
```

---

# 33. Execution-plan template

```text
Read and obey the governed-coding-upgrade skill before editing.

Read the frozen checklist:
<CHECKLIST PATH>

Repository:
<ROOT>

Branch:
<BRANCH>

PR:
<PR OR N/A>

Required starting SHA:
<SHA>

Objective:
<ONE MEASURABLE OBJECTIVE>

Change class:
<CLASS>

Governing sources:
<SOURCES>

Protected invariants:
<INVARIANTS>

Complete every checklist ID in the frozen checklist.
Do not add scope, optional refactors, or future work.
Do not modify files outside the permitted boundary.
Do not merge/release unless explicitly authorized.

Required order:
1. Verify preflight.
2. Establish/confirm direct proof for every checklist ID.
3. Record expected pre-fix failure when required.
4. Implement the complete frozen checklist.
5. Run narrow verification.
6. Run acceptance/integration where applicable.
7. Run static/type/security/build checks where applicable.
8. Run full regression where available.
9. Run protected-invariant checks.
10. Run scope check.
11. Inspect complete diff.
12. Commit/push under repository governance.
13. Confirm exact-head CI when applicable.
14. Run independent exact-head audit.
15. Correct only failed IDs if audit blocks.
16. Re-verify and re-audit the corrected exact head.
17. Return the evidence report only.

A checklist item is complete only when direct proof exists.
Do not claim completion while any required item is FAIL, open, or in progress.
```

---

# 34. Independent-audit template

```text
Audit the governed change at exact head <SHA>.
Do not modify, merge, deploy, or release.

Read:
- governed-coding-upgrade skill
- repository governance sources
- Governed Change Profile
- frozen checklist

For every checklist ID:
1. inspect actual implementation;
2. inspect exact proof;
3. inspect acceptance/runtime behavior where applicable;
4. inspect failure-state/effect proof where applicable;
5. inspect protected-invariant evidence;
6. mark PASS or BLOCKED.

Also verify:
- exact-head identity;
- exact-head CI when applicable;
- permitted-file scope;
- prohibited files untouched;
- complete diff;
- migration/dependency/security obligations where applicable;
- no false completion proof;
- repository/PR state;
- merge/release authorization state.

Return only:
PASS

or:
BLOCKED
Failed checklist IDs:
Evidence:
Smallest required correction:
```

---

# 35. Consolidated-correction template

```text
Correct only these failed checklist IDs:
<FAILED IDS>

Required starting SHA:
<FAILED HEAD SHA>

Preserve the frozen scope unless a proven contract defect requires a versioned checklist update.
Do not revisit accepted IDs unless directly required by a failed ID.
Do not add optional improvements.
Do not merge/release unless explicitly authorized.

For each failed ID:
- correct missing/false proof first when appropriate;
- change implementation only as required by governed evidence;
- run the complete applicable verification matrix;
- run scope check;
- inspect complete diff;
- commit/push under repository governance;
- audit the corrected exact head independently;
- return checklist evidence only.
```

---

# 36. Global invocation contract

A skill can be available without being invoked consistently. To make this protocol mandatory across coding work, the coding agent's global/project instructions MUST include an invocation rule equivalent to:

```text
For every task that changes code, tests, schemas, dependencies, executable
configuration, infrastructure-as-code, build/release logic, migrations, or
runtime behavior, invoke and obey the `governed-coding-upgrade` skill before
editing. Do not bypass it because a change appears small. Complete its frozen
checklist, verification, independent exact-head audit, and closure gates before
claiming the change is complete.
```

This invocation contract is part of the skill's governance architecture, not an optional recommendation.

---

# 37. Adoption rule

The skill is considered installed for a coding environment only when BOTH are true:

1. the skill is available to the coding agent; and
2. the global/project instruction layer contains the mandatory invocation contract.

For each repository, establish or derive the Governed Change Profile before the first governed implementation.

From that point forward, every qualifying coding change follows the same governed lifecycle while repository-specific commands and invariants come from the profile.

---

# 38. Self-check before declaring a governed change complete

Before returning PASS, answer every statement with YES from evidence:

```text
Was the exact starting state verified?
Was scope frozen before implementation?
Did every requirement receive a stable checklist ID?
Does every checklist ID have direct proof?
Were repository-specific protected invariants identified?
Were all applicable verification responsibilities executed?
Were unexpected changed files exactly zero?
Were prohibited changed files exactly zero?
Was the complete diff inspected?
Was the final exact head independently audited?
Were audit failures corrected only through governed IDs?
Was the corrected exact head re-audited when needed?
Is merge/release state reported truthfully?
Are all required checklist items PASS?
```

If any required answer is NO, final status is BLOCKED.
