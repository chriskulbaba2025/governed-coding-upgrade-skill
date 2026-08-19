# GCU Change Workspace

For material work, keep durable governance/evidence under a change ID so interrupted or multi-agent work can resume from repository state rather than agent memory.

Preferred layout:

```text
.governance/
  PROJECT_ADAPTER.md
  changes/
    <CHANGE-ID>/
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

Small T1 changes may use a reduced package if repository governance permits it, but the Requirement Preservation and Surgical Change Determinacy obligations still apply. `LEARNING.md` is required only when `gcu-learning-memory/1.0.0` is active for the change.

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

After interruption or role handoff:

1. inspect repository/branch/HEAD;
2. inspect this workspace;
3. inspect the frozen Surgical Change Contract and any reopen history;
4. inspect current diff and test evidence;
5. continue from the first unproven obligation.

The workspace does not override higher-order repository governance, current user authorization, or current evidence. Approved practices are advisory context only.
