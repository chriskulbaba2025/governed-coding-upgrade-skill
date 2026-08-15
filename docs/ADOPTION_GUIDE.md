# Adoption Guide

## Objective

Install Governed Coding Upgrade v2.2.0 so qualifying coding changes use one universal governance lifecycle while each repository supplies its own facts through a Project Adapter.

The goal is portability without weakening proof.

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

Record behaviors/artifacts that may not change without explicit authorization, including applicable API/schema contracts, data/access isolation, lifecycle transitions, authentication/authorization, migrations, golden/reference artifacts, generated output, dependency compatibility, external-call restrictions, deployment, and rollback.

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

Available roles:

- Scout;
- Planner;
- Builder;
- Challenger;
- Verifier;
- Auditor;
- Release Authority.

A small T1 change may use one agent for several roles. A higher-risk T3/T4 change should use stronger separation when practical or required.

If the Builder audits its own work, label it `SELF_AUDIT`.

See [`AGENT_ORCHESTRATION.md`](AGENT_ORCHESTRATION.md).

## 9. Create the Test Area Map

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

## 10. Use a durable change workspace for material work

Recommended layout:

```text
.governance/changes/<CHANGE-ID>/
```

Use [`../templates/CHANGE_WORKSPACE_TEMPLATE.md`](../templates/CHANGE_WORKSPACE_TEMPLATE.md).

This gives interrupted sessions and multiple agents a durable source of truth for scope, evidence, open failures, and audit state.

## 11. Adopt the Production Spine and contract map

For T3/T4 cross-boundary production work, use [`../templates/PRODUCTION_SPINE_TEMPLATE.md`](../templates/PRODUCTION_SPINE_TEMPLATE.md).

Trace the real path to its terminal outcome and map material handoffs as Producer → Contract → Consumer. Include tenant/account/security identity where it affects access.

T2 boundary work still requires the relevant Producer → Contract → Consumer mapping even if a full Production Spine is not needed.

## 12. Freeze acceptance before implementation

Use [`../templates/ACCEPTANCE_CONTRACT_TEMPLATE.md`](../templates/ACCEPTANCE_CONTRACT_TEMPLATE.md) whenever correctness depends on a real path or controlled dependency boundary.

Freeze real project modules, controlled seams, validators/contracts, positive/negative assertions, prohibited later effects, external-call ceiling, and exact command before implementation.

Run the false-PASS scan before accepting terminal green results.

## 13. Adopt Sequential Evidence Gates

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

## 14. Run the Challenger gate

For T2+ work, challenge the plan/proof before terminal acceptance.

Ask whether:

- a mock sits above the boundary being claimed;
- a negative path is missing;
- a downstream consumer is unproved;
- a compatibility/migration/auth/recovery condition was overlooked;
- the Project Adapter is stale;
- the test would still pass if the defect remained.

Fix proof defects before terminal acceptance.

## 15. Adopt balanced verification

Use three levels:

1. narrow active test areas;
2. affected test areas only when a changed boundary can invalidate them;
3. one terminal verification after all sections and cross-section review pass.

## 16. Configure controlled external-call and durable-work proof

Where external services/models or asynchronous work exist:

- inject deterministic controlled dependencies below real adapters/services;
- avoid unintended live execution where technically feasible;
- measure actual call/task counters;
- define retry/timeout/recovery/idempotency/cancellation obligations;
- prove restart from a fresh process when durable recovery is part of the claim.

## 17. Add terminal-path and system-readiness proof

For `STAGING_READY` or `PRODUCTION_READY`, define and prove the terminal user/business promise.

For `PRODUCTION_READY`, prove all applicable full-system responsibilities defined by the skill.

A scoped PASS and system readiness must be reported separately.

## 18. Add the terminal machine release gate

Use [`../templates/MACHINE_RELEASE_GATE_TEMPLATE.md`](../templates/MACHINE_RELEASE_GATE_TEMPLATE.md).

Prefer one stable repository command such as:

```text
change:release-gate
```

The gate exits 0 only when all machine-enforceable mandatory conditions are satisfied at the exact candidate head.

Mandatory exact-head CI unavailable is `CODE VERIFIED / GOVERNANCE HOLD`, not final PASS.

## 19. Audit and correct

Use [`../templates/INDEPENDENT_AUDIT_TEMPLATE.md`](../templates/INDEPENDENT_AUDIT_TEMPLATE.md) against the exact final head.

If the audit is performed in the Builder's same context, record `SELF_AUDIT`. Do not claim independence.

If blocked, correct the owning checklist IDs/boundaries/test areas, rerun narrow and affected checks, rerun terminal verification, and audit the corrected head.

If a production defect escaped earlier green proof, correct both the defect and the proof system that missed it.

## 20. Monorepo adoption

For a monorepo, the Project Adapter should define component roots and shared boundaries.

Per change:

- select affected components;
- select shared contract consumers;
- run narrow tests in affected components;
- run shared-boundary tests when invalidated;
- reserve unrelated expensive full-workspace verification for terminal checks unless governance requires otherwise.

## 21. Resume interrupted sessions

After interruption, reopen the same repository/branch, inspect HEAD/diff/change workspace/test evidence, identify the last directly proven section, preserve valid work, and continue from the first unproven/failing obligation.

## 22. Close with evidence

Use [`../templates/FINAL_REPORT_TEMPLATE.md`](../templates/FINAL_REPORT_TEMPLATE.md). Do not replace missing proof with confidence language.

## Repository-level acceptance

v2.2.0 adoption is complete when:

- the skill and global rule are installed;
- Project Discovery has been performed;
- a Project Adapter exists or the legacy profile is explicitly retained;
- material adapter facts are supported or `UNRESOLVED`;
- protected invariants are registered;
- Change Tier and Release Intent are declared per change;
- agent roles are assigned truthfully when used;
- Test Area Map selection is evidence-based;
- production-spine/contract-map records are used when required;
- acceptance architecture is frozen before real-path implementation;
- false-PASS controls are active;
- challenge/proof-falsification is used for T2+ changes;
- controlled external-call/durable-work policy is defined where applicable;
- terminal verification and machine release gate are executable when required;
- exact-head audit can be performed;
- merge/release authorization remains explicit.
