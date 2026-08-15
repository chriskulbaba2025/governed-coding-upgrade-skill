# Governed Change Final Report

**Skill version:** 2.2.0

Record:

- change ID;
- Change Tier;
- Release Intent;
- Project Adapter version / verified SHA;
- starting SHA and final SHA;
- branch and PR;
- exact changed files;
- agent roster and audit separation (`INDEPENDENT` / `SELF_AUDIT` / N/A);
- Production Spine result;
- Producer → Contract → Consumer map result;
- acceptance-freeze result;
- false-PASS scan result;
- Challenger gate result;
- Test Area Map and per-area evidence;
- terminal-path result;
- full-system readiness result;
- checklist evidence;
- verification commands/results;
- scope/invariant result;
- machine gate;
- exact-head CI;
- audit result;
- external-call/cost evidence when applicable;
- repository state;
- release authorization.

Report `CHANGE RESULT` separately from `SYSTEM READINESS`.

Do not claim `RELEASE READY` while any mandatory proof or authorization is open or failed.

Recommended terminal block:

```text
CHANGE RESULT: PASS / BLOCKED
CHANGE TIER: T1_LOCAL / T2_BOUNDARY / T3_SYSTEM / T4_RELEASE
RELEASE INTENT: CHANGE_ONLY / STAGING_READY / PRODUCTION_READY
SYSTEM READINESS: NOT ASSESSED / BLOCKED / READY
AUDIT: INDEPENDENT / SELF_AUDIT / N/A — PASS / BLOCKED / HOLD
FINAL STATUS: CODE VERIFIED / STAGING CANDIDATE / GOVERNANCE HOLD / RELEASE READY / BLOCKED
```
