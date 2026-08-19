# Surgical Change Determinacy

Surgical Change Determinacy is the v2.3 control that prevents a valid software request from becoming an unnecessarily broad implementation.

It has two enforcement points:

1. a **pre-change Surgical Change Determinacy Gate**;
2. a **post-change Surgical Determinacy Audit**.

Everything between them supplies evidence. GCU deliberately avoids creating separate bureaucratic gates for every sub-control.

## Governing principle

> Every material changed production boundary must be causally necessary for the preserved required outcome.

Supporting principle:

> Discovery does not create authorization.

## 1. Requirement Preservation

Before causal planning, preserve the user's actual request.

Record:

```text
Original requested outcome:
Faithful governed interpretation:
Explicit exclusions / non-goals:
Observable acceptance condition:
```

The governed interpretation must remain implementation-independent.

The Challenger later asks whether the implementation solves the original request or merely the Planner's reformulation.

## 2. Change hypothesis

State why the current behavior differs from the required outcome or, for intentional capability work, what system boundary must change to create the requested capability.

```text
Observed/requested state:
Direct evidence:
Change hypothesis:
Predicted effect:
Status: PROVEN / DISPROVEN / UNRESOLVED
```

Do not implement while a material causal fact is `UNRESOLVED`.

A hypothesis may be disproven during investigation. That is useful evidence. Replace it with a supported hypothesis before implementation.

## 3. Causal boundary

Identify the smallest architectural boundary that direct evidence shows is responsible for the required result.

Examples:

- one renderer consumer;
- one API contract and its validating consumer;
- one persistence adapter;
- one authorization boundary;
- one migration plus its required compatibility reader;
- one producer/consumer handoff.

Do not define the causal boundary as “the whole feature” when evidence supports something narrower.

## 4. Expected change surface

Freeze what is required or reasonably expected to change.

Use three levels:

```text
REQUIRED
Known modules/contracts/components that evidence says must change.

EXPECTED
Known symbols/functions when determinable before implementation.

PROHIBITED
Unrelated modules, contracts, public behavior, and protected boundaries.
```

Symbols are frozen when they are genuinely known. Do not invent false precision merely to fill a template.

## 5. Protected surface

Explicitly name behavior and boundaries that must remain unchanged.

Typical protected surfaces include:

- public API shape;
- authentication/tenant rules;
- persistence schema;
- unrelated report sections;
- upstream producer behavior;
- dependencies;
- configuration;
- release behavior.

Everything outside the justified causal chain is protected by default unless the frozen contract says otherwise.

## 6. Structural change budget

The budget measures architectural surface, not textual size.

Example:

```text
Production modules: 1
Public contracts: 0
Schemas: 0
Persistence boundaries: 0
Dependencies: 0
External integrations: 0
Configuration surfaces: 0
New abstractions: 0
Migrations: 0
Test surfaces: 1 bounded area
```

Do not use:

- maximum lines changed;
- arbitrary diff size;
- maximum function count;
- code-golf style minimality.

Those metrics can reward unsafe shortcuts.

## 7. Acceptance proof

Freeze what evidence will demonstrate the requested result and preservation of relevant prior behavior.

Where safe and feasible, obtain a failing proof before the implementation intended to make it pass.

## 8. Expansion rule

If implementation requires a boundary outside the frozen contract:

```text
STOP
→ do not modify the newly discovered boundary
→ record the evidence
→ reopen Surgical Change Determinacy Gate
→ prove causal necessity
→ update the contract and structural budget
→ continue only after the gate passes again
```

An agent may not use “I discovered I also need…” as automatic scope authorization.

## 9. Incidental findings

Incidental findings are recorded separately.

They do not enter the active change merely because:

- the same file is already open;
- the fix is small;
- the code is poor;
- cleanup would be convenient;
- the agent thinks it is safer;
- the change would reduce technical debt;
- another defect is nearby.

The only automatic relevance test is causal necessity to the preserved requirement. Anything else needs a separately authorized governed change.

## 10. Causal Necessity Audit

After implementation, every material changed boundary must map to:

```text
Requirement ID
→ changed boundary
→ why the requirement would remain incorrect if this boundary were unchanged
→ direct evidence
```

This is stronger and more scalable than blindly reverting every individual line or commit fragment.

Selective revert testing is appropriate when necessity is disputed, coupled changes make the reasoning unclear, or direct causal evidence is otherwise insufficient.

If a material change has no causal mapping, remove it or separately authorize it.

## 11. Surgical Determinacy Audit

At exact candidate head, report:

```text
Requirement preserved: PASS / FAIL
Change hypothesis validated: PASS / FAIL
Required outcome achieved: PASS / FAIL
Material changed boundaries causally justified: PASS / FAIL
Protected surfaces preserved: PASS / FAIL
Structural change budget respected or formally reopened: PASS / FAIL
Incidental findings excluded: PASS / FAIL
Unauthorized scope expansion: ZERO / NONZERO
Unjustified architectural change: ZERO / NONZERO
Unjustified contract change: ZERO / NONZERO
Unjustified dependency change: ZERO / NONZERO

SURGICAL DETERMINACY: PASS / FAIL
```

Any mandatory FAIL or nonzero unauthorized/unjustified state blocks governed completion.

## Example

Requirement:

> Render an existing `competitivePosition` field in the v2 report.

Evidence:

- the validated report object already contains the field;
- the renderer does not consume it.

Frozen contract:

```text
Required outcome:
competitivePosition appears in the rendered report.

Change hypothesis:
The production renderer omits an already-valid field.

Required surface:
report renderer
bounded renderer acceptance test

Protected surface:
generation
schema
normalization
persistence
other report sections
shared utilities

Budget:
Production modules: 1
Contracts/schemas: 0
Dependencies: 0
Persistence: 0
New abstractions: 0
```

A renderer fix plus a helper rename, mapper refactor, schema cleanup, and unrelated error-message change is not surgical merely because all changes pass tests.

The Causal Necessity Audit would reject the unrelated changes because the preserved requirement remains satisfied without them.

## Why only two gates

GCU intentionally uses one strong pre-change determinacy gate and one strong post-change audit.

Requirement preservation, causal hypothesis, expected surface, protected surface, budget, incidental-finding controls, and necessity mapping are evidence within those controls rather than separate lifecycle gates.

This avoids turning surgicality into process bureaucracy.
