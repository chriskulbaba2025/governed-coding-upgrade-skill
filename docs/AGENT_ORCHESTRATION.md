# Agent Orchestration

Governed Coding Upgrade defines **roles**, not a required agent vendor or runtime.

The same protocol can run with one coding agent, several specialized agents, a human/agent team, or an automated agent framework.

## Core rule

> Separate responsibilities when that improves proof. Do not create agents merely to create more activity.

Roles are capability boundaries. One agent may perform several roles on a small change. A role can also be assigned to a human.

## Standard roles

### 1. Scout

Purpose: establish repository facts before planning.

Default authority: read-only.

Produces:

- repository and component map;
- governing-source list;
- Project Adapter updates or `UNRESOLVED` items;
- likely Change Tier;
- affected boundaries;
- candidate test areas;
- risk/unknown list.

The Scout does not implement the change.

### 2. Planner

Purpose: turn the request and discovered repository facts into a governed change package.

Produces:

- release intent;
- Change Tier;
- permitted/prohibited scope;
- protected invariants;
- ordered checklist;
- Production Spine/contract map when applicable;
- acceptance freeze;
- Test Area Map;
- exact stop/authorization boundaries.

The Planner may not claim proof that has not been run.

### 3. Builder

Purpose: implement one governed section at a time.

Rules:

- edits only permitted scope;
- preserves pre-existing valid work;
- follows the frozen checklist;
- does not silently widen requirements;
- stops on a failed section or authorization boundary;
- records direct implementation evidence.

### 4. Challenger

Purpose: try to falsify the plan, implementation assumptions, and proof system before final acceptance.

Questions include:

- What assumption could make this PASS false?
- What production boundary is mocked above the point under proof?
- What negative path is missing?
- What stale adapter fact could invalidate the plan?
- What compatibility, migration, auth, tenant, external-call, recovery, or terminal-path condition was overlooked?
- What later consumer can still break even if the producer test is green?

The Challenger proposes failures to test; it does not override direct evidence.

### 5. Verifier

Purpose: execute the active Test Area Map and collect evidence.

Rules:

- uses repository commands from the Project Adapter;
- starts narrow, then affected, then terminal;
- measures calls/writes/tasks where required;
- distinguishes N/A from untested;
- reports exact commands and outcomes;
- never converts a failed test into a prose PASS.

### 6. Auditor

Purpose: inspect the exact candidate head independently of the Builder's completion claim.

Checks:

- exact SHA and diff;
- scope/invariants;
- checklist evidence;
- active test areas;
- Production Spine/contract map when applicable;
- false-PASS risk;
- terminal path/system readiness for the declared intent;
- machine gate and exact-head CI when required;
- truthful release/authorization state.

When practical, use a separate agent/context from the Builder. If the same agent performs the audit, label it `SELF_AUDIT`; do not call it independent.

### 7. Release Authority

Purpose: provide the human or repository-controlled authorization needed to merge, deploy, release, activate, or perform other protected operations.

A coding agent does not gain Release Authority from green tests.

## Recommended orchestration

```text
Scout
→ Planner
→ Builder (section)
→ Verifier (section)
→ repeat Builder/Verifier
→ Challenger
→ Terminal Verifier
→ Auditor
→ Release Authority when required
```

The Challenger may also run earlier for high-risk acceptance designs.

## Small-change mode

For T1 LOCAL work, one agent may perform:

```text
Scout + Planner + Builder + Verifier + SELF_AUDIT
```

provided the final report is truthful about the lack of independent separation.

Do not force a seven-agent process onto a one-line local correction.

## High-risk mode

For T3 SYSTEM or T4 RELEASE work, prefer separate contexts for:

- planning/challenge;
- implementation;
- terminal verification;
- exact-head audit.

Repository governance may require stronger separation.

## Handoff contract

Every role handoff should contain only evidence-backed state needed by the next role:

- change ID;
- repository/branch/current SHA;
- Project Adapter version/verified SHA;
- Change Tier and Release Intent;
- permitted/prohibited scope;
- active checklist IDs;
- active test areas;
- direct evidence already obtained;
- unresolved items;
- next authorization boundary.

Do not hand off hidden chain-of-thought. Hand off decisions, facts, evidence, and open questions.

## Parallel-agent rule

Parallel work is allowed only when sections are genuinely independent and do not edit overlapping governed boundaries.

Before parallel execution, define:

- file/boundary ownership;
- shared contracts;
- merge order;
- integration test owner;
- conflict behavior.

Cross-boundary or dependent sections remain sequential.

## Agent failure / interruption

If any role is interrupted:

1. recover repository state;
2. inspect HEAD, diff, checklist, and evidence files;
3. identify the last directly proven state;
4. preserve valid work;
5. resume from the first unproven or failing obligation.

Agent memory is not the source of truth. Repository state and recorded evidence are.
