# Architecture

## Purpose

Governed Coding Upgrade separates universal change governance from repository-specific implementation facts. v2.1 adds production-spine and contract-boundary proof without removing v1.2 sequential execution and machine-gate controls.

## Control layers

```text
External safety / legal / security constraints
→ Current user authorization and scope
→ Repository governance and product contracts
→ Protected invariants
→ Governed Coding Upgrade skill
→ Governed Change Profile
→ Release intent
→ Production Spine + Producer/Contract/Consumer map
→ Acceptance contract freeze + false-PASS scan
→ Frozen checklist
→ Sequential Evidence Gates
→ Balanced verification
→ Cross-section review
→ Terminal-path gate
→ Full-system readiness gate when PRODUCTION_READY
→ Terminal machine release gate
→ Independent exact-head audit
→ Release authority
```

A lower layer cannot silently override a higher layer.

## Runtime roles

### Implementer

Builds only governed scope, produces direct evidence, closes ordered sections sequentially, and cannot override a failed terminal gate.

### Section verifier

Runs the narrowest direct proof after each section and reruns affected earlier boundaries only when they can be invalidated.

### Terminal verifier

Runs cross-section review, full acceptance/regression, static/build/security/invariant checks, terminal-path/system-readiness checks as applicable, and the machine release gate.

### Independent auditor

Inspects the actual exact-head implementation and proof rather than accepting the implementation report as proof.

### Release authority

Provides merge/deploy/release authorization required by governance. Passing verification does not create authorization.

## Governed Change Profile

The profile stores repository facts that should not be rediscovered in every change:

- build/runtime/test systems;
- narrow, affected, acceptance, regression, static, security, scope, and machine-gate commands;
- migration and persistence/recovery policy;
- external-call and controlled-test policy;
- release-intent policy;
- production-spine and contract-map locations;
- acceptance-freeze and false-PASS method;
- terminal promise and system-readiness method;
- exact-head CI method;
- protected invariants;
- rollback and release authorization.

Unknown facts remain `UNRESOLVED`.

## Production Spine architecture

The production spine prevents isolated component PASS from being mistaken for end-to-end correctness.

```text
real entry
→ auth/validation when applicable
→ service/application boundary
→ persistence/durable state
→ jobs/external services when applicable
→ normalization/contracts
→ decision/transformation
→ rendering/publication/delivery
→ terminal retrieval/outcome
```

Every material handoff is mapped as Producer → Contract → Consumer with state/artifact, validation point, failure behavior, authorization/tenant implication, and direct proof.

## Acceptance architecture

Acceptance is designed before implementation. The frozen acceptance record names:

- real production modules executed;
- controlled dependency seam;
- production contracts/validators;
- persisted state/artifacts inspected;
- positive terminal assertion;
- negative/fail-closed assertion;
- prohibited later effects;
- external-call ceiling;
- exact command.

The false-PASS scan rejects proof that bypasses the production boundary being claimed.

## Sequential evidence architecture

```text
inspect
→ define proof
→ reproduce failure when safe/feasible
→ implement complete section
→ narrow verify
→ section audit
→ PASS
→ next section
```

A failed section is corrected before dependent work proceeds. Routine PASS automatically continues unless the next action crosses an explicit authorization boundary.

## Balanced verification architecture

Three levels:

1. narrow section verification;
2. affected integration verification;
3. one terminal full verification after all sections pass.

This reduces cycle time without weakening final acceptance.

## Evidence and validated-object architecture

Strong proof includes exact assertions, persisted state, artifacts/hashes, production-path execution, measured call/task counts, restart proof, exact object equality/identity where governed, exact diffs/SHAs, terminal retrieval, machine-gate status, and exact-head audit.

For governed boundaries:

```text
assemble complete object
→ validate
→ retain/freeze when applicable
→ persist/transition/render/publish/authorize/consume the validated object
```

## External-call and durable-job architecture

External integrations define task/request identity, timeouts, retry classification, budgets, cancellation, recovery/reuse, duplicate-work prevention, and measured counters. Controlled tests execute below production adapters and avoid unintended live execution where technically feasible.

Asynchronous work persists enough state to recover from a fresh process without reconstructing required input from defaults.

## Terminal and system-readiness architecture

`CHANGE_ONLY` proves the scoped change. `STAGING_READY` proves the governed staging promise. `PRODUCTION_READY` additionally proves the terminal user/business promise and applicable system responsibilities such as production composition, persistence/migrations, access isolation, executable contracts, adapters, durability/recovery, external-call controls, publication/retrieval, rollback, exact-head CI, machine gate, audit, and authorization.

A scoped PASS and system readiness are reported separately.

## Correction architecture

When a section, terminal gate, or audit fails, assign the failure to the owning checklist ID, correct the smallest governed boundary, rerun its direct proof and affected later sections, then rerun terminal verification and exact-head audit.

If a production defect escaped earlier green proof, correct both the implementation and the proof system that allowed the false PASS.
