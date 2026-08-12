# Governed Change Final Report

**Skill version:** 1.2.0  
**Starting SHA:**  
**Final SHA:**  
**Branch:**  
**PR:**  
**Change class:**  

## Exact files changed

- 

## Sequential section/checklist results

- [x] `CHG-ID` — PASS — exact assertion/test/state/artifact evidence
- [ ] `CHG-ID` — FAIL — exact evidence

## Verification

- [x] Preflight — PASS — exact repo/branch/SHA/tree evidence
- [x] Narrow section checks — PASS — command/result
- [x] Affected integration — PASS/N/A — command/result
- [x] Cross-section review — PASS/N/A — exact evidence
- [x] Production acceptance — PASS/N/A — command/result
- [x] Negative proofs — PASS/N/A — state/call/write evidence
- [x] Persistence/recovery/idempotency — PASS/N/A — evidence
- [x] Credential isolation/live-call guard — PASS/N/A — evidence
- [x] Full regression — PASS/N/A — command/result
- [x] Protected invariants — PASS — exact evidence
- [x] Scope check — PASS — unexpected=0; prohibited=0
- [x] Terminal machine release gate — PASS/BLOCKED/N/A — command + exit code
- [x] Exact-head CI — PASS/BLOCKED/N/A — exact SHA/run

## External effects

- Controlled provider calls:
- Live provider calls:
- Controlled model calls:
- Live LLM calls:
- Paid task calls:
- Measured controlled cost:
- Production mutations:

## Exact-head state

- CI run:
- Git status:
- PR state:
- Independent audit:
- Correction rounds:
- Merge/release authorization:

## Final disposition

Choose exactly one:

```text
CODE VERIFIED
```

```text
STAGING CANDIDATE
```

```text
CODE VERIFIED / GOVERNANCE HOLD
Reason:
Mandatory external condition:
Exact SHA to re-verify later:
```

```text
RELEASE READY
```

```text
BLOCKED
Failed checklist/release condition:
Exact evidence:
```

Do not claim `RELEASE READY` while any required checklist item, machine release gate, exact-head CI requirement, independent audit requirement, or authorization prerequisite is open or failed.

A local substitute does not satisfy mandatory exact-head CI.
