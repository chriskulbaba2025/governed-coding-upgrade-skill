# Mandatory Global Agent Invocation Rule

This is the canonical vendor-neutral invocation rule for Governed Coding Upgrade.

Install an equivalent rule in the persistent instruction layer of the coding agent or AI workspace being used.

```text
MANDATORY GOVERNED CODING CHANGES

For every task that intentionally changes source code, tests, schemas, APIs,
dependencies, executable configuration, migrations, persistence, jobs, external
integrations, security controls, infrastructure, build/release logic, generated
production artifacts, or runtime behavior, invoke and obey `governed-coding-upgrade`
before editing.

Do not assume the project stack. Run Project Discovery and verify the repository's
Project Adapter / governed profile. Record material unknowns as UNRESOLVED rather than
guessing architecture, commands, contracts, or boundaries.

Before implementation, preserve the requested requirement and pass the Surgical
Change Determinacy Gate. Freeze the required outcome, supporting evidence, change
hypothesis, causal boundary, expected change surface, protected surface, structural
change budget, acceptance proof, and scope-expansion conditions.

Discovery does not create authorization. Do not absorb an incidental defect, cleanup,
refactor, dependency update, hardening opportunity, rename, reorganization, or adjacent
feature into the active change merely because it was discovered or is nearby.

Every material changed production boundary must be causally necessary for the frozen
required outcome. “Useful”, “related”, “cleaner”, “safer”, and “while we are here” are
not sufficient causal justification.

The structural change budget governs architectural surface, not line count. Do not use
maximum lines changed, arbitrary diff-size limits, or function-count limits as a proxy
for surgicality.

If implementation requires a boundary outside the frozen determinacy contract or
exceeds the structural change budget, STOP. Do not broaden scope automatically. Reopen
the Surgical Change Determinacy Gate, establish direct causal necessity, update the
frozen contract, and only then continue.

Classify Change Tier as T1_LOCAL, T2_BOUNDARY, T3_SYSTEM, or T4_RELEASE and declare
Release Intent as CHANGE_ONLY, STAGING_READY, or PRODUCTION_READY. Change Tier controls
governance depth; Release Intent controls the readiness claim.

Select applicable Test Areas from STRUCTURE, UNIT, CONTRACT, INTEGRATION,
END_TO_END/ACCEPTANCE, DATA/MIGRATION, SECURITY/PRIVACY, RELIABILITY/RECOVERY,
EXTERNAL CALL/COST, PERFORMANCE/RESOURCE, COMPATIBILITY, and RELEASE/DEPLOYMENT.
Do not convert missing knowledge into N/A.

For cross-boundary production work, trace the Production Spine and material
Producer → Contract → Consumer handoffs before editing. Freeze acceptance before
production implementation and reject false-PASS proof.

Use agent roles only when they add value. Scout, Planner, Builder, Challenger,
Verifier, Auditor, and Release Authority are responsibilities, not model brands.
If Builder and Auditor share the same agent/context, report SELF_AUDIT.

When an execution orchestrator or AI policy authority is present, obey
`gcu-execution-control/1.0.0`. GCU must not select a concrete provider/model, store
provider credentials, silently escalate model capability, duplicate an authoritative
usage ledger, or treat Release Authority as an AI model-execution role. Preserve
applicable task/run, routing, approval, budget-envelope, and usage-receipt references.

When `gcu-learning-memory/1.0.0` is available, recalled approved practices are
ADVISORY_ONLY and never outrank current user instruction, repository authority, or
current evidence. The producing run must not auto-promote its own lesson candidate.

For ordered work, use the Sequential Evidence Gate:
inspect → define proof → reproduce failure when safe/feasible → implement the complete
bounded section → narrow verify → section audit → continue only on PASS.

After implementation, run a Causal Necessity Audit. For every material changed
boundary, map Requirement ID → changed boundary → why the requirement would remain
incorrect if that boundary were unchanged → direct evidence. Remove or separately
authorize unjustified changes. Use selective revert testing only when causal necessity
is disputed or cannot otherwise be established.

Before terminal acceptance for T2+ work, run the Challenger gate. Challenge the
requirement interpretation, causal hypothesis, scope, change budget, proof system,
negative paths, downstream consumers, and any apparent incidental adoption.

For STAGING_READY or PRODUCTION_READY, prove the terminal user/business promise. For
PRODUCTION_READY, prove all applicable full-system readiness responsibilities.

At exact head, verify the complete diff and run the Surgical Determinacy Audit:
requirement preserved; hypothesis validated; required outcome achieved; every material
changed boundary causally justified; protected surfaces preserved; structural change
budget respected or formally reopened; incidental findings excluded; unauthorized
scope expansion zero.

Do not claim RELEASE READY unless the required machine gate exits 0, required exact-head
CI passes for the exact final SHA, the applicable audit passes, and required release
authorization exists.

If controlled code verification passes but a mandatory external release or
execution-policy condition is unavailable, report CODE VERIFIED / GOVERNANCE HOLD.

Do not merge, deploy, release, activate, make prohibited live paid/provider/model calls,
change an AI policy route, or bypass a required budget/approval decision without the
authorization required by repository governance and current user instruction.
```
