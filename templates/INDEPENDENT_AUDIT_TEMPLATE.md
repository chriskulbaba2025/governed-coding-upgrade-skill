# Independent Exact-Head Audit

Audit the governed change at exact head `[SHA]`.

Do not modify, merge, deploy, release, or activate during the audit.

## Read

- `SKILL.md`
- repository Governed Change Profile
- frozen change checklist
- production-spine/contract-map record when applicable
- frozen acceptance contract when applicable
- governing repository contracts/invariants
- terminal machine-gate evidence when configured

## Production correctness checks

- [ ] Declared release intent matches the claim being made.
- [ ] Production spine is complete for the declared release intent.
- [ ] Material Producer → Contract → Consumer handoffs are mapped and proven.
- [ ] Acceptance architecture was frozen before implementation where required.
- [ ] False-PASS scan found no prohibited proof substitute.
- [ ] Validated-object continuity holds at governed boundaries.
- [ ] Terminal result is proven for staging/production claims.
- [ ] Full-system readiness is complete when PRODUCTION_READY is claimed.
- [ ] Cross-account/cross-tenant rejection is proven where applicable.

## Sequential execution checks

- [ ] Ordered work used stable checklist sections.
- [ ] Each section has direct PASS evidence before dependent sections rely on it.
- [ ] Failed sections were corrected before progression.
- [ ] Affected earlier boundaries were rerun when later work could invalidate them.
- [ ] Cross-section integration was reviewed before terminal verification.

## Real-path checks

- [ ] Acceptance uses real production modules with controlled dependencies.
- [ ] Fabricated downstream success does not substitute for production execution.
- [ ] Measured counters/state/artifacts support side-effect claims where applicable.

## Repository checks

- [ ] Reported final SHA equals inspected head.
- [ ] Required CI ran against that exact SHA.
- [ ] Changed files remain inside permitted scope.
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
Failed checklist IDs or release condition:
Exact evidence:
Smallest required correction/action:
```
