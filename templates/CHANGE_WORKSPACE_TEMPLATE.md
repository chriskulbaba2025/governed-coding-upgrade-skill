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
      CHECKLIST.md
      AGENT_ROSTER.md
      TEST_AREA_MAP.md
      EVIDENCE.md
      AUDIT.md
```

Small T1 changes may use a reduced package if repository governance permits it.

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

Record exact-head audit state, including whether the audit was independent or `SELF_AUDIT`.

## Resume rule

After interruption or role handoff:

1. inspect repository/branch/HEAD;
2. inspect this workspace;
3. inspect current diff and test evidence;
4. continue from the first unproven obligation.

The workspace does not override higher-order repository governance or current user authorization.
