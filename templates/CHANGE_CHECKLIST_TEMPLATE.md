# Governed Change Checklist

**Change ID:**  
**Protocol version:** 1.2.0  
**Checklist version:** 1.0.0  
**Branch:**  
**PR:**  
**Required starting SHA:**  
**Primary class:**  
**Objective:**  

## Protected invariants

- [ ] `INV-ID` — exact invariant

## Permitted files

- [ ] `path`

## Prohibited files

- [ ] `path/**`

## Ordered sections / requirements

Use one section per architectural boundary when the change is multi-section. Complete sections sequentially.

### SECTION A — Boundary name

#### CHG-AREA-01 — Exact behavior name

- [ ] Behavior:
- [ ] Implementation boundary:
- [ ] Positive/unit proof:
- [ ] Acceptance/real-path proof:
- [ ] Negative/failure proof:
- [ ] Prohibited later calls/events/writes:
- [ ] Protected invariant proof:
- [ ] Narrow verification command:
- [ ] Affected earlier/later sections:
- [ ] Final-report evidence:

### Section A gate

- [ ] Existing real path inspected.
- [ ] Proof defined before implementation.
- [ ] Required failing proof reproduced when safe/feasible.
- [ ] Narrow verification PASS.
- [ ] Required negative proof PASS.
- [ ] Earlier affected sections remain PASS.
- [ ] SECTION A PASS — automatic continuation permitted.

## Cross-section review

- [ ] Upstream validated outputs match downstream consumers.
- [ ] No downstream bypass of governed validation.
- [ ] No mutation after validation where exact model/object identity is governed.
- [ ] Cross-section defects corrected in owning section and affected sections rerun.

## Balanced terminal verification

- [ ] Production acceptance PASS/N/A.
- [ ] Full regression PASS/N/A.
- [ ] Static/type/build/security PASS/N/A.
- [ ] Persistence/migration/recovery/idempotency PASS/N/A.
- [ ] Controlled credential isolation/live-call guard PASS/N/A.
- [ ] Protected invariants PASS.
- [ ] Scope check PASS — unexpected files = 0; prohibited files = 0.
- [ ] Generated-artifact check PASS/N/A.
- [ ] Complete diff inspected.
- [ ] Terminal machine release gate PASS when required.
- [ ] Exact-head CI PASS when required.
- [ ] Independent exact-head audit PASS when required.

## Completion state

Select one supported state from evidence:

- [ ] CODE VERIFIED
- [ ] STAGING CANDIDATE
- [ ] CODE VERIFIED / GOVERNANCE HOLD
- [ ] RELEASE READY
- [ ] BLOCKED

Merge/release remains subject to required authorization.
