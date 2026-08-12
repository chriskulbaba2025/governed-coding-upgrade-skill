# Mandatory Global Invocation Rule

Add this rule to the global coding-agent instruction layer so the skill is invoked consistently rather than merely being available:

```text
MANDATORY GOVERNED CODING CHANGES

For every task that changes code, tests, schemas, dependencies, executable
configuration, infrastructure-as-code, build/release logic, migrations,
persistence, or runtime behavior, invoke and obey the
`governed-coding-upgrade` skill before editing.

Do not bypass the skill because a change appears small.
Do not begin implementation until repository preflight, protected invariants,
permitted/prohibited file scope, and the frozen checklist are established.

When the user asks to finish production readiness, fix all known blockers, make
the complete path work, or continue until clean, activate PRODUCTION_CLOSURE.
Repository-owned missing infrastructure required by an already-governed contract
is implementation work, not a final blocker.

For multi-section closure, execute sections sequentially:
inspect → define proof → reproduce failure when safe → implement → narrow verify
→ section audit → automatically continue on PASS. Do not proceed past a failed
section. Do not ask for routine approval between passed sections unless the next
step crosses an explicit authorization boundary.

Use balanced machine verification: narrow checks at each section, affected
integration checks only when a boundary can be invalidated, then cross-section
review plus full acceptance/regression/invariant/scope verification once all
sections pass.

Acceptance must exercise the real production implementation with controlled
injected dependencies rather than fabricated downstream success objects.
Controlled tests should isolate real provider/LLM credentials when technically
possible, fail unexpected live network execution, and measure actual controlled
and live call counts rather than hardcoding PASS.

If an API/agent/terminal response is interrupted, resume from repository state,
inspect the current diff/task/checklist evidence, identify the last directly
proven section, and continue from the first unproven section. Do not restart
completed valid work merely because the connection ended.

Do not claim RELEASE READY unless the repository's required terminal machine
release gate exits 0, required exact-head CI passes for the exact final SHA, and
the independent exact-head audit passes. Agent prose, confidence, local
substitutes, and environmental explanations cannot override a failed required
gate.

If local controlled verification passes but mandatory external CI/platform proof
is temporarily unavailable, report CODE VERIFIED / GOVERNANCE HOLD rather than
final PASS. Rerun the external proof and machine gate against the unchanged exact
SHA when the external dependency becomes available.

Do not merge, deploy, release, activate, or make prohibited live paid/provider
or LLM calls without the authorization required by repository governance and
the current user instruction.
```
