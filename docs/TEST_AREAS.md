# Universal Test Areas

Governed Coding Upgrade uses **test areas** instead of assuming one framework or directory layout.

A test area is a class of proof. The Project Adapter maps each active area to the repository's real commands and evidence.

Not every area applies to every change. `N/A` must be justified; `UNRESOLVED` is not the same as N/A.

## Core test areas

### A. STRUCTURE

Purpose: prove the codebase remains structurally valid.

Examples:

- formatting policy;
- lint/static analysis;
- type checking;
- compilation/build;
- generated artifact consistency;
- manifest/lockfile consistency.

Typical activation: almost all code changes where such tools exist.

### B. UNIT

Purpose: prove local deterministic behavior at the smallest meaningful boundary.

Typical activation: changed business logic, utilities, components, functions, classes, modules.

### C. CONTRACT

Purpose: prove producer/consumer interfaces and data shapes.

Examples:

- API request/response schemas;
- serialization;
- event payloads;
- library public APIs;
- database record shapes;
- plugin interfaces;
- component props/contracts.

Typical activation: T2+ boundary changes.

### D. INTEGRATION

Purpose: prove two or more real project components work together through their actual boundary.

Examples:

- service + persistence;
- API + domain layer;
- package + consuming package;
- job + queue adapter;
- UI + application API;
- IaC module composition.

### E. END_TO_END / ACCEPTANCE

Purpose: prove the requested user/business outcome through the real production path with controlled dependencies where required.

Typical activation: T3 SYSTEM, T4 RELEASE, or any change whose correctness cannot be established at a lower boundary.

### F. DATA / MIGRATION

Purpose: prove data compatibility and state transition safety.

Examples:

- schema migrations;
- backfills;
- data transformations;
- file format changes;
- state-machine migrations;
- rollback/forward compatibility.

### G. SECURITY / PRIVACY

Purpose: prove security, access, tenant, secret, and privacy invariants affected by the change.

Examples:

- authorization;
- cross-account/tenant denial;
- authentication/session behavior;
- secret exposure;
- unsafe input handling;
- data minimization;
- dependency/security scanning.

### H. RELIABILITY / RECOVERY

Purpose: prove failure handling and recoverability.

Examples:

- retries;
- idempotency;
- restart/resume;
- cancellation;
- timeout;
- partial failure;
- duplicate work prevention;
- crash recovery.

### I. EXTERNAL CALL / COST

Purpose: prove controlled use of paid, remote, rate-limited, or side-effecting systems.

Examples:

- provider/model/API calls;
- webhook delivery;
- cloud task creation;
- payment or notification side effects;
- call/task/cost ceilings;
- reuse after retry.

Unexpected live execution should fail the controlled test where technically feasible.

### J. PERFORMANCE / RESOURCE

Purpose: prove material latency, throughput, memory, CPU, storage, bundle size, query count, or cost constraints.

Activate only when the change or governing contract makes performance/resources material.

### K. COMPATIBILITY

Purpose: prove supported consumers/environments remain valid.

Examples:

- runtime versions;
- browsers/devices;
- API versions;
- package consumers;
- database versions;
- backwards/forwards compatibility;
- platform-specific behavior.

### L. RELEASE / DEPLOYMENT

Purpose: prove repository-owned release mechanics and the exact candidate head.

Examples:

- exact-head CI;
- packaging;
- artifact signing/hash;
- infrastructure plan/apply validation;
- deployment preview/staging proof;
- machine release gate;
- rollback readiness.

Typical activation: T4 RELEASE and repository-defined release gates.

## Test Area Map

Preferred per-change path:

```text
.governance/changes/<CHANGE-ID>_TEST_AREA_MAP.md
```

For each area record:

| Area | Active? | Why | Command/mechanism | Scope | Positive proof | Negative proof | Evidence |
|---|---|---|---|---|---|---|---|

Rules:

- `Active = NO` requires a reason;
- missing repository capability is `UNRESOLVED`, not automatically N/A;
- the Project Adapter supplies stable commands when available;
- per-change commands may narrow an adapter command but may not silently weaken a mandatory repository gate;
- expensive areas run according to balanced verification, not after every local edit.

## Activation by Change Tier

These are defaults, not substitutes for repository facts.

### T1 LOCAL

Usually consider:

- STRUCTURE;
- UNIT;
- affected COMPATIBILITY when relevant.

### T2 BOUNDARY

Add consideration of:

- CONTRACT;
- INTEGRATION;
- SECURITY/PRIVACY when the boundary carries identity or sensitive data;
- COMPATIBILITY.

### T3 SYSTEM

Add consideration of:

- END_TO_END / ACCEPTANCE;
- DATA/MIGRATION;
- RELIABILITY/RECOVERY;
- EXTERNAL CALL/COST;
- PERFORMANCE/RESOURCE when material.

### T4 RELEASE

Add:

- RELEASE/DEPLOYMENT;
- all repository-mandatory terminal areas;
- exact-head evidence required by governance.

## Test-area isolation

Test areas are logical proof lanes, not necessarily separate folders.

A repository may use:

```text
tests/unit/
tests/contracts/
tests/integration/
tests/e2e/
```

or one framework with tags, projects, markers, targets, workspaces, or scripts. GCU does not require a filesystem layout.

## Evidence rule

A green command is evidence only for the behavior it actually proves.

Do not infer:

- contract correctness from unit tests alone;
- persistence correctness from an in-memory double;
- production readiness from a build;
- terminal delivery from an intermediate state;
- security isolation from a happy path;
- external-call ceilings from hardcoded claims.
