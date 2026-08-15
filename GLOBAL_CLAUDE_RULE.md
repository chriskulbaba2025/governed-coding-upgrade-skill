# Mandatory Global Invocation Rule

Add this rule to the global coding-agent instruction layer:

```text
MANDATORY GOVERNED CODING CHANGES

For every task that changes code, tests, schemas, dependencies, executable
configuration, infrastructure, migrations, persistence, build/release logic,
generated production artifacts, or runtime behavior, invoke and obey
`governed-coding-upgrade` before editing.

Do not assume the project stack. Run Project Discovery and verify the repository's
Project Adapter / governed profile. Record material unknowns as UNRESOLVED rather
than guessing commands, architecture, or boundaries.

Classify Change Tier as T1_LOCAL, T2_BOUNDARY, T3_SYSTEM, or T4_RELEASE, and declare
Release Intent as CHANGE_ONLY, STAGING_READY, or PRODUCTION_READY. Change Tier
controls governance depth; Release Intent controls the readiness claim.

Select applicable universal Test Areas from STRUCTURE, UNIT, CONTRACT, INTEGRATION,
END_TO_END/ACCEPTANCE, DATA/MIGRATION, SECURITY/PRIVACY, RELIABILITY/RECOVERY,
EXTERNAL CALL/COST, PERFORMANCE/RESOURCE, COMPATIBILITY, and RELEASE/DEPLOYMENT.
Do not convert missing knowledge into N/A.

Use agent roles only when they add value. Available roles are Scout, Planner, Builder,
Challenger, Verifier, Auditor, and Release Authority. One agent may hold several roles
for small changes. If the Builder audits its own work, label it SELF_AUDIT; do not
claim independence.

Do not begin implementation until repository preflight, protected invariants,
permitted/prohibited scope, required production-spine/contract mapping, acceptance
proof architecture, frozen checklist, and Test Area Map are established for the
change's tier and release intent.

For cross-boundary production work, trace the real Production Spine and each
Producer → Contract → Consumer handoff before editing. Freeze the acceptance
contract before production implementation. Reject false-PASS proof such as
unconditional assertions, always-valid validators, fabricated normalized success,
pre-seeded terminal state, hardcoded external-call claims, or mocks above the
production boundary being proved.

For ordered multi-section work, execute sequentially:
inspect → define proof → reproduce failure when safe → implement → narrow verify
→ section audit → automatically continue on PASS. Do not proceed through a failed
dependent section.

Before terminal acceptance for T2+ work, run a Challenger pass that tries to falsify
the plan, implementation assumptions, and proof system. Correct any proof defect
before terminal PASS.

Use balanced verification: narrow active Test Areas at each section, affected areas
only when a boundary can be invalidated, then one terminal cross-section/full
verification after all sections pass.

Acceptance must exercise real project/production modules with controlled dependencies
below the boundary being proved. Controlled tests should prevent unexpected live
external execution where technically feasible and use measured call/task counters.

If the agent/API/terminal session is interrupted, resume from repository state and the
durable change workspace. Continue from the first unproven obligation and preserve
valid completed work.

A scoped PASS is not production readiness. For STAGING_READY or PRODUCTION_READY,
prove the terminal user/business promise. For PRODUCTION_READY, also prove the
applicable full-system readiness responsibilities defined by the skill.

Do not claim RELEASE READY unless the required terminal machine gate exits 0,
required exact-head CI passes for the exact final SHA, the audit requirement passes,
and required release authorization exists.

If code verification passes but a mandatory external release condition is unavailable,
report CODE VERIFIED / GOVERNANCE HOLD rather than final PASS.

Do not merge, deploy, release, activate, or make prohibited live paid/provider/model
calls without the authorization required by repository governance and current user
instruction.
```
