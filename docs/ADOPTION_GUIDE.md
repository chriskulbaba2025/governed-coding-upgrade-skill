# Adoption Guide

## Objective

Install Governed Coding Upgrade v2.2.0 so qualifying coding changes use one universal governance lifecycle while each repository supplies its own facts through a Project Adapter and, where present, integrates cleanly with an external execution control plane.

The goal is portability without weakening proof or duplicating routing, billing, orchestration, or release authority.

## 1. Install the skill

Place `SKILL.md` in the coding agent's reusable skill location under:

```text
governed-coding-upgrade
```

Load it as an authoritative execution skill, not optional reference material.

## 2. Install the global invocation rule

Add `GLOBAL_CLAUDE_RULE.md` to the global coding-agent instruction layer.

## 3. Run Project Discovery

Before creating an adapter, inspect the repository and record directly supported facts:

- project kinds and component/workspace boundaries;
- languages/runtimes/build systems;
- test frameworks and commands;
- CI/release mechanisms;
- persistence/migrations/background work;
- external systems and controlled-test seams;
- security/privacy/tenant boundaries;
- execution orchestrator / AI policy authority when present;
- generated/protected paths;
- rollback/recovery mechanisms;
- repository governance.

Unknown material facts are `UNRESOLVED`, not guessed.

See [`UNIVERSAL_PROJECT_MODEL.md`](UNIVERSAL_PROJECT_MODEL.md).

## 4. Create the Project Adapter

Preferred path:

```text
.governance/PROJECT_ADAPTER.md
```

Use [`../templates/PROJECT_ADAPTER_TEMPLATE.md`](../templates/PROJECT_ADAPTER_TEMPLATE.md).

The adapter maps universal GCU test/proof capabilities to the repository's real commands and boundaries.

Existing repositories using `.governance/GOVERNED_CHANGE_PROFILE.md` remain compatible. They may keep it, add the adapter beside it, or migrate facts gradually.

## 5. Establish protected invariants

Record behaviors/artifacts that may not change without explicit authorization, including applicable API/schema contracts, data/access isolation, lifecycle transitions, authentication/authorization, migrations, golden/reference artifacts, generated output, dependency compatibility, external-call restrictions, deployment, model-route authority when applicable, and rollback.

## 6. Classify Change Tier

For each change, declare one:

- `T1_LOCAL`
- `T2_BOUNDARY`
- `T3_SYSTEM`
- `T4_RELEASE`

Change Tier scales governance depth based on affected boundaries.

It does not replace Release Intent.

## 7. Declare Release Intent

Every governed change declares:

- `CHANGE_ONLY`;
- `STAGING_READY`; or
- `PRODUCTION_READY`.

Do not let a green scoped change imply a higher readiness state than it proved.

## 8. Select an agent roster when useful

Use [`../templates/AGENT_ROSTER_TEMPLATE.md`](../templates/AGENT_ROSTER_TEMPLATE.md).

Available governance roles:

- Scout;
- Planner;
- Builder;
- Challenger;
- Verifier;
- Auditor;
- Release Authority.

A small T1 change may use one agent for several roles. A higher-risk T3/T4 change should use stronger separation when practical or required.

If the Builder audits its own work, label it `SELF_AUDIT`.

**Release Authority is not an AI execution role.** It remains human/repository controlled and may not be model-dispatched.

See [`AGENT_ORCHESTRATION.md`](AGENT_ORCHESTRATION.md).

## 9. Register the Execution Control Plane when present

If the coding agent runs behind an execution orchestrator, model gateway, or AI policy platform, adopt [`EXECUTION_CONTROL_PLANE_INTEGRATION.md`](EXECUTION_CONTROL_PLANE_INTEGRATION.md) and record the authority boundaries in the Project Adapter.

Contract:

```text
gcu-execution-control/1.0.0
```

Record, when applicable:

