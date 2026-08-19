# Exact-Head Audit

Audit the governed change at exact head `[SHA]`.

**Audit separation:** INDEPENDENT / SELF_AUDIT  
**Change Tier:** T1_LOCAL / T2_BOUNDARY / T3_SYSTEM / T4_RELEASE  
**Release Intent:** CHANGE_ONLY / STAGING_READY / PRODUCTION_READY  

Do not modify, merge, deploy, release, or activate during the audit.

If the Builder and Auditor are the same agent/context, mark `SELF_AUDIT`. Do not claim independence.

## Read

- `SKILL.md`
- repository Project Adapter and/or legacy Governed Change Profile
- change intake/discovery record when used
- frozen Surgical Change Contract
- frozen change checklist
- Agent Roster when used
- Test Area Map
- production-spine/contract-map record when applicable
- frozen acceptance contract when applicable
- governing repository contracts/invariants
- terminal machine-gate evidence when configured

## Adaptation checks

- [ ] Project Adapter facts used by the change are supported at the recorded verified SHA or were re-verified.
- [ ] Material unknowns were not converted to N/A.
- [ ] Affected components/workspaces are correctly identified.
- [ ] Change Tier matches the changed boundaries.
- [ ] Agent/audit separation is labeled truthfully.
- [ ] Every active Test Area has direct evidence.
- [ ] Every N/A Test Area has a direct reason.

## Requirement and surgical determinacy checks

- [ ] Original requested outcome was preserved faithfully.
- [ ] Governed interpretation did not silently add implementation scope.
- [ ] Change hypothesis was proven before implementation or the gate was formally reopened after contrary evidence.
- [ ] Causal boundary is directly supported.
- [ ] Expected and protected surfaces were frozen before implementation.
- [ ] Structural change budget measures architectural surface, not line count/diff size.
- [ ] Budget exceedance caused a stop/reopen before new-boundary implementation.
- [ ] Discovery did not create authorization for incidental work.
- [ ] Every material changed boundary has Causal Necessity Audit evidence.
- [ ] Unauthorized scope expansion = 0.
- [ ] Unjustified architectural/contract/dependency changes = 0.
- [ ] Surgical Determinacy Audit = PASS.

## Production correctness checks

- [ ] Declared Release Intent matches the claim being made.
- [ ] Production Spine is complete where required.
- [ ] Material Producer → Contract → Consumer handoffs are mapped and proven.
- [ ] Acceptance architecture was frozen before implementation where required.
- [ ] False-PASS scan found no prohibited proof substitute.
- [ ] Challenger findings are resolved or explicitly block the result.
- [ ] Validated-object continuity holds at governed boundaries.
- [ ] Terminal result is proven for staging/production claims.
- [ ] Full-system readiness is complete when PRODUCTION_READY is claimed.
- [ ] Cross-account/cross-tenant rejection is proven where applicable.

## Sequential execution checks

- [ ] Ordered work used stable checklist sections.
- [ ] Each section has direct PASS evidence before dependent sections rely on it.
- [ ] Failed sections were corrected before progression.
- [ ] Affected earlier boundaries/test areas were rerun when later work could invalidate them.
- [ ] Cross-section integration was reviewed before terminal verification.

## Real-path checks

- [ ] Acceptance uses real project/production modules with controlled dependencies.
- [ ] Fabricated downstream success does not substitute for real execution.
- [ ] Measured counters/state/artifacts support side-effect claims where applicable.

## Repository checks

- [ ] Reported final SHA equals inspected head.
- [ ] Required CI ran against that exact SHA.
- [ ] Changed files remain inside permitted/frozen causal scope.
- [ ] Prohibited files are untouched.
- [ ] Every completion claim has direct proof.
- [ ] No `A OR B` assertion replaces one governed result.
- [ ] No missing requirement is hidden as a limitation.
- [ ] Protected invariants remain intact.
- [ ] Complete diff was inspected.
- [ ] Terminal machine-gate result is truthful.
- [ ] Release authorization has not been assumed.

## CI / governance-hold distinction

If controlled code verification passes but mandatory exact-head external proof is unavailable:

```text
CODE VERIFIED / GOVERNANCE HOLD
```

Do not return final governed PASS from local substitutes.

## Return

Return `PASS` only when every mandatory condition for the declared result is satisfied.

Otherwise return:

```text
BLOCKED or GOVERNANCE HOLD
Failed requirement/checklist IDs / Test Areas / determinacy or release condition:
Exact evidence:
Smallest causally justified correction/action:
```
