# Surgical Change Contract

**Change ID:**  
**Protocol version:** 2.3.0  
**Starting SHA:**  
**Change Tier:** T1_LOCAL / T2_BOUNDARY / T3_SYSTEM / T4_RELEASE  
**Release Intent:** CHANGE_ONLY / STAGING_READY / PRODUCTION_READY  
**Status:** DRAFT / FROZEN / REOPENED / PASS / BLOCKED  

## 1. Requirement Preservation

**Original requested outcome:**  

**Faithful governed interpretation:**  

**Explicit exclusions / non-goals:**  

**Observable acceptance condition:**  

## 2. Evidence and Change Hypothesis

**Observed/requested state:**  

**Direct evidence:**  

**Change hypothesis:**  

**Predicted effect:**  

**Hypothesis status:** PROVEN / DISPROVEN / UNRESOLVED  

> Material causal facts must not remain UNRESOLVED at implementation start.

## 3. Causal Boundary

**Smallest directly supported responsible boundary:**  

**Why this boundary is responsible:**  

## 4. Expected Change Surface

### REQUIRED

- `module / contract / component`

### EXPECTED when determinable

- `symbol / function / method`

### PROHIBITED

- `unrelated boundary / public behavior / path`

## 5. Protected Surface

- `invariant / module / contract / behavior that must remain unchanged`

Anything outside the justified causal chain is protected by default unless explicitly added to the frozen contract.

## 6. Structural Change Budget

| Surface | Frozen budget | Actual | Result |
|---|---:|---:|---|
| Production modules | | | PASS/BLOCKED |
| Public contracts | | | PASS/BLOCKED |
| Schemas | | | PASS/BLOCKED |
| Persistence boundaries | | | PASS/BLOCKED |
| Dependencies | | | PASS/BLOCKED |
| External integrations | | | PASS/BLOCKED |
| Configuration surfaces | | | PASS/BLOCKED |
| New abstractions | | | PASS/BLOCKED |
| Migrations | | | PASS/BLOCKED |
| Bounded test surfaces | | | PASS/BLOCKED |

Do not use line count, arbitrary diff size, or function count as a surgicality proxy.

## 7. Acceptance Proof

**Positive proof:**  

**Negative/preservation proof when applicable:**  

**Exact verification mechanism:**  

## 8. Expansion Conditions

If implementation requires an unlisted boundary or exceeds a frozen budget dimension:

```text
STOP
→ record evidence
→ reopen this contract
→ prove causal necessity
→ update frozen surface/budget
→ continue only after the determinacy gate passes again
```

**Reopen history:**  

## 9. Incidental Findings

| Finding | Evidence | Required for frozen outcome? | Disposition |
|---|---|---|---|
| | | YES/NO | absorbed only after gate reopen / separate change / no action |

Discovery does not create authorization.

## 10. Causal Necessity Audit

| Requirement ID | Material changed boundary | Why outcome remains incorrect if unchanged | Direct evidence | Result |
|---|---|---|---|---|
| | | | | PASS/BLOCKED |

Selective revert testing is required only when causal necessity remains disputed or insufficiently supported.

## 11. Surgical Determinacy Audit

- [ ] Requirement preserved.
- [ ] Change hypothesis validated.
- [ ] Required outcome achieved.
- [ ] Every material changed boundary causally justified.
- [ ] Protected surfaces preserved.
- [ ] Structural change budget respected or formally reopened.
- [ ] Incidental findings excluded unless separately justified and frozen.
- [ ] Unauthorized scope expansion = 0.
- [ ] Unjustified architectural change = 0.
- [ ] Unjustified contract change = 0.
- [ ] Unjustified dependency change = 0.

**SURGICAL DETERMINACY:** PASS / BLOCKED
