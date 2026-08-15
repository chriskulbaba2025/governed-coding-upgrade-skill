# Execution Control Plane Integration

**Contract family:** `gcu-execution-control`
**Contract version:** `1.0.0`
**Protocol:** Governed Coding Upgrade v2.2.0
**Status:** Governing integration contract
**Canonical request schema:** `schemas/execution_control_request.schema.json`

## Purpose

Governed Coding Upgrade (GCU) governs the correctness, proof, audit, and release-readiness lifecycle of a software change. It may run inside a larger agent runtime or AI policy platform, but it must not become a second model router, billing system, credential broker, orchestration ledger, or policy authority.

This contract defines the boundary between GCU and an external execution control plane.

## Root boundary

```text
GCU
  owns: change scope, proof obligations, roles, acceptance, challenge, audit
  emits: execution context and capability requests

Execution orchestrator
  owns: task/run lifecycle, agent assignment, approvals, human wait, escalation state
  emits: authorized AI-operation request

AI policy authority
  owns: provider/model resolution, credentials, cost ceilings, usage accounting, policy audit
  emits: routing decision and durable usage receipt
```

GCU MUST remain operable without any specific execution-control product. Repositories without an external control plane may use a local/manual adapter, but must preserve the same authority boundaries.

## Authority rules

1. GCU MUST NOT choose a provider or concrete model as an execution side effect.
2. GCU MUST NOT silently escalate to a more capable or more expensive model.
3. GCU MUST NOT store provider credentials.
4. GCU MUST NOT maintain a competing authoritative billing or usage ledger.
5. GCU MAY request a capability class and MAY record an approved budget-envelope reference.
6. The control plane MUST return durable routing, approval, and usage references when those capabilities exist.
7. A model-routing or budget decision made outside GCU cannot override GCU proof, audit, scope, or release gates.
8. A GCU PASS cannot override a denied execution-policy decision.

## Execution-context request

For a governed role or section that requires an AI execution decision, GCU emits or records the following logical fields:

```text
contract: gcu-execution-control/1.0.0
change_id
repository
branch
candidate_sha when available
change_tier
release_intent
role
workload_class
capability_floor
independence_required
section_or_gate
authorization_boundary
budget_envelope_ref when supplied
escalation_reason when applicable
```

The canonical machine-readable representation is `schemas/execution_control_request.schema.json`. Product-specific adapters may maintain receiving mirrors, but the GCU schema remains the contract authority.

### `role`

GCU governance roles may include:

```text
SCOUT
PLANNER
BUILDER
CHALLENGER
VERIFIER
AUDITOR
RELEASE_AUTHORITY
```

Only these roles are AI-executable through `gcu-execution-control/1.0.0`:

```text
SCOUT
PLANNER
BUILDER
CHALLENGER
VERIFIER
AUDITOR
```

`RELEASE_AUTHORITY` is deliberately excluded from the canonical execution request schema. It is a human or repository-controlled governance role, never a request for an AI model to approve its own release.

### `workload_class`

```text
DISCOVERY
PLANNING
CODING
VERIFICATION
CHALLENGE
AUDIT
SUMMARIZATION
```

### `capability_floor`

Provider-neutral classes:

```text
ECONOMY
STANDARD
ADVANCED
PREMIUM
```

These are minimum capability requests, not model aliases. The external policy authority maps them to approved server-side aliases and concrete providers/models.

GCU MUST NOT encode provider names, provider model IDs, API endpoints, credentials, or price tables into this field.

## Escalation contract

When the current execution capability is insufficient, GCU records one escalation request rather than switching models itself.

Allowed reasons:

```text
CAPABILITY_INSUFFICIENT
INDEPENDENCE_REQUIRED
CONTEXT_LIMIT
REPEATED_PROOF_FAILURE
POLICY_REQUIREMENT
MATERIAL_AMBIGUITY
```

Required escalation state:

```text
change_id
role
section_or_gate
current_capability
requested_capability
reason
current_evidence
approval_ref when required
status: REQUESTED | APPROVED | DENIED | EXPIRED
```

