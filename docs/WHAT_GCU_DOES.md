# What Governed Coding Upgrade Does

Governed Coding Upgrade (GCU) is a control system for intentional software change.

Its purpose is not to make an AI coding agent more creative. Its purpose is to make the agent's changes **bounded, explainable, testable, auditable, and truthful**.

## The simple version

Without governance, a coding agent can receive one request and produce a much broader patch:

```text
requested fix
+ nearby cleanup
+ refactor
+ dependency change
+ speculative hardening
+ renamed helpers
= a larger and harder-to-audit change
```

GCU instead requires:

```text
preserve the requirement
→ prove the relevant cause or change hypothesis
→ freeze the smallest justified change surface
→ protect everything else
→ implement inside that boundary
→ prove the real behavior
→ audit the exact resulting commit
```

## What “governed” means

GCU separates five questions that coding agents often blur together:

1. **What did the user actually ask for?** — Requirement Preservation.
2. **What must change to satisfy it?** — Surgical Change Determinacy.
3. **How much proof is required?** — Change Tier, Release Intent, and Test Area Map.
4. **Did the real system behave correctly?** — acceptance, negative-path, Production Spine, contract and terminal proof.
5. **Can we trust the candidate commit?** — machine gates, complete diff inspection, exact-head audit, and truthful release state.

## What GCU prevents

GCU is specifically designed to prevent:

- accidental scope expansion;
- opportunistic refactoring;
- “while we are here” changes;
- solving a symptom without establishing the responsible boundary;
- silently changing contracts, schemas, persistence, dependencies, or architecture;
- treating newly discovered problems as automatically authorized work;
- tests that prove a mock or fabricated path instead of production behavior;
- declaring a scoped PASS to be production readiness;
- calling same-context review independent audit;
- treating model confidence as evidence.

## Surgical Determinacy

A surgical change is not defined by a tiny diff.

It is defined by **causal necessity**.

A 100-line change can be surgical if all 100 lines are required by one proven causal boundary. A three-line change can be unsafe if it bypasses a contract or hides a required system correction.

GCU therefore uses a structural change budget instead of line limits.

## Discovery does not create authorization

This is a core v2.3 principle.

During investigation, an agent may discover technical debt, weak tests, a security concern, stale naming, duplicated logic, or another defect.

That discovery is useful information. It is **not permission to modify it**.

The finding remains outside the active change unless the agent proves that the frozen requirement cannot be satisfied correctly without changing that boundary. If so, the determinacy gate must be reopened before the scope expands.

## When to use GCU

Use GCU for intentional changes to source, tests, APIs, schemas, dependencies, executable configuration, persistence, migrations, integrations, infrastructure, build/release behavior, or generated production artifacts.

Read-only investigation can remain read-only until a change is authorized.

## Does every change require the same ceremony?

No.

Change Tier scales documentation and proof depth:

- `T1_LOCAL` — contained local behavior;
- `T2_BOUNDARY` — contracts/interfaces/boundaries;
- `T3_SYSTEM` — cross-boundary/system behavior;
- `T4_RELEASE` — staging/production/release readiness.

The surgical causal rule applies at every tier, but a small T1 fix does not require the same artifact depth as a T4 production release.

## What GCU is not

GCU is not:

- a model router;
- a credential store;
- a billing ledger;
- a replacement for repository CI;
- a release authority;
- a programming language or framework;
- a requirement to use multiple AI agents;
- a guarantee that an LLM will never make a mistake.

It is a protocol that reduces ambiguity and requires direct proof before stronger completion claims are allowed.

## The output

A governed change should leave a reviewer able to answer:

```text
What was requested?
What evidence established the relevant cause or change hypothesis?
What was allowed to change?
What was protected?
Why was every material changed boundary necessary?
What proof ran?
What exact SHA was audited?
What is the truthful readiness state?
```

If those questions cannot be answered from evidence, the change is not governed complete.
