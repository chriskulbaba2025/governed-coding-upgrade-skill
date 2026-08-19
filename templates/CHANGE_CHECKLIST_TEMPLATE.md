# Governed Change Checklist

**Change ID:**  
**Protocol version:** 2.3.0  
**Checklist version:** 1.2.0  
**Branch:**  
**PR:**  
**Required starting SHA:**  
**Change Tier:** T1_LOCAL / T2_BOUNDARY / T3_SYSTEM / T4_RELEASE  
**Release intent:** CHANGE_ONLY / STAGING_READY / PRODUCTION_READY  
**Objective:**  
**Project Adapter verified SHA:**  
**Terminal result when applicable:**  

## Discovery and adaptation

- [ ] Repository/component boundaries inspected.
- [ ] Project Adapter verified or material gaps marked `UNRESOLVED`.
- [ ] Governing sources identified.
- [ ] Change Tier justified.
- [ ] Agent roster/separation recorded when used.
- [ ] Test Area Map created; N/A reasons are explicit.

## Requirement Preservation

- [ ] Original requested outcome recorded faithfully.
- [ ] Governed interpretation remains implementation-independent.
- [ ] Explicit exclusions/non-goals recorded.
- [ ] Observable acceptance condition frozen.

## Surgical Change Determinacy Gate

- [ ] Direct evidence recorded.
- [ ] Change hypothesis is PROVEN; material causal facts are not UNRESOLVED.
- [ ] Causal boundary identified.
- [ ] REQUIRED/EXPECTED/PROHIBITED change surface frozen.
- [ ] Protected surface frozen.
- [ ] Structural change budget frozen.
- [ ] Acceptance proof frozen.
- [ ] Expansion conditions frozen.
- [ ] Incidental findings do not create authorization.
- [ ] Gate status = PASS before implementation.

## Production correctness

- [ ] Production Spine traced where applicable.
- [ ] Producer → Contract → Consumer map complete where applicable.
- [ ] Identity/access continuity mapped where applicable.
- [ ] Terminal result identified for staging/production claims.

## Acceptance freeze

- [ ] Real project/production modules named.
- [ ] Controlled dependency seam named.
- [ ] Positive result frozen.
- [ ] Negative result frozen.
- [ ] Prohibited later effects frozen.
- [ ] False-PASS scan method defined.

## Protected invariants

- [ ] `INV-ID` — exact invariant

## Permitted files / boundaries

- [ ] `path or boundary`

## Prohibited files / boundaries

- [ ] `path/** or boundary`

## Ordered sections

### SECTION A — Boundary name

#### CHG-AREA-01 — Exact behavior name

- [ ] Behavior:
- [ ] Implementation boundary:
- [ ] Active test areas:
- [ ] Positive/unit proof:
- [ ] Contract/integration proof when applicable:
- [ ] Acceptance/real-path proof when applicable:
- [ ] Negative/failure proof:
- [ ] Prohibited later effects:
- [ ] Protected invariant proof:
- [ ] Narrow verification command:
- [ ] Affected sections/test areas:
- [ ] Final-report evidence:

### Section A gate

- [ ] Existing real path inspected.
- [ ] Proof defined before implementation.
- [ ] Failing proof reproduced when safe/feasible.
- [ ] Implementation stayed inside frozen determinacy boundary or gate was formally reopened first.
- [ ] Narrow active Test Areas PASS.
- [ ] Negative proof PASS when required.
- [ ] Affected earlier sections/boundaries remain PASS.
- [ ] SECTION A PASS — automatic continuation permitted.

## Causal Necessity Audit

- [ ] Every material changed boundary maps to a Requirement ID.
- [ ] Each mapping states why the requirement remains incorrect if the boundary is unchanged.
- [ ] Each mapping has direct evidence.
- [ ] Unjustified material changes removed or separately authorized.
- [ ] Selective revert proof used where necessity remained disputed.

## Challenger gate

- [ ] Original requirement versus governed interpretation challenged.
- [ ] Change hypothesis and causal boundary challenged.
- [ ] Structural change budget and any reopen events challenged.
- [ ] Incidental-finding adoption challenged.
- [ ] False-PASS risks challenged.
- [ ] Downstream consumer/compatibility gaps checked.
- [ ] Missing negative/recovery/security cases checked.
- [ ] Adapter staleness checked.
- [ ] Proof would fail if the governed defect remained.

## Cross-section review

- [ ] Upstream validated outputs match downstream consumers.
- [ ] No downstream validation bypass.
- [ ] No post-validation mutation where continuity is governed.
- [ ] Shared monorepo/component boundaries PASS when applicable.

## Terminal verification

- [ ] All ACTIVE Test Areas PASS.
- [ ] All N/A Test Areas have direct reasons.
- [ ] Material UNRESOLVED Test Areas = 0 for declared result.
- [ ] Production acceptance PASS/N/A.
- [ ] False-PASS scan PASS.
- [ ] Challenger gate PASS/N/A.
- [ ] Terminal-path gate PASS/N/A.
- [ ] Full-system readiness gate PASS/N/A.
- [ ] Full regression PASS/N/A.
- [ ] Protected invariants PASS.
- [ ] Scope check PASS — unexpected files = 0; prohibited files = 0.
- [ ] Complete diff inspected.
- [ ] Surgical Determinacy Audit PASS.
- [ ] Terminal machine release gate PASS when required.
- [ ] Exact-head CI PASS when required.
- [ ] Audit PASS and separation truthfully labeled.

## Completion state

- [ ] CODE VERIFIED
- [ ] STAGING CANDIDATE
- [ ] CODE VERIFIED / GOVERNANCE HOLD
- [ ] RELEASE READY
- [ ] BLOCKED
