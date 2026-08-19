# Adoption Guide

## Objective

Install Governed Coding Upgrade **v2.3.0 — Surgical Determinacy** so qualifying software changes use one evidence-based, LLM-agnostic governance lifecycle while each repository supplies its own implementation facts through a Project Adapter.

The adoption goal is not more process. It is a reliable separation of:

```text
what the user requested
what evidence says must change
what is authorized to change
what must remain protected
what proof is required
what the exact candidate head actually contains
```

## 1. Install the authoritative protocol

Make [`../SKILL.md`](../SKILL.md) available to the coding agent under the stable machine-facing name:

```text
governed-coding-upgrade
```

Treat `SKILL.md` as the governing protocol, not optional reference material.

The protocol is LLM-agnostic. Do not fork its governing semantics for individual model vendors.

## 2. Install the persistent invocation rule

Use [`../GLOBAL_AGENT_RULE.md`](../GLOBAL_AGENT_RULE.md) as the canonical vendor-neutral invocation rule.

Install an equivalent rule in the persistent instruction surface of the coding environment so qualifying changes invoke GCU **before editing**.

Agent-specific files are adapters:

- Claude Code: [`CLAUDE_CODE_QUICKSTART.md`](CLAUDE_CODE_QUICKSTART.md) and [`../GLOBAL_CLAUDE_RULE.md`](../GLOBAL_CLAUDE_RULE.md);
- ChatGPT Projects/custom GPTs: [`CHATGPT_AND_CUSTOM_GPT_USAGE.md`](CHATGPT_AND_CUSTOM_GPT_USAGE.md);
- other LLM/coding environments: [`LLM_AGNOSTIC_USAGE.md`](LLM_AGNOSTIC_USAGE.md).

An adapter may change how GCU is invoked. It does not change the protocol.

## 3. Run Project Discovery

Before planning a change or creating an adapter, inspect directly supported repository facts relevant to governed work:

- project kinds and component/workspace boundaries;
- languages, runtimes, build/package systems;
- test frameworks and commands;
- CI/release/rollback mechanisms;
- persistence, migrations, queues, and background work;
- external systems and controlled-test seams;
- security/privacy/tenant boundaries;
- execution orchestrator / AI policy authority when present;
- generated/protected paths;
- repository governance and authorization boundaries.

Unknown material facts are `UNRESOLVED`, not guessed.

See [`UNIVERSAL_PROJECT_MODEL.md`](UNIVERSAL_PROJECT_MODEL.md).

## 4. Create the Project Adapter

Preferred repository path:

```text
.governance/PROJECT_ADAPTER.md
```

Start from [`../templates/PROJECT_ADAPTER_TEMPLATE.md`](../templates/PROJECT_ADAPTER_TEMPLATE.md).

The Project Adapter maps universal GCU capabilities to the repository's actual commands, components, boundaries, CI, release process, persistence rules, security constraints, external-call policy, and stop conditions.

Existing repositories using `.governance/GOVERNED_CHANGE_PROFILE.md` remain compatible.

## 5. Establish protected invariants

Record behavior that may not change without explicit authorization, including applicable:

- API/schema/public contracts;
- authentication, authorization, tenant/account isolation;
- persistence and migration semantics;
- lifecycle transitions;
- golden/reference artifacts;
- generated output;
- dependency compatibility;
- external-call restrictions;
- deployment/rollback behavior;
- model-route and execution-policy authority.

These invariants become part of the protected surface for individual changes when relevant.

## 6. Preserve the requirement before implementation planning

For every governed change, record:

```text
Original requested outcome
Faithful governed interpretation
Explicit exclusions / non-goals
Observable acceptance condition
```

Do not let implementation ideas silently become requirements.

The governed interpretation must remain faithful to the requested outcome and implementation-independent.

## 7. Freeze the Surgical Change Contract

Before governed production edits, use [`../templates/SURGICAL_CHANGE_CONTRACT_TEMPLATE.md`](../templates/SURGICAL_CHANGE_CONTRACT_TEMPLATE.md) or an equivalent durable record.

Freeze:

```text
required outcome
direct evidence
change hypothesis + predicted effect
causal boundary
REQUIRED / EXPECTED / PROHIBITED change surface
protected surface
structural change budget
acceptance proof
scope-expansion conditions
```

The change hypothesis must be `PROVEN` before implementation if it contains a material causal fact. `UNRESOLVED` is a stop condition, not permission to guess.

