# GCU Change Workspace

For material work, keep durable governance/evidence under a change ID so interrupted or multi-agent work can resume from repository state rather than agent memory.

Preferred layout:

```text
.governance/
  PROJECT_ADAPTER.md
  changes/
    <CHANGE-ID>/
      STATE.json
      INTAKE.md
      DISCOVERY.md
      SURGICAL_CHANGE.md
      CHECKLIST.md
      AGENT_ROSTER.md
      TEST_AREA_MAP.md
      EVIDENCE.md
      AUDIT.md
      LEARNING.md
```

Small T1 changes may use a reduced package if repository governance permits it, but the Requirement Preservation and Surgical Change Determinacy obligations still apply. `LEARNING.md` is required only when `gcu-learning-memory/1.0.0` is active for the change. `STATE.json` is preferred for any material, multi-context, interruptible, or long-running change.

## STATE.json

For resumable work, use `gcu-state-capsule/1.0.0` with `templates/GOVERNED_STATE_CAPSULE_TEMPLATE.json`.

The capsule is a compact derived index over authoritative repository state and governed evidence. Record only the current phase, `nextObligation`, active/protected boundaries, unresolved items, decision/proof references, authorization boundary, and `contextManifest` needed for the next action.

Do not copy full evidence, transcripts, prompts, secrets, provider credentials, or authoritative usage/billing transactions into the capsule.

At each meaningful governed transition, update the capsule. Do not update it for every command or conversational turn.

## INTAKE.md

Record:

- objective;
- current user instruction;
- starting SHA;
- Change Tier;
- Release Intent;
- permitted/prohibited operations;
- explicit authorization boundaries.

## DISCOVERY.md

Record only directly supported facts relevant to this change:

- affected components;
- governing sources;
- Project Adapter gaps/staleness;
- boundaries/contracts;
- risks and unknowns.

When governed learning memory is available, record the IDs of active approved practices recalled for this repository/component. Recalled memory remains `ADVISORY_ONLY` and never outranks current repository/user authority.

## SURGICAL_CHANGE.md

Use `templates/SURGICAL_CHANGE_CONTRACT_TEMPLATE.md` or an equivalent durable record.

Freeze:

- Requirement Preservation;
- direct evidence and change hypothesis;
- causal boundary;
- expected and protected surfaces;
- structural change budget;
- acceptance proof;
- expansion conditions.

Record reopen events before implementation expands into any newly justified boundary. Discovery alone never authorizes expansion.

After implementation, add the Causal Necessity Audit and Surgical Determinacy Audit evidence.

## CHECKLIST.md

Use the governed checklist with stable IDs and binary completion.

## AGENT_ROSTER.md

Record role assignment and separation requirements.

## TEST_AREA_MAP.md

Activate only applicable universal test areas and map them to real repository commands.

## EVIDENCE.md

Record evidence, not confidence:

| Obligation | Command/action | Result | Artifact/state | SHA/context | Notes |
|---|---|---|---|---|---|
| | | | | | |

Do not paste secrets or unnecessary sensitive data into evidence files.

## AUDIT.md

Record exact-head audit state, including Surgical Determinacy and whether the audit was independent or `SELF_AUDIT`.

## LEARNING.md

When the governed learning loop is active, record references only:

```text
Contract: gcu-learning-memory/1.0.0
Run-history refs: ...
Approved practices recalled: none | <ids>
Lesson candidates emitted: none | <ids>
Stale/conflicting practices flagged: none | <ids>
Practice promotion performed by producing run: NO
```

The workspace does not become the authoritative Agentic OS lesson/practice ledger. Do not copy full practice stores into the change workspace.

## Resume rule

After interruption, context-limit recovery, or role handoff:

1. inspect repository/branch/HEAD and working-tree state;
2. read `STATE.json` first when present and verify its `currentSha` against repository truth;
3. load only the `contextManifest` references plus code required by the active causal boundary;
4. inspect the frozen Surgical Change Contract only where referenced or when scope has reopened;
5. preserve referenced valid proof and decision state unless its invalidation condition has triggered;
6. continue from `nextObligation`, not from the beginning of discovery;
7. if the capsule conflicts with repository state or direct evidence, repair the capsule before continuing.

Repository state and direct evidence outrank the capsule. The capsule outranks agent/session memory only as a compact resume index. Approved practices remain advisory context only.