Rules:

- `DENIED` or `EXPIRED` MUST NOT be treated as approval.
- A higher-cost or cross-provider route MUST NOT occur until the controlling policy allows it.
- Repeated escalation attempts MUST use the same governed change identity and remain auditable.
- Escalation does not reset or erase prior evidence.

## Cost-governance contract

GCU distinguishes two cost domains:

1. **Product external-call cost** — calls made by the software under test. This remains governed by GCU's `EXTERNAL CALL / COST` Test Area and external-call contract.
2. **Execution-resource cost** — AI/model usage consumed by agents performing the governed change. This belongs to the execution control plane.

GCU MAY require an execution budget before a role or gate proceeds, but the authoritative estimate, pricing, enforcement, and accounting belong to the control plane.

GCU records references only:

```text
budget_envelope_ref
routing_decision_ref
approval_ref
usage_receipt_ref[]
execution_cost_status: WITHIN_BUDGET | BLOCKED | UNAVAILABLE | N/A
```

Hardcoded cost claims are not evidence.

## Persistent usage receipts

When a control plane supplies durable usage accounting, the final GCU evidence MUST retain enough references to reconcile the governed change with the authoritative usage record without copying the full ledger.

Recommended receipt identity:

```text
change_id
orchestrator_task_id
orchestrator_run_id
policy_operation_id
usage_receipt_id
routing_decision_id
approval_id when applicable
```

The authoritative usage system owns token counts, provider/model identity, actual or estimated cost, timestamps, tenant/team/user identity, and billing aggregation.

GCU stores the receipt IDs and final policy status, not a duplicate billing transaction.

## Audit and independence

A routing decision does not prove audit independence.

If an independent Auditor or Challenger is required, the orchestration layer must provide a distinct execution context when required by repository governance. GCU records the independence result separately from the model route.

A premium model used in the same Builder context remains `SELF_AUDIT` when the same context performs the audit.

## Fail-closed behavior

GCU MUST stop or report `BLOCKED` / `GOVERNANCE HOLD` when a mandatory execution-control obligation is materially unresolved, including:

- required route approval denied or missing;
- required usage receipt missing after governed execution;
- policy authority reports budget exceeded;
- provider/model bypass is detected;
- silent fallback is detected where prohibited;
- independent context is required but not provided;
- `RELEASE_AUTHORITY` appears in an AI execution request.

## Product-specific adapters

This contract is intentionally vendor-neutral.

A product-specific adapter MAY map this contract into its native records, for example:

```text
GCU execution context
→ task/run/approval records in an execution orchestrator
→ authorized AI-operation packet
→ server-side model alias resolution in an AI policy authority
→ durable usage/audit receipt
→ receipt references returned to GCU evidence
```

Product-specific adapters MUST NOT redefine GCU's change-proof authority, redefine the canonical request schema, or create a second routing/billing authority inside GCU.

## Project Adapter fields

Repositories integrating an execution control plane should record:

```text
Execution orchestrator:
AI policy authority:
Integration contract/version:
Capability mapping owner:
Budget-envelope authority:
Model-route approval authority:
Usage ledger authority:
Usage receipt lookup method:
Escalation/human-wait mechanism:
Independent-context mechanism:
Direct provider/model calls from coding agents: FORBIDDEN / CONTROLLED / N/A
```

Unknown material fields are `UNRESOLVED`.

## Final-report evidence

When applicable, the governed final report includes:

```text
Execution control plane: PASS / N/A / BLOCKED
Integration contract/version:
Orchestrator task/run refs:
Routing decision refs:
Escalation/approval refs:
Budget envelope ref:
Usage receipt refs:
Execution cost status:
Provider/model bypass check:
```

Provider/model names may appear in returned evidence, but they are not selected by GCU.

## Compatibility

This contract is additive to GCU v2.2.0. It does not require Agentic OS, Controlled AI Portal, Claude Code, LiteLLM, DeepSeek, OpenAI, or any other specific product. Those systems may implement adapters while preserving this contract's authority separation.