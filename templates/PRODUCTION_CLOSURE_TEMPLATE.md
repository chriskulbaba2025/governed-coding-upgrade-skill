# Production Closure Template

Use when the objective is to close all known defects on one production path.

```text
Read and obey governed-coding-upgrade v2.1.0.
Activate PRODUCTION_CLOSURE.

Repository:
Branch:
PR:
Required starting SHA:
Release intent:
Terminal user/business promise:
Governing sources:
Objective:
Known blockers:

Before implementation:
1. Verify repository, branch, SHA, working tree, and authorization boundaries.
2. Preserve valid active work.
3. Trace the complete production spine.
4. Build the Producer → Contract → Consumer map.
5. Freeze acceptance proof and the false-PASS scan.
6. Convert all known same-path blockers into one frozen checklist.
7. Define permitted/prohibited files.
8. Define terminal-path and full-system readiness proof required by release intent.
9. Define the terminal machine-gate command.

For every ordered section:
INSPECT
→ DEFINE PROOF
→ REPRODUCE FAILURE when safe/feasible
→ IMPLEMENT COMPLETE SECTION
→ NARROW VERIFY
→ SECTION AUDIT
→ AUTO-CONTINUE ON PASS

Use balanced verification:
section proof
→ affected integration when required
→ all sections PASS
→ cross-section contract review
→ terminal-path/system-readiness checks
→ full terminal verification
→ machine gate
→ exact-head audit

Acceptance must execute real production modules with controlled dependencies below the production boundary. Do not substitute fabricated downstream success for the production producer being proved.

If the session is interrupted, resume the same repository/branch from the last directly proven section and preserve valid work.

If a production defect escaped earlier green proof, correct both the defect and the proof system that allowed it through.

Repository-owned work required by governing contracts is implementation work, not a final blocker. Stop only for a genuine governance, safety, authorization, or external dependency that cannot be resolved or controlled from the repository.

Do not merge, deploy, release, or activate without required authorization.

Final report must include:
Skill version: 2.1.0
Starting SHA:
Final SHA:
Exact files changed:
Release intent:
Production spine:
Contract map:
Acceptance freeze:
False-PASS scan:
Sequential section results:
Cross-section review:
Terminal-path gate:
Full-system readiness:
Terminal machine gate:
Exact-head CI:
Independent audit:
Repository state:
Final status:
```
