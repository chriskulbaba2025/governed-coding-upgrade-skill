# Mandatory Global Invocation Rule

Add this rule to the global coding-agent instruction layer:

```text
MANDATORY GOVERNED CODING CHANGES

For every task that changes code, tests, schemas, dependencies, executable
configuration, infrastructure, migrations, persistence, build/release logic,
or runtime behavior, invoke and obey `governed-coding-upgrade` before editing.

Declare release intent as CHANGE_ONLY, STAGING_READY, or PRODUCTION_READY.
Do not begin implementation until repository preflight, protected invariants,
permitted/prohibited scope, production-spine/contract mapping when applicable,
acceptance proof architecture, and the frozen checklist are established.

For cross-boundary production work, trace the real production spine and each
Producer → Contract → Consumer handoff before editing. Freeze the acceptance
contract before production implementation. Reject false-PASS proof such as
unconditional assertions, always-valid validators, fabricated normalized success,
pre-seeded terminal state, hardcoded external-call claims, or mocks above the
production boundary being proved.

For multi-section work, execute sequentially:
inspect → define proof → reproduce failure when safe → implement → narrow verify
→ section audit → automatically continue on PASS. Do not proceed through a failed
section. Routine section PASS does not require approval unless the next action
crosses an explicit authorization boundary.

Use balanced verification: narrow checks at each section, affected integration
only when a boundary can be invalidated, then one terminal cross-section/full
verification after all sections pass.

Acceptance must exercise real production modules with controlled dependencies
below the production boundary. Controlled tests should prevent unexpected live
external execution where technically feasible and use measured call/task counters.

If the agent/API/terminal session is interrupted, resume from repository state and
continue from the first unproven section; preserve valid completed work.

A scoped PASS is not production readiness. For STAGING_READY or PRODUCTION_READY,
prove the terminal user/business promise. For PRODUCTION_READY, also prove the
applicable full-system readiness responsibilities defined by the skill.

Do not claim RELEASE READY unless the required terminal machine gate exits 0,
required exact-head CI passes for the exact final SHA, the independent exact-head
audit passes, and required release authorization exists.

If code verification passes but a mandatory external release condition is
unavailable, report CODE VERIFIED / GOVERNANCE HOLD rather than final PASS.

Do not merge, deploy, release, activate, or make prohibited live paid/provider/model
calls without the authorization required by repository governance and current user
instruction.
```