```text
Execution orchestrator
AI policy authority
Capability mapping owner
Budget-envelope authority
Model-route approval authority
Usage-ledger authority
Usage-receipt lookup method
Escalation / human-wait mechanism
Independent-context mechanism
Direct-provider/model-call policy
```

GCU requests provider-neutral capability only:

```text
ECONOMY
STANDARD
ADVANCED
PREMIUM
```

GCU does not choose concrete providers/models, hold provider credentials, silently escalate, maintain provider price tables, or create a competing authoritative usage ledger.

When the control plane returns evidence, retain compact references such as:

```text
orchestrator task/run refs
routing-decision refs
approval/escalation refs
budget-envelope ref
usage-receipt refs
execution-cost status
provider/model bypass result
```

Keep coding-agent execution-resource cost separate from the `EXTERNAL CALL / COST` proof for provider/API calls made by the software under test.

## 10. Create the Test Area Map

Use [`../templates/TEST_AREA_MAP_TEMPLATE.md`](../templates/TEST_AREA_MAP_TEMPLATE.md).

Consider these universal areas:

- STRUCTURE;
- UNIT;
- CONTRACT;
- INTEGRATION;
- END_TO_END / ACCEPTANCE;
- DATA / MIGRATION;
- SECURITY / PRIVACY;
- RELIABILITY / RECOVERY;
- EXTERNAL CALL / COST;
- PERFORMANCE / RESOURCE;
- COMPATIBILITY;
- RELEASE / DEPLOYMENT.

Activate only applicable areas, but do not convert unknowns into N/A.

See [`TEST_AREAS.md`](TEST_AREAS.md).

## 11. Use a durable change workspace for material work

Recommended layout:

```text
.governance/changes/<CHANGE-ID>/
```

Use [`../templates/CHANGE_WORKSPACE_TEMPLATE.md`](../templates/CHANGE_WORKSPACE_TEMPLATE.md).

This gives interrupted sessions and multiple agents a durable source of truth for scope, evidence, open failures, audit state, and safe execution-control references.

Do not copy provider credentials, sensitive prompts, or duplicate billing transactions into the GCU workspace.

## 12. Adopt the Production Spine and contract map

For T3/T4 cross-boundary production work, use [`../templates/PRODUCTION_SPINE_TEMPLATE.md`](../templates/PRODUCTION_SPINE_TEMPLATE.md).

Trace the real path to its terminal outcome and map material handoffs as Producer → Contract → Consumer. Include tenant/account/security identity where it affects access.

T2 boundary work still requires the relevant Producer → Contract → Consumer mapping even if a full Production Spine is not needed.

## 13. Freeze acceptance before implementation

Use [`../templates/ACCEPTANCE_CONTRACT_TEMPLATE.md`](../templates/ACCEPTANCE_CONTRACT_TEMPLATE.md) whenever correctness depends on a real path or controlled dependency boundary.

Freeze real project modules, controlled seams, validators/contracts, positive/negative assertions, prohibited later effects, external-call ceiling, and exact command before implementation.

Run the false-PASS scan before accepting terminal green results.

## 14. Adopt Sequential Evidence Gates

For ordered work:

```text
inspect
→ define proof
→ reproduce failure when safe/feasible
→ implement
→ narrow verify
→ section audit
→ automatically continue on PASS
```

Do not proceed through a failed dependent section.

Do not auto-continue through a required model-route approval, execution budget approval, human-wait state, or other explicit authorization boundary.

## 15. Run the Challenger gate

For T2+ work, challenge the plan/proof before terminal acceptance.

Ask whether:

- a mock sits above the boundary being claimed;
- a negative path is missing;
- a downstream consumer is unproved;
- a compatibility/migration/auth/recovery condition was overlooked;
- the Project Adapter is stale;
- the test would still pass if the defect remained;
- routing/billing/orchestration authority is duplicated;
- a model/provider fallback could happen silently;
- audit independence is being confused with model capability.

Fix proof defects before terminal acceptance.

## 16. Adopt balanced verification

Use three levels:

