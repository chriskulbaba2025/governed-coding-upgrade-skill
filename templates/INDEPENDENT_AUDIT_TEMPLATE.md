# Independent Exact-Head Audit

Audit the governed change at exact head `[SHA]`.

Do not modify, merge, deploy, release, or activate during the audit.

## Read

- `SKILL.md`
- repository `GOVERNED_CHANGE_PROFILE.md`
- frozen change checklist
- governing repository contracts/invariants
- terminal machine release-gate evidence when configured

## Verify every checklist ID

1. Inspect the actual implementation at the exact head.
2. Inspect the exact proof claimed for the ID.
3. Confirm acceptance/runtime behavior where required.
4. Confirm negative-path state, events, calls, writes, or artifacts where governed.
5. Confirm protected invariants.
6. Mark the ID `PASS` or `BLOCKED`.

## Sequential execution checks

- [ ] Multi-section work was divided into stable checklist sections/groups.
- [ ] Each section has direct PASS evidence before dependent sections rely on it.
- [ ] Failed sections were corrected before progression.
- [ ] Affected earlier boundaries were rerun when later work could invalidate them.
- [ ] Cross-section integration was reviewed before terminal verification.

## Real-path and external-call checks

- [ ] Acceptance uses real production adapters/services/orchestration with controlled dependencies.
- [ ] No fabricated downstream success objects substitute for production execution.
- [ ] Real provider/LLM credentials were isolated from controlled acceptance where technically feasible.
- [ ] Unexpected live network/provider execution fails closed where the repository can enforce it.
- [ ] Controlled/live provider and model calls are measured from actual counters, not hardcoded PASS.

## Repository checks

- [ ] Reported final SHA equals inspected head.
- [ ] CI, when required, ran against that exact SHA.
- [ ] Changed files remain inside permitted scope.
- [ ] Prohibited files are untouched.
- [ ] Every completion claim has direct proof.
- [ ] No `A OR B` assertion replaces a single governed result.
- [ ] No missing requirement is hidden as a limitation.
- [ ] Required protected invariants remain intact.
- [ ] Complete diff was inspected.
- [ ] Terminal machine release-gate result is truthful.
- [ ] Release authorization has not been assumed.

## CI / machine-gate distinction

If local controlled verification passes but mandatory exact-head CI is unavailable:

```text
CODE VERIFIED / GOVERNANCE HOLD
```

Do not return final governed PASS merely because equivalent local commands passed.

## Return

```text
PASS
```

only when every mandatory exact-head release condition is satisfied.

Otherwise return:

```text
BLOCKED or GOVERNANCE HOLD
Failed checklist IDs or release condition:
Exact evidence:
Smallest required correction/action:
```
