# Adoption Guide

## Objective

Install Governed Coding Upgrade v2.1.0 so qualifying coding changes use the same production-correctness and sequential-governance lifecycle while each repository retains its own commands, invariants, CI, and release controls.

## 1. Install the skill

Place `SKILL.md` in the coding agent's reusable skill location under:

```text
governed-coding-upgrade
```

Load it as an authoritative execution skill, not optional reference material.

## 2. Install the global invocation rule

Add `GLOBAL_CLAUDE_RULE.md` to the global coding-agent instruction layer.

## 3. Create or upgrade the repository profile

Create/update:

```text
.governance/GOVERNED_CHANGE_PROFILE.md
```

Use [`../templates/GOVERNED_CHANGE_PROFILE_TEMPLATE.md`](../templates/GOVERNED_CHANGE_PROFILE_TEMPLATE.md).

For v2.1.0 explicitly populate:

- release-intent policy;
- narrow and affected-integration commands;
- acceptance and full-regression commands;
- production-spine record path;
- Producer → Contract → Consumer map path;
- acceptance-contract/freeze path;
- false-PASS scan method;
- terminal user/business promise definition;
- full-system production-readiness method;
- persistence/recovery policy;
- external-call/controlled-test policy;
- terminal machine release-gate command;
- exact-head CI verification method;
- merge/release authorization rule;
- rollback mechanism.

Unknown material fields are `UNRESOLVED`, not guessed.

## 4. Establish protected invariants

Record behaviors/artifacts that may not change without explicit authorization, including applicable API/schema contracts, data/access isolation, lifecycle transitions, authentication/authorization, migrations, golden/reference artifacts, generated output, dependency compatibility, external-call restrictions, deployment, and rollback.

## 5. Adopt release intent

Every governed change declares:

- `CHANGE_ONLY`;
- `STAGING_READY`; or
- `PRODUCTION_READY`.

Do not let a green scoped change imply a higher readiness state than it proved.

## 6. Adopt the Production Spine and contract map

For cross-boundary production work, use [`../templates/PRODUCTION_SPINE_TEMPLATE.md`](../templates/PRODUCTION_SPINE_TEMPLATE.md).

Trace the real path to its terminal outcome and map material handoffs as Producer → Contract → Consumer. Include tenant/account/security identity where it affects access.

## 7. Freeze acceptance before implementation

Use [`../templates/ACCEPTANCE_CONTRACT_TEMPLATE.md`](../templates/ACCEPTANCE_CONTRACT_TEMPLATE.md).

Freeze real production modules, controlled seams, validators/contracts, positive/negative assertions, prohibited later effects, external-call ceiling, and exact command before production implementation.

Run the false-PASS scan before accepting terminal green results.

## 8. Adopt Sequential Evidence Gates

For ordered multi-section work:

```text
inspect
→ define proof
→ reproduce failure when safe/feasible
→ implement
→ narrow verify
→ section audit
→ automatically continue on PASS
```

Do not proceed through a failed section. Routine PASS does not require user approval unless the next action crosses an explicit authorization boundary.

## 9. Adopt balanced verification

Use three levels:

1. narrow section proof;
2. affected integration proof only when a changed boundary can invalidate earlier behavior;
3. one terminal full verification after all sections and cross-section review pass.

## 10. Configure controlled external-call and durable-work proof

Where external services/models or asynchronous work exist:

- inject deterministic controlled dependencies below real production adapters/services;
- avoid unintended live execution where technically feasible;
- measure actual call/task counters;
- define retry/timeout/recovery/idempotency/cancellation obligations;
- prove restart from a fresh process when durable recovery is part of the production claim.

## 11. Add terminal-path and system-readiness proof

For `STAGING_READY` or `PRODUCTION_READY`, define and prove the terminal user/business promise. For `PRODUCTION_READY`, prove all applicable full-system responsibilities defined by the skill.

A scoped PASS and system readiness must be reported separately.

## 12. Add the terminal machine release gate

Use [`../templates/MACHINE_RELEASE_GATE_TEMPLATE.md`](../templates/MACHINE_RELEASE_GATE_TEMPLATE.md).

Prefer one stable repository command such as:

```text
change:release-gate
```

The gate exits 0 only when all machine-enforceable mandatory conditions are satisfied at the exact candidate head.

Mandatory exact-head CI unavailable is `CODE VERIFIED / GOVERNANCE HOLD`, not final PASS.

## 13. Audit and correct

Use [`../templates/INDEPENDENT_AUDIT_TEMPLATE.md`](../templates/INDEPENDENT_AUDIT_TEMPLATE.md) against the exact final head.

If blocked, correct the owning checklist IDs/boundaries, rerun narrow and affected checks, rerun terminal verification, and audit the corrected exact head.

If a production defect escaped earlier green proof, correct both the defect and the proof system that missed it.

## 14. Resume interrupted sessions

After interruption, reopen the same repository/branch, inspect HEAD/diff/checklist/test evidence, identify the last directly proven section, preserve valid work, and continue from the first unproven/failing section.

## 15. Close with evidence

Use [`../templates/FINAL_REPORT_TEMPLATE.md`](../templates/FINAL_REPORT_TEMPLATE.md). Do not replace missing proof with confidence language.

## Repository-level acceptance

v2.1.0 adoption is complete when:

- the skill and global rule are installed;
- the profile contains no material guessed facts;
- protected invariants are registered;
- release intent is declared per change;
- production-spine/contract-map records are used for cross-boundary production work;
- acceptance architecture is frozen before implementation;
- false-PASS controls are active;
- sequential and affected-integration checks map to executable commands;
- terminal-path and system-readiness claims are distinguishable from scoped PASS;
- controlled external-call/durable-work policy is defined where applicable;
- full terminal verification and machine release gate are executable;
- exact-head audit can be performed;
- merge/release authorization remains explicit.
