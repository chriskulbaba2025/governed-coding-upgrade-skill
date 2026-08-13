# Machine Release Gate Template

Use this template to convert final release judgment from agent prose into one executable repository gate.

Prefer a stable repository command such as:

```text
change:release-gate
```

## Required contract

The gate must:

1. inspect the exact candidate branch and SHA;
2. execute or verify every mandatory machine-enforceable condition;
3. exit `0` only when all required conditions pass;
4. return non-zero when required evidence is failed, missing, stale, or cannot be tied to the exact candidate head;
5. print checklist-style evidence;
6. never convert unavailable mandatory evidence into PASS.

## Recommended checks

```text
[ ] exact repository identity
[ ] exact branch and SHA
[ ] declared release intent truthful
[ ] production spine / contract map PASS/N/A
[ ] acceptance contract freeze PASS/N/A
[ ] false-PASS scan PASS
[ ] frozen checklist complete
[ ] unexpected changed files == 0
[ ] prohibited changed files == 0
[ ] sequential sections PASS
[ ] affected integration PASS/N/A
[ ] production acceptance PASS/N/A
[ ] negative-path checks PASS/N/A
[ ] contract validation PASS/N/A
[ ] persistence/recovery PASS/N/A
[ ] terminal-path gate PASS/N/A
[ ] full-system readiness PASS/N/A
[ ] full regression PASS/N/A
[ ] static/type/build/security PASS/N/A
[ ] protected invariants PASS
[ ] generated-artifact check PASS/N/A
[ ] complete diff evidence recorded
[ ] required exact-head CI PASS/N/A
[ ] independent exact-head audit PASS/N/A
[ ] PR/release state truthful
[ ] release authorization truthful
```

## Balanced execution

```text
section work
→ narrow proof
→ affected integration when needed
→ all sections PASS
→ cross-section review
→ terminal-path/system-readiness checks
→ full terminal verification
→ machine release gate
```

## Exact-head CI handling

Mandatory CI success must correspond to the exact final SHA. If mandatory CI is temporarily unavailable, the release-ready condition fails and the appropriate state is `CODE VERIFIED / GOVERNANCE HOLD` when code verification otherwise passes.

Local reruns do not substitute for mandatory exact-head CI.

## Agent rule

The coding agent may not override the gate result with prose or confidence.

```text
gate exit 0 + required authorization
→ RELEASE READY

gate non-zero because repository-controlled requirement failed
→ BLOCKED

gate non-zero only because mandatory temporary external release proof is unavailable while code verification passes
→ CODE VERIFIED / GOVERNANCE HOLD
```
