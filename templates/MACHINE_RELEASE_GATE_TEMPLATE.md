# Machine Release Gate Template

Use this template to convert final release judgment from agent prose into one executable repository gate.

The exact command is repository-specific. Prefer a stable responsibility name such as:

```text
change:release-gate
```

or a native equivalent such as:

```text
npm run change:release-gate
python scripts/change_release_gate.py
make change-release-gate
```

## Required contract

The gate must:

1. inspect the exact candidate branch and SHA;
2. execute or verify every mandatory machine-enforceable release condition;
3. return exit `0` only when all required conditions pass;
4. return non-zero when any required condition is failed, missing, stale, or cannot be tied to the exact candidate head;
5. print a checklist-style evidence summary;
6. never convert unavailable mandatory evidence into PASS.

## Recommended checks

Adapt only the rows that apply to the repository.

```text
[ ] exact repository identity
[ ] exact branch
[ ] exact final SHA
[ ] working-tree/protected-work state
[ ] frozen checklist complete
[ ] unexpected changed files == 0
[ ] prohibited changed files == 0
[ ] sequential section checks PASS
[ ] affected integration checks PASS/N/A
[ ] production acceptance PASS/N/A
[ ] negative-path checks PASS/N/A
[ ] schema/contract validation PASS/N/A
[ ] persistence/migration checks PASS/N/A
[ ] restart/recovery PASS/N/A
[ ] retry/idempotency/abort PASS/N/A
[ ] controlled credential isolation PASS/N/A
[ ] live provider/LLM call policy PASS
[ ] controlled/live call counters measured
[ ] full regression PASS/N/A
[ ] static/type/build/security checks PASS/N/A
[ ] protected invariants PASS
[ ] generated-artifact check PASS/N/A
[ ] complete diff evidence recorded
[ ] required exact-head CI PASS/N/A
[ ] independent exact-head audit PASS/N/A
[ ] PR/release state truthful
[ ] merge/deploy authorization truthful
```

## Balanced execution

The terminal gate is not a substitute for section-level narrow verification.

Use:

```text
section work
→ narrow section proof
→ affected integration when needed
→ all sections PASS
→ cross-section review
→ full terminal verification
→ machine release gate
```

Do not rerun the full repository regression after every isolated section unless repository governance requires it.

## Exact-head CI handling

When exact-head CI is mandatory:

```text
CI SUCCESS for exact final SHA
→ gate may continue

CI FAILURE
→ gate fails

CI unavailable / billing blocked / platform outage / run cannot start
→ gate fails the release-ready condition
→ report CODE VERIFIED / GOVERNANCE HOLD if local controlled verification otherwise passes
```

Local reruns do not substitute for mandatory exact-head CI.

If the branch remains unchanged, rerun CI and this gate against the same SHA once the external platform becomes available.

## Controlled external-call handling

Where tests exercise provider integrations:

- inject controlled transports/clients below real production adapters;
- isolate real credentials from controlled acceptance when feasible;
- fail on unexpected network/provider execution;
- collect actual call counters from controlled and live boundaries;
- never hardcode `0` calls or `$0.00` as PASS evidence.

## Suggested output

```text
MACHINE RELEASE GATE
Repository:
Branch:
SHA:

[x] scope — PASS — unexpected=0 prohibited=0
[x] acceptance — PASS — <command/result>
[x] regression — PASS — <command/result>
[x] external-call policy — PASS — live provider=0 live LLM=0
[x] exact-head CI — PASS/N/A — <run/SHA>
[x] independent audit — PASS/N/A — <evidence>

RESULT: PASS
```

or:

```text
MACHINE RELEASE GATE
Repository:
Branch:
SHA:

[x] local verification — PASS — <evidence>
[ ] exact-head CI — HOLD — mandatory CI unavailable

RESULT: GOVERNANCE HOLD
EXIT: non-zero
```

## Agent rule

A coding agent may not override the gate result with prose, confidence, or a locally substituted check.

```text
release-gate exit 0 + required authorization
→ RELEASE READY

release-gate non-zero because repository-controlled condition failed
→ BLOCKED

release-gate non-zero only because a mandatory temporary external release condition is unavailable while code verification passes
→ CODE VERIFIED / GOVERNANCE HOLD
```
