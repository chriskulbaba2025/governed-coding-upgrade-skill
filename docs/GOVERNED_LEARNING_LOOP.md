# Governed Learning Loop

**Contract:** `gcu-learning-memory/1.0.0`  
**Applies to:** Governed Coding Upgrade v2.2+  
**Durable record owner:** Agentic OS when present  
**Model/usage authority:** Controlled AI Portal when present

## Purpose

GCU should improve from completed work without treating every AI output as truth or silently rewriting engineering standards.

```text
preflight
→ recall active approved practices
→ execute governed change
→ verify/audit/postflight
→ create evidence-linked lesson candidates
→ validate
→ explicit promotion outside the producing run
→ future preflight recall
```

## Persistent classes

### 1. Run history

The governed change workspace, exact-head evidence, task/run correlation, approvals, audit records, and usage receipts preserve what happened.

Run history is automatic evidence. It is not itself a best practice.

### 2. LessonCandidate

After a truthful terminal state, GCU may emit zero or more reusable learning candidates derived from evidence.

Allowed categories include:

- fix pattern;
- known failure;
- verification technique;
- architecture constraint;
- security lesson;
- performance lesson;
- tooling constraint;
- process improvement.

Every candidate must cite the source `changeId` and durable evidence references. A failed/blocked run may produce a known-failure lesson, but it must not produce a positive best-practice claim solely because an implementation was attempted.

A candidate is **non-authoritative**.

### 3. ApprovedPractice

An approved practice is a validated lesson explicitly promoted for reuse by the applicable governance/approval authority.

GCU MUST NOT auto-promote its own lesson candidates.

When Agentic OS is present, it owns the durable `LessonCandidateRecord` and `ApprovedPracticeRecord` lifecycle. GCU carries only the references needed for the governed change report/evidence.

## Authority order

Recalled memory is advisory and never overrides current authority:

```text
current user instruction
→ current repository contracts / frozen change scope / approved plan
→ current governed evidence
→ active ApprovedPractice
→ LessonCandidate / historical memory
```

If recalled memory conflicts with current authority, ignore the memory for execution and flag it for retirement/supersession review.

## Preflight recall

When a governed learning store is available, GCU preflight SHOULD recall only active approved practices relevant to the current repository/component/task.

Preflight MUST NOT silently inject:

- raw historical transcripts;
- unvalidated candidates;
- rejected lessons;
- superseded/retired practices;
- provider/model credentials;
- unrelated cross-project memory.

Recalled practices must preserve their source lesson/change/evidence lineage and be labeled `ADVISORY_ONLY`.

## Postflight extraction

After the change reaches an honest terminal state (`PASS`, `CODE VERIFIED / GOVERNANCE HOLD`, `BLOCKED`, or another explicit governed outcome), inspect the final evidence for reusable learning.

Create a lesson candidate only when all are true:

1. the lesson is materially reusable;
2. its claim is supported by durable evidence;
3. its applicability/scope can be stated;
4. it does not contradict current authority;
5. it contains no secret/provider credential material.

Zero candidates is a valid result.

## Promotion gate

Validation and promotion are separate decisions.

A lesson may be validated because evidence supports it but still remain unpromoted because it is too narrow, risky, obsolete, or not worth injecting into future work.

Promotion requires an explicit approval reference and named promoting authority. Existing higher-risk approval rules still apply to practices involving security, credentials, model routing, deployment, schema/data-model changes, architecture, or authority contracts.

## Staleness

Approved practices must support `active`, `superseded`, and `retired` states. Default recall includes only `active` practices.

Supersession/retirement preserves historical lineage; it does not erase the source change or evidence.

## Cross-system boundary

### GCU owns

- deciding whether a completed governed change contains evidence-backed learning worth proposing;
- requiring learning references in governed evidence/reporting when the learning loop is active;
- consuming bounded active approved practices during discovery/preflight.

### Agentic OS owns

- durable lesson/practice records;
- validation/promotion lifecycle state;
- repository/component/tag lookup and recall;
- supersession/retirement lineage.

### Controlled AI Portal owns

- provider/model route;
- provider credentials;
- provider usage/cost/audit.

Portal records may be cited as source evidence. Portal is not the engineering-memory authority.

## Claude Code boundary

This learning loop does not alter Claude Code configuration, existing DeepSeek behavior, model credentials, model endpoint selection, or session behavior. Model routing remains a separate execution-control concern.

## Final-report evidence

When learning memory is active, the final governed report should include:

```text
LEARNING MEMORY
Run-history refs: ...
Lesson candidates: none | <ids>
Approved practices recalled: none | <ids>
Practice promotion performed by this run: NO
Stale/conflicting memory flagged: none | <ids>
```

`Practice promotion performed by this run` must remain `NO` unless the change itself is an explicitly authorized governance change whose scope includes practice promotion.
