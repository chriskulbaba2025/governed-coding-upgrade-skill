# Universal Project Model

Governed Coding Upgrade must adapt to the repository. The repository must not be forced to resemble a specific stack.

## Core model

```text
Universal GCU protocol
+ Project Discovery
+ Project Adapter
+ Change Tier + Release Intent
+ Agent Roster
+ Test Area Map
= Governed execution for the current repository
```

The universal protocol owns governance rules. The Project Adapter owns repository facts.

## 1. Project Discovery

Before creating or changing a Project Adapter, inspect the repository and record only directly supported facts.

Discover, when present:

- repository/monorepo/workspace boundaries;
- languages and runtimes;
- package/build systems;
- applications, services, libraries, packages, infrastructure, jobs, scripts, and data pipelines;
- entry points and public interfaces;
- test frameworks and existing test locations;
- CI/CD and release automation;
- schemas, migrations, persistence, caches, queues, object stores, and generated artifacts;
- authentication, authorization, tenant/account boundaries, and secrets handling;
- external providers, paid APIs, models, webhooks, and background jobs;
- deployment targets and rollback/recovery mechanisms;
- repository governance, protected files, and explicit user constraints.

Unknown material facts remain `UNRESOLVED`. Discovery does not guess missing commands or invent architecture.

## 2. Project Adapter

Preferred path:

```text
.governance/PROJECT_ADAPTER.md
```

The adapter maps the universal protocol to the repository. It may describe one repository or multiple components in a monorepo.

It records:

- project/component identity;
- project kind;
- roots and boundaries;
- build/runtime commands;
- test commands by area;
- generated/protected paths;
- persistence/migration policy;
- external-call policy;
- CI/release methods;
- terminal promises when applicable;
- rollback/recovery methods;
- project-specific stop conditions.

The adapter is evidence-backed configuration, not an architectural wish list.

## 3. Supported project kinds

Project kinds are descriptive, not restrictive. A repository can declare several.

Examples:

- web application;
- API/service;
- CLI;
- library/package/SDK;
- mobile/desktop application;
- infrastructure/IaC;
- data pipeline/ETL;
- ML/AI system;
- background worker/job system;
- database/schema repository;
- documentation/static site;
- monorepo/multi-service workspace;
- plugin/extension;
- embedded/edge system;
- other/custom.

A new project kind does not require a new GCU skill version unless it needs a new universal governance capability.

## 4. Change Tier

Change Tier controls governance depth. Release Intent controls the readiness claim. They are separate.

### T1 — LOCAL

Use for a contained change that does not alter a governed external or persistent boundary.

Minimum proof:

- preflight;
- scope/invariants;
- narrow test/static proof;
- affected checks when applicable;
- diff review;
- final evidence.

### T2 — BOUNDARY

Use when a contract, public API, schema, dependency boundary, data shape, auth rule, or component handoff changes.

Adds:

- Producer → Contract → Consumer mapping;
- positive and negative contract proof;
- compatibility analysis where applicable.

### T3 — SYSTEM

Use for cross-boundary, persistence, asynchronous, external-provider, multi-component, security-sensitive, or end-to-end behavior.

Adds when applicable:

- Production Spine;
- acceptance freeze;
- recovery/idempotency/external-call proof;
- terminal-path proof;
- broader integration/e2e test areas.

### T4 — RELEASE

Use when the requested result includes staging or production readiness.

Adds:

- full release-intent obligations;
- exact-head CI;
- machine release gate;
- independent audit;
- deployment/rollback/readiness evidence required by repository governance.

A simple change may still use T4 if a production-ready claim is requested. A complex change may remain CHANGE_ONLY if production readiness is not claimed.

## 5. Monorepo and multi-component rules

The Project Adapter may contain component records.

For each change:

1. identify affected components;
2. identify affected shared contracts;
3. select tests from affected components plus shared boundaries;
4. avoid unrelated full-repo verification until terminal verification unless repository governance requires it;
5. prove cross-component handoffs when the change crosses component boundaries.

## 6. Adapter lifecycle

The adapter should be re-verified when material repository facts change, including:

- build system;
- runtime;
- CI provider;
- test framework;
- deployment model;
- persistence or migration model;
- security/tenant boundary;
- workspace structure;
- external provider model;
- release gate.

Record the last verified SHA. Do not silently reuse stale material facts.

## 7. Portability rule

GCU must express requirements as capabilities and proof obligations, not vendor commands.

Examples:

- say `type/static verification`, not `npm run typecheck`;
- say `controlled external dependency`, not one provider-specific mock library;
- say `exact-head CI`, not one CI vendor;
- say `terminal retrieval/outcome`, not one web framework route.

The Project Adapter supplies the concrete command or mechanism.