### Structural change budget

Budget architectural surface, not lines of code. Applicable dimensions include production modules, contracts, schemas, persistence, dependencies, integrations, configuration, abstractions, migrations, and bounded test surfaces.

Do not impose arbitrary line-count, diff-size, or function-count limits as a definition of surgicality.

### Discovery does not create authorization

A newly discovered defect, cleanup, refactor, dependency issue, hardening opportunity, rename, reorganization, or adjacent feature stays outside the active change unless direct evidence proves it is causally required for the frozen outcome.

If implementation needs a new material boundary:

```text
STOP
→ preserve evidence
→ reopen the Surgical Change Determinacy Gate
→ prove causal necessity
→ update the contract/budget
→ continue only after PASS
```

See [`SURGICAL_CHANGE_DETERMINACY.md`](SURGICAL_CHANGE_DETERMINACY.md).

## 8. Classify Change Tier and Release Intent

Declare one Change Tier:

- `T1_LOCAL`
- `T2_BOUNDARY`
- `T3_SYSTEM`
- `T4_RELEASE`

Change Tier scales governance depth. The surgical causal rule applies at every tier.

Declare one Release Intent:

- `CHANGE_ONLY`
- `STAGING_READY`
- `PRODUCTION_READY`

Release Intent controls the readiness claim. A scoped PASS is not production readiness.

## 9. Assign agent roles only when useful

Available roles:

- Scout;
- Planner;
- Builder;
- Challenger;
- Verifier;
- Auditor;
- Release Authority.

Use [`../templates/AGENT_ROSTER_TEMPLATE.md`](../templates/AGENT_ROSTER_TEMPLATE.md) when a durable roster is useful.

One context may hold several roles for small changes. If Builder and Auditor share the same context, label the audit `SELF_AUDIT`.

**Release Authority is not an AI execution role.** It remains human/repository controlled and may not be model-dispatched.

See [`AGENT_ORCHESTRATION.md`](AGENT_ORCHESTRATION.md).

## 10. Register the Execution Control Plane when present

If the coding agent runs behind an execution orchestrator, model gateway, or AI policy platform, adopt [`EXECUTION_CONTROL_PLANE_INTEGRATION.md`](EXECUTION_CONTROL_PLANE_INTEGRATION.md).

Canonical contract:

```text
gcu-execution-control/1.0.0
```

GCU may request provider-neutral capability but does not choose concrete providers/models, hold provider credentials, silently escalate, maintain provider price tables, or duplicate the authoritative usage ledger.

Retain durable references such as task/run, routing-decision, approval/escalation, budget-envelope, and usage-receipt references when supplied.

Keep execution-resource cost separate from `EXTERNAL CALL / COST` evidence produced by the software under test.

## 11. Create the durable change workspace when warranted

Recommended layout:

```text
.governance/changes/<CHANGE-ID>/
  INTAKE.md
  DISCOVERY.md
  SURGICAL_CHANGE.md
  CHECKLIST.md
  AGENT_ROSTER.md
  TEST_AREA_MAP.md
  EVIDENCE.md
  AUDIT.md
  LEARNING.md when applicable
```

Use [`../templates/CHANGE_WORKSPACE_TEMPLATE.md`](../templates/CHANGE_WORKSPACE_TEMPLATE.md).

Small T1 changes may use a reduced record if repository governance permits it. Requirement Preservation and Surgical Determinacy still apply.

Do not copy secrets, provider credentials, sensitive prompts, or duplicate billing transactions into GCU evidence.

## 12. Build the FROZEN CHECKLIST and Test Area Map

Use:

- [`../templates/CHANGE_CHECKLIST_TEMPLATE.md`](../templates/CHANGE_CHECKLIST_TEMPLATE.md);
- [`../templates/TEST_AREA_MAP_TEMPLATE.md`](../templates/TEST_AREA_MAP_TEMPLATE.md).

Universal Test Areas are:

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

Activate only applicable areas. A missing command or unknown fact is not automatically N/A.

## 13. Map the Production Spine and contracts when applicable

For T3/T4 cross-boundary production work, use [`../templates/PRODUCTION_SPINE_TEMPLATE.md`](../templates/PRODUCTION_SPINE_TEMPLATE.md).

Trace the real path to the terminal outcome and map material `Producer → Contract → Consumer` handoffs, including identity/security continuity where relevant.

