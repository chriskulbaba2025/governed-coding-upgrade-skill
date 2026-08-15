<p align="center">
  <img src="branding/logo.svg" alt="Governed Coding Upgrade" width="760">
</p>

<p align="center">
  <strong>Universal governance, testing, audit, and production-readiness for AI-assisted software changes.</strong><br>
  Project discovery. Project adapters. Optional agent roles. Capability-based test areas. Production spine. Proof-first acceptance. Exact-head audit.
</p>

<p align="center">
  <code>v2.2.0 — Universal Project Orchestration</code>
</p>

> **Official canonical repository.** Maintained and controlled by **Chris Kulbaba (@chriskulbaba2025)**. Public forks and derivatives are not official releases.

# Governed Coding Upgrade v2.2.0 — Universal Project Orchestration

Governed Coding Upgrade (GCU) is a project-agnostic execution skill for coding agents and engineering teams.

It is designed to run across project types without hard-coding a language, framework, CI provider, cloud, repository layout, agent runtime, model provider, or billing system.

The machine-facing skill name remains:

```text
governed-coding-upgrade
```

## What v2.2 changes

v2.1 established strong production-correctness controls: production-spine tracing, Producer → Contract → Consumer mapping, proof-first acceptance, sequential evidence, terminal-path verification, machine gating, and exact-head audit.

v2.2 makes that protocol easier to reuse across very different repositories by adding five universal layers:

1. **Project Discovery** — inspect the repository before planning instead of assuming the stack.
2. **Project Adapter** — map universal GCU capabilities to the repository's real commands, components, boundaries, CI, and release process.
3. **Agent Orchestration** — optional Scout, Planner, Builder, Challenger, Verifier, Auditor, and Release Authority roles.
4. **Execution Control Plane Integration** — request capability, budget, escalation, and usage evidence without turning GCU into a model router or billing authority.
5. **Test Area Map** — activate proof by capability rather than fixed folders or frameworks.

It also adds Change Tiers so a small library fix does not need the same operating weight as a cross-service production release.

## Universal operating model

```text
Universal GCU protocol
+ Project Discovery
+ Project Adapter
+ Change Tier + Release Intent
+ Agent Roster when useful
+ Execution Control Plane contract when present
+ Test Area Map
= governed execution for this repository
```

## Supported project types

The protocol can adapt to repositories containing one or more of:

- web applications;
- APIs and services;
- CLIs;
- libraries, packages, and SDKs;
- mobile and desktop applications;
- infrastructure / IaC;
- data pipelines / ETL;
- ML / AI systems;
- workers, queues, and background jobs;
- database/schema projects;
- plugins/extensions;
- static sites/documentation systems;
- monorepos and multi-service workspaces;
- embedded/edge systems;
- custom project types.

A project kind is descriptive, not restrictive. The Project Adapter supplies the concrete commands and boundaries.

## Change Tiers

- **T1_LOCAL** — contained local behavior.
- **T2_BOUNDARY** — public contract, schema, API, data-shape, auth, or component-boundary changes.
- **T3_SYSTEM** — cross-boundary, persistence, async, provider, security-sensitive, or end-to-end work.
- **T4_RELEASE** — staging/production readiness or protected release gates.

Change Tier controls governance depth.

Release Intent remains separate:

- `CHANGE_ONLY`
- `STAGING_READY`
- `PRODUCTION_READY`

## Optional agent roles

GCU defines responsibilities, not a required agent vendor.

- **Scout** — read-only discovery and adapter verification.
- **Planner** — scope, contracts, checklist, acceptance, and test map.
- **Builder** — governed implementation.
- **Challenger** — tries to break assumptions and proof.
- **Verifier** — runs active test areas and records evidence.
- **Auditor** — inspects the exact candidate head.
- **Release Authority** — owns protected merge/deploy/release authorization.

One agent may hold several roles for small work. Do not multiply agents without value.

If the Builder audits its own work, report `SELF_AUDIT`; do not call it independent.

See [`docs/AGENT_ORCHESTRATION.md`](docs/AGENT_ORCHESTRATION.md).

## Execution control plane integration

GCU governs the **change lifecycle**. It does not become the model gateway or billing ledger when it runs inside a larger agent platform.

The v2.2 execution-control contract separates responsibility cleanly:

```text
GCU
→ emits provider-neutral role/workload/capability context

Execution orchestrator
→ owns task/run state, approvals, escalation, and human-wait lifecycle

AI policy authority
→ owns model/provider resolution, credentials, cost ceilings, usage accounting, and policy audit

GCU evidence
← receives durable routing/approval/usage references
```

GCU must not silently switch provider/model, maintain provider credentials, or duplicate an authoritative usage ledger. A premium model used in the same Builder context also does not create an independent audit.

See [`docs/EXECUTION_CONTROL_PLANE_INTEGRATION.md`](docs/EXECUTION_CONTROL_PLANE_INTEGRATION.md).

## Universal test areas

The Project Adapter maps these logical proof lanes to real repository commands:

- STRUCTURE
- UNIT
- CONTRACT
- INTEGRATION
- END_TO_END / ACCEPTANCE
- DATA / MIGRATION
- SECURITY / PRIVACY
- RELIABILITY / RECOVERY
- EXTERNAL CALL / COST
- PERFORMANCE / RESOURCE
- COMPATIBILITY
- RELEASE / DEPLOYMENT

Only applicable areas are activated. `N/A` requires a reason. Unknown is `UNRESOLVED`, not N/A.

