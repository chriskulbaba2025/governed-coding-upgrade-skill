# Governed State Capsule

**Contract:** `gcu-state-capsule/1.0.0`  
**Purpose:** compact resumable working-state index for Governed Coding Upgrade  
**Authority:** derived index only — repository truth and governed evidence remain authoritative

## Problem

GCU already preserves repository evidence, exact-head state, surgical scope, checklists, and governed learning. Those controls prevent unsafe drift, but a fresh or interrupted coding context can still waste tokens by re-reading broad history and re-deriving decisions that were already proven.

The Governed State Capsule solves that problem without storing conversation or creating a second evidence ledger.

```text
repository truth + governed artifacts
            ↓
       STATE.json
            ↓
minimal context manifest
            ↓
next governed obligation
```

The capsule persists **where the change is, what is already proven, what remains unresolved, and what context is required next**.

## Canonical location

For material or interruptible work:

```text
.governance/changes/<CHANGE-ID>/STATE.json
```

Use `templates/GOVERNED_STATE_CAPSULE_TEMPLATE.json` and validate against `schemas/governed_state_capsule.schema.json`.

Small T1 changes may omit the capsule when repository governance permits and the work is not expected to span contexts or interruptions.

## Authority rule

`STATE.json` is a resumability index, not a new source of truth.

Authority remains:

```text
current user authorization
→ repository state / exact HEAD / current diff
→ repository contracts and governance
→ frozen GCU artifacts and direct evidence
→ STATE.json
→ agent/session memory
```

If the capsule conflicts with repository state or direct evidence, the capsule is stale. Repair it before using it to continue.

## Required state

The capsule records only compact execution state and durable references:

- contract version;
- change ID;
- repository and branch;
- starting and current SHA;
- Change Tier and Release Intent;
- current phase and execution state;
- last proven obligation;
- next obligation;
- active files/boundaries;
- protected boundaries;
- unresolved material items;
- decision references;
- valid proof references;
- invalidated proof references;
- next authorization boundary;
- context manifest;
- updated timestamp.

It MUST NOT copy full evidence, prompts, transcripts, model reasoning, provider credentials, secret values, or authoritative billing transactions.

## Resume-first rule

On a fresh context, role handoff, interruption, or context-limit recovery:

1. verify repository identity, branch, HEAD, and working-tree state;
2. read `STATE.json` before broad rediscovery;
3. verify the capsule's `currentSha` against repository truth;
4. load only the artifacts/sections listed in `contextManifest` plus code required by the active causal boundary;
5. continue from `nextObligation`;
6. do not re-investigate a referenced proven decision or rerun a referenced valid proof unless its invalidation condition has been triggered;
7. if state is stale or contradictory, repair the capsule from authoritative evidence before continuing.

The capsule therefore reduces context reconstruction without allowing stale memory to override current facts.

## Context manifest

`contextManifest` is the token-control mechanism. It identifies the smallest context required for the next governed action.

Examples:

```text
PROJECT_ADAPTER#testing
SURGICAL_CHANGE.md
CHECKLIST.md#CHG-04
EVIDENCE.md#P-018
services/worker/src/narrative-v2/live-binding.test.js
```

Do not load the entire governed change history when the next obligation can be completed from the manifest.

The manifest may expand only when direct evidence shows additional context is necessary.

## Decision and proof reuse

The capsule stores references, not duplicated decision/proof bodies.

A proven decision reference remains reusable until a documented invalidation trigger occurs. A valid proof reference remains reusable for intermediate work while its governed dependencies remain unchanged.

Exact-head terminal CI, release gates, and any proof explicitly required at the final candidate SHA are never skipped merely because an earlier proof is cached.

## Invalidation

Update or invalidate capsule state when any applicable condition occurs:

- branch or HEAD changes in a way that affects the active obligation;
- the frozen Surgical Change Contract is reopened;
- an active file/boundary changes after its proof;
- a referenced contract/schema/dependency changes;
- new evidence disproves a recorded decision;
- a proof's declared dependency fingerprint changes;
- authorization scope changes;
- an external controlled state required by the next obligation changes.

Do not invalidate unrelated repository knowledge merely because the commit SHA advanced.

## Update discipline

Update `STATE.json` only at meaningful governed transitions, such as:

```text
preflight complete
surgical determinacy PASS
section PASS / FAIL
proof invalidated
scope formally reopened
authorization boundary reached
terminal verification PASS / FAIL
audit PASS / FAIL
closure
```

Do not update it for every thought, command, or conversational turn.

## Relationship to governed learning memory

The State Capsule and learning memory solve different problems:

- `gcu-state-capsule/1.0.0` — current change working state and resumability;
- `gcu-learning-memory/1.0.0` — reusable lessons and approved practices across runs.

The capsule MUST NOT become a second ApprovedPractice store. Learning memory MUST NOT be used to reconstruct the current change state when current repository evidence exists.

## Success condition

A fresh coding context should be able to recover the next governed action by reading:

```text
repository HEAD/status
→ STATE.json
→ contextManifest references
```

without rereading the complete conversation or complete change history.
