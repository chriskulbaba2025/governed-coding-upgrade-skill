# Governed Change Checklist

**Change ID:**  
**Protocol version:** 2.1.0  
**Checklist version:** 1.0.0  
**Branch:**  
**PR:**  
**Required starting SHA:**  
**Primary class:**  
**Release intent:** CHANGE_ONLY / STAGING_READY / PRODUCTION_READY  
**Objective:**  
**Terminal result when applicable:**  

## Production correctness

- [ ] Production spine traced where applicable.
- [ ] Producer → Contract → Consumer map complete.
- [ ] Identity/access continuity mapped where applicable.
- [ ] Terminal result identified for staging/production claims.

## Acceptance freeze

- [ ] Real production modules named.
- [ ] Controlled dependency seam named.
- [ ] Positive result frozen.
- [ ] Negative result frozen.
- [ ] Prohibited later effects frozen.
- [ ] False-PASS scan method defined.

## Protected invariants

- [ ] `INV-ID` — exact invariant

## Permitted files

- [ ] `path`

## Prohibited files

- [ ] `path/**`

## Ordered sections

### SECTION A — Boundary name

#### CHG-AREA-01 — Exact behavior name

- [ ] Behavior:
- [ ] Implementation boundary:
- [ ] Positive/unit proof:
- [ ] Acceptance/real-path proof:
- [ ] Negative/failure proof:
- [ ] Prohibited later effects:
- [ ] Protected invariant proof:
- [ ] Narrow verification command:
- [ ] Affected sections:
- [ ] Final-report evidence:

### Section A gate

- [ ] Existing real path inspected.
- [ ] Proof defined before implementation.
- [ ] Failing proof reproduced when safe/feasible.
- [ ] Narrow verification PASS.
- [ ] Negative proof PASS when required.
- [ ] Affected earlier sections remain PASS.
- [ ] SECTION A PASS — automatic continuation permitted.

## Cross-section review

- [ ] Upstream validated outputs match downstream consumers.
- [ ] No downstream validation bypass.
- [ ] No post-validation mutation where continuity is governed.

## Terminal verification

- [ ] Production acceptance PASS/N/A.
- [ ] False-PASS scan PASS.
- [ ] Terminal-path gate PASS/N/A.
- [ ] Full-system readiness gate PASS/N/A.
- [ ] Full regression PASS/N/A.
- [ ] Static/type/build/security PASS/N/A.
- [ ] Persistence/recovery PASS/N/A.
- [ ] Protected invariants PASS.
- [ ] Scope check PASS — unexpected files = 0; prohibited files = 0.
- [ ] Complete diff inspected.
- [ ] Terminal machine release gate PASS when required.
- [ ] Exact-head CI PASS when required.
- [ ] Independent exact-head audit PASS when required.

## Completion state

- [ ] CODE VERIFIED
- [ ] STAGING CANDIDATE
- [ ] CODE VERIFIED / GOVERNANCE HOLD
- [ ] RELEASE READY
- [ ] BLOCKED