See [`docs/TEST_AREAS.md`](docs/TEST_AREAS.md).

## Governed lifecycle

```text
INTAKE
→ PREFLIGHT
→ PROJECT DISCOVERY / ADAPTER CHECK
→ CHANGE TIER + RELEASE INTENT
→ AGENT ROSTER when useful
→ EXECUTION CONTROL PLANE CHECK when present
→ PRODUCTION SPINE / CONTRACT MAP when applicable
→ ACCEPTANCE FREEZE
→ FROZEN CHECKLIST + TEST AREA MAP
→ SEQUENTIAL BUILD / VERIFY
→ CHALLENGE
→ TERMINAL-PATH / SYSTEM READINESS when applicable
→ MACHINE GATE
→ EXACT-HEAD AUDIT
→ CORRECTION / RE-AUDIT
→ CLOSE
```

## Core rule

> A coding change is not complete because an agent says it is complete. It is complete when governed requirements are directly proven at the exact candidate head, with proof depth matched to the changed boundaries and the readiness claim.

## Repository structure

| Path | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | Authoritative v2.2.0 execution skill |
| [`GLOBAL_CLAUDE_RULE.md`](GLOBAL_CLAUDE_RULE.md) | Mandatory invocation rule |
| [`docs/UNIVERSAL_PROJECT_MODEL.md`](docs/UNIVERSAL_PROJECT_MODEL.md) | Project discovery, adapter, tiers, monorepo rules |
| [`docs/AGENT_ORCHESTRATION.md`](docs/AGENT_ORCHESTRATION.md) | Role-based agent orchestration |
| [`docs/EXECUTION_CONTROL_PLANE_INTEGRATION.md`](docs/EXECUTION_CONTROL_PLANE_INTEGRATION.md) | Capability, escalation, cost, usage-receipt, and authority boundary contract |
| [`docs/TEST_AREAS.md`](docs/TEST_AREAS.md) | Universal capability-based test areas |
| [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | Control architecture |
| [`docs/ADOPTION_GUIDE.md`](docs/ADOPTION_GUIDE.md) | Adoption procedure |
| [`templates/PROJECT_ADAPTER_TEMPLATE.md`](templates/PROJECT_ADAPTER_TEMPLATE.md) | Universal repository adapter |
| [`templates/AGENT_ROSTER_TEMPLATE.md`](templates/AGENT_ROSTER_TEMPLATE.md) | Optional role assignment |
| [`templates/TEST_AREA_MAP_TEMPLATE.md`](templates/TEST_AREA_MAP_TEMPLATE.md) | Per-change test selection |
| [`templates/CHANGE_WORKSPACE_TEMPLATE.md`](templates/CHANGE_WORKSPACE_TEMPLATE.md) | Durable change-package layout |
| [`templates/PRODUCTION_SPINE_TEMPLATE.md`](templates/PRODUCTION_SPINE_TEMPLATE.md) | Production spine / handoff record |
| [`templates/ACCEPTANCE_CONTRACT_TEMPLATE.md`](templates/ACCEPTANCE_CONTRACT_TEMPLATE.md) | Proof-first acceptance freeze |
| [`scripts/validate-package.py`](scripts/validate-package.py) | Package integrity validator |
| [`.github/`](.github/) | Repository governance and CI |

## Installation

1. Install `SKILL.md` in the reusable skill location under `governed-coding-upgrade`.
2. Add `GLOBAL_CLAUDE_RULE.md` to the global coding-agent instruction layer.
3. Run Project Discovery in the target repository.
4. Create `.governance/PROJECT_ADAPTER.md` from the template.
5. Map real repository commands to applicable universal test areas.
6. For each change, declare Change Tier and Release Intent.
7. Use agent roles only when they improve separation or throughput.
8. If an execution control plane exists, register its authority boundaries and receipt methods in the Project Adapter.
9. Use the production-spine, acceptance, checklist, test-area, and audit controls required by the change.

See [`docs/ADOPTION_GUIDE.md`](docs/ADOPTION_GUIDE.md).

## Backward compatibility

Existing v2.1 repositories using `.governance/GOVERNED_CHANGE_PROFILE.md` remain valid.

They can:

- keep the existing profile;
- add a Project Adapter beside it;
- or migrate repository facts into the Project Adapter over time.

The machine-facing skill identifier does not change.

## Proof model

Strong proof includes exact assertions, lifecycle/state history, persisted round trips, artifacts/hashes, real modules with controlled dependencies, call/task counters, restart/recovery evidence, contract continuity, exact changed-file scope, exact final SHA, exact-head CI, machine-gate result, terminal retrieval, execution-policy receipts when applicable, and audit evidence.

Weak proof includes prose, confidence, test names, comments, fabricated success objects, hardcoded call counts, hardcoded cost claims, or green CI without showing what the CI proved.

## Versioning

Semantic versioning applies to the protocol artifact.

- **Protocol version:** `2.2.0`
- **Project Adapter schema:** `1.0.0`
- **Execution-control contract:** `gcu-execution-control/1.0.0`
- **Machine-facing name:** `governed-coding-upgrade`

Compatible installations keep the machine-facing identifier stable while protocol and adapter obligations may advance.

**Display name:** Governed Coding Upgrade v2.2.0 — Universal Project Orchestration  
**Canonical maintainer:** Chris Kulbaba (@chriskulbaba2025)  
**Copyright:** © 2026 Chris Kulbaba. All rights reserved.