# GCU Agent Roster

**Change ID:**  
**Repository:**  
**Change Tier:** T1 LOCAL / T2 BOUNDARY / T3 SYSTEM / T4 RELEASE  
**Release Intent:** CHANGE_ONLY / STAGING_READY / PRODUCTION_READY  
**Execution-control contract:** `gcu-execution-control/1.0.0` / N/A  

Roles are responsibilities, not required separate processes. One agent or human may hold several roles unless governance requires separation.

| Role | Assigned agent/human | Separate context? | Capability floor | Write authority | Required output | Status |
|---|---|---|---|---|---|---|
| Scout | | | ECONOMY / STANDARD / ADVANCED / PREMIUM | Read-only by default | Discovery facts / adapter gaps | |
| Planner | | | ECONOMY / STANDARD / ADVANCED / PREMIUM | Plan/governance files only by default | Frozen change package | |
| Builder | | | ECONOMY / STANDARD / ADVANCED / PREMIUM | Permitted implementation scope | Section implementation | |
| Challenger | | | ECONOMY / STANDARD / ADVANCED / PREMIUM | No production edits by default | Falsification findings | |
| Verifier | | | ECONOMY / STANDARD / ADVANCED / PREMIUM | Test/evidence files if authorized | Test-area evidence | |
| Auditor | | | ECONOMY / STANDARD / ADVANCED / PREMIUM | No implementation edits during audit | Exact-head audit | |
| Release Authority | | | N/A unless explicitly governed | Protected operation authority | Authorization decision | |

Capability floors are provider-neutral requests. They are not provider/model aliases and do not grant permission to change routing or spend.

## Execution control plane when present

- Execution orchestrator:
- AI policy authority:
- Budget-envelope ref:
- Model-route approval required for escalation? YES / NO / N/A
- Usage-receipt refs required? YES / NO / N/A
- Direct provider/model access from agent contexts: FORBIDDEN / CONTROLLED / N/A
- Silent provider/model fallback: FORBIDDEN / CONTROLLED / N/A

## Separation requirements

- Independent auditor required? YES / NO
- If NO, audit label: `SELF_AUDIT`
- Separate terminal verifier required? YES / NO
- Separate challenger required? YES / NO
- Parallel builders allowed? YES / NO

A stronger or more expensive model in the same Builder context does not make an audit independent.

## Escalation record

When a role needs more capability, record rather than silently reroute:

- Role:
- Section/gate:
- Current capability:
- Requested capability:
- Reason: CAPABILITY_INSUFFICIENT / INDEPENDENCE_REQUIRED / CONTEXT_LIMIT / REPEATED_PROOF_FAILURE / POLICY_REQUIREMENT / MATERIAL_AMBIGUITY
- Approval ref:
- Routing-decision ref:
- Status: REQUESTED / APPROVED / DENIED / EXPIRED

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
- execution-control task/run refs when applicable;
- routing/approval refs when applicable;
- usage-receipt refs already obtained when applicable;
- failures/unresolved items;
- next authorization boundary.