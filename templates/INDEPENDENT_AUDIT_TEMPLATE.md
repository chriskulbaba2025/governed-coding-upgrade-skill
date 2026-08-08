# Independent Exact-Head Audit

Audit the governed change at exact head `[SHA]`.

Do not modify, merge, deploy, release, or activate during the audit.

## Read

- `SKILL.md`
- repository `GOVERNED_CHANGE_PROFILE.md`
- frozen change checklist
- governing repository contracts/invariants

## Verify every checklist ID

1. Inspect the actual implementation at the exact head.
2. Inspect the exact proof claimed for the ID.
3. Confirm acceptance/runtime behavior where required.
4. Confirm negative-path state, events, calls, writes, or artifacts where governed.
5. Confirm protected invariants.
6. Mark the ID `PASS` or `BLOCKED`.

## Repository checks

- [ ] Reported final SHA equals inspected head.
- [ ] CI, when required, ran against that exact SHA.
- [ ] Changed files remain inside permitted scope.
- [ ] Prohibited files are untouched.
- [ ] Every completion claim has direct proof.
- [ ] No `A OR B` assertion replaces a single governed result.
- [ ] No missing requirement is hidden as a limitation.
- [ ] Required protected invariants remain intact.
- [ ] Release authorization has not been assumed.

## Return

```text
PASS
```

or:

```text
BLOCKED — failed checklist IDs and exact evidence
```