T2 boundary work still requires the applicable contract/handoff proof even when a full Production Spine is unnecessary.

## 14. Freeze acceptance before implementation

Use [`../templates/ACCEPTANCE_CONTRACT_TEMPLATE.md`](../templates/ACCEPTANCE_CONTRACT_TEMPLATE.md) when correctness depends on a real path or controlled dependency boundary.

Freeze real project modules, controlled seams, validators/contracts, positive and negative assertions, prohibited later effects, external-call ceiling, and exact verification command.

Reject false-PASS proof such as fabricated success, always-valid validators, bypassed real modules, pre-seeded terminal state, hardcoded call counts, or mocks above the production boundary being claimed.

## 15. Execute with Sequential Evidence Gates

For ordered work:

```text
inspect
→ define proof
→ reproduce failure when safe/feasible
→ implement complete bounded section
→ narrow verify
→ section audit
→ continue only on PASS
```

Do not auto-continue through:

- a failed dependent section;
- a determinacy reopen;
- an explicit human authorization boundary;
- route/budget approval;
- a denied execution-control decision.

## 16. Run the Causal Necessity Audit

After implementation, map every material changed production boundary:

```text
Requirement ID
→ changed boundary
→ why the requirement remains incorrect if unchanged
→ direct evidence
```

If a material changed boundary cannot be justified, remove it or govern it as a separately authorized change.

Use selective revert testing only where necessity remains disputed or insufficiently evidenced.

## 17. Run the Challenger and terminal checks

For T2+ work, Challenger review should attack:

- requirement drift;
- causal hypothesis;
- causal boundary breadth;
- structural-budget expansion;
- incidental-work adoption;
- false-PASS risks;
- missing consumers, compatibility, migration, auth, recovery, or negative paths;
- audit-independence claims.

Then run affected cross-section verification and, for `STAGING_READY` / `PRODUCTION_READY`, prove the same governed execution reaches the terminal user/business result.

For `PRODUCTION_READY`, complete all applicable full-system readiness obligations.

## 18. Machine gate and exact-head audit

Do not call the change release-ready from agent prose.

Where required, the exact candidate head must satisfy repository machine gates and exact-head CI.

Use [`../templates/INDEPENDENT_AUDIT_TEMPLATE.md`](../templates/INDEPENDENT_AUDIT_TEMPLATE.md).

The exact-head audit must inspect the actual diff and include the Surgical Determinacy Audit:

```text
Requirement preserved: PASS
Change hypothesis validated: PASS
Required outcome achieved: PASS
Material changed boundaries causally justified: PASS
Protected surfaces preserved: PASS
Structural change budget respected or formally reopened: PASS
Incidental findings excluded unless causally authorized: PASS
Unauthorized scope expansion: ZERO
Unjustified architectural change: ZERO
Unjustified contract change: ZERO
Unjustified dependency change: ZERO
```

If controlled code verification passes but mandatory external release evidence is unavailable, report:

```text
CODE VERIFIED / GOVERNANCE HOLD
```

## 19. Governed learning when available

When `gcu-learning-memory/1.0.0` is active, recalled approved practices remain `ADVISORY_ONLY` and cannot override current user instruction, repository authority, or current evidence.

A producing run may emit evidence-linked lesson candidates after a truthful terminal state but must not auto-promote its own lesson into an approved practice.

See [`GOVERNED_LEARNING_LOOP.md`](GOVERNED_LEARNING_LOOP.md).

## 20. Release-state rule

Keep these distinct:

```text
CHANGE RESULT
SURGICAL DETERMINACY
SYSTEM READINESS
AUDIT STATE
RELEASE AUTHORIZATION
```

Do not merge, deploy, release, activate, spend against prohibited live providers, change routing policy, or bypass a required approval because code tests are green.

## Minimum adoption standard

A repository has a credible GCU v2.3 adoption when it has:

1. authoritative `SKILL.md` available to the coding environment;
2. a persistent invocation rule equivalent to `GLOBAL_AGENT_RULE.md`;
3. a verified Project Adapter or compatible governed profile;
4. Requirement Preservation and Surgical Change Determinacy before edits;
5. a structural change budget and fail-closed expansion behavior;
6. applicable Test Area / real-path proof;
7. Causal Necessity Audit after implementation;
8. exact-head Surgical Determinacy Audit before governed completion;
9. truthful separation of code verification, system readiness, audit independence, and release authority.
