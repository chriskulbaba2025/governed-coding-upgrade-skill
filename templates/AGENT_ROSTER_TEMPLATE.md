# GCU Agent Roster

**Change ID:**  
**Repository:**  
**Change Tier:** T1 LOCAL / T2 BOUNDARY / T3 SYSTEM / T4 RELEASE  
**Release Intent:** CHANGE_ONLY / STAGING_READY / PRODUCTION_READY  

Roles are responsibilities, not required separate processes. One agent or human may hold several roles unless governance requires separation.

| Role | Assigned agent/human | Separate context? | Write authority | Required output | Status |
|---|---|---|---|---|---|
| Scout | | | Read-only by default | Discovery facts / adapter gaps | |
| Planner | | | Plan/governance files only by default | Frozen change package | |
| Builder | | | Permitted implementation scope | Section implementation | |
| Challenger | | | No production edits by default | Falsification findings | |
| Verifier | | | Test/evidence files if authorized | Test-area evidence | |
| Auditor | | | No implementation edits during audit | Exact-head audit | |
| Release Authority | | | Protected operation authority | Authorization decision | |

## Separation requirements

- Independent auditor required? YES / NO
- If NO, audit label: `SELF_AUDIT`
- Separate terminal verifier required? YES / NO
- Separate challenger required? YES / NO
- Parallel builders allowed? YES / NO

## Parallel ownership when allowed

| Workstream | Owner | Permitted paths/boundaries | Shared contracts | Merge order | Integration owner |
|---|---|---|---|---|---|
| | | | | | |

## Handoff record

Each handoff must include:

- current SHA;
- adapter verified SHA/version;
- active checklist IDs;
- permitted/prohibited scope;
- active test areas;
- direct evidence obtained;
- failures/unresolved items;
- next authorization boundary.