1. narrow active test areas;
2. affected test areas only when a changed boundary can invalidate them;
3. one terminal verification after all sections and cross-section review pass.

## 17. Configure controlled external-call and durable-work proof

Where external services/models or asynchronous work exist in the software under test:

- inject deterministic controlled dependencies below real adapters/services;
- avoid unintended live execution where technically feasible;
- measure actual call/task counters;
- define retry/timeout/recovery/idempotency/cancellation obligations;
- prove restart from a fresh process when durable recovery is part of the claim.

This is separate from model usage consumed by coding agents, which belongs to the execution control plane when present.

## 18. Add terminal-path and system-readiness proof

For `STAGING_READY` or `PRODUCTION_READY`, define and prove the terminal user/business promise.

For `PRODUCTION_READY`, prove all applicable full-system responsibilities defined by the skill, including required execution-control-plane evidence when that integration is part of the governed environment.

A scoped PASS and system readiness must be reported separately.

## 19. Add the terminal machine release gate

Use [`../templates/MACHINE_RELEASE_GATE_TEMPLATE.md`](../templates/MACHINE_RELEASE_GATE_TEMPLATE.md).

Prefer one stable repository command such as:

```text
change:release-gate
```

The gate exits 0 only when all machine-enforceable mandatory conditions are satisfied at the exact candidate head.

Mandatory exact-head CI unavailable is `CODE VERIFIED / GOVERNANCE HOLD`, not final PASS.

A model route or model-generated recommendation cannot substitute for Release Authority.

## 20. Audit and correct

Use [`../templates/INDEPENDENT_AUDIT_TEMPLATE.md`](../templates/INDEPENDENT_AUDIT_TEMPLATE.md) against the exact final head.

If the audit is performed in the Builder's same context, record `SELF_AUDIT`. Do not claim independence.

A stronger model in the same context does not change that result.

If blocked, correct the owning checklist IDs/boundaries/test areas, rerun narrow and affected checks, rerun terminal verification, and audit the corrected head.

If a production or execution-control defect escaped earlier green proof, correct both the defect and the proof system that missed it.

## 21. Monorepo adoption

For a monorepo, the Project Adapter should define component roots and shared boundaries.

Per change:

- select affected components;
- select shared contract consumers;
- run narrow tests in affected components;
- run shared-boundary tests when invalidated;
- reserve unrelated expensive full-workspace verification for terminal checks unless governance requires otherwise.

## 22. Resume interrupted sessions

After interruption, reopen the same repository/branch, inspect HEAD/diff/change workspace/test evidence, identify the last directly proven section, preserve valid work, and continue from the first unproven/failing obligation.

When external task/run/routing/usage references exist, preserve them across resume rather than reconstructing them from agent memory.

## 23. Close with evidence

Use [`../templates/FINAL_REPORT_TEMPLATE.md`](../templates/FINAL_REPORT_TEMPLATE.md). Do not replace missing proof with confidence language.

When execution control is active, store the authoritative receipt references and final policy status; do not duplicate the provider's billing transaction.

## Repository-level acceptance

v2.2.0 adoption is complete when:

- the skill and global rule are installed;
- Project Discovery has been performed;
- a Project Adapter exists or the legacy profile is explicitly retained;
- material adapter facts are supported or `UNRESOLVED`;
- protected invariants are registered;
- Change Tier and Release Intent are declared per change;
- agent roles are assigned truthfully when used;
- Release Authority remains outside model execution;
- execution-control authorities and receipt methods are registered when an external control plane is present;
- capability/model-route escalation is provider-neutral at the GCU boundary;
- execution usage is referenced rather than duplicated;
- Test Area Map selection is evidence-based;
- production-spine/contract-map records are used when required;
- acceptance architecture is frozen before real-path implementation;
- false-PASS controls are active;
- challenge/proof-falsification is used for T2+ changes;
- controlled external-call/durable-work policy is defined where applicable;
- terminal verification and machine release gate are executable when required;
- exact-head audit can be performed;
- merge/release authorization remains explicit.