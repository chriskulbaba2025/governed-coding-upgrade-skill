# Architecture

## 1. Purpose

Governed Coding Upgrade separates **universal change governance** from **repository-specific implementation facts**.

The universal layer defines the non-bypassable lifecycle and proof requirements. The project adapter layer records the actual commands, invariants, CI behavior, external-call rules, and release controls of a specific repository.

## 2. Control layers

```text
External safety / legal / security constraints
                    ↓
Current user authorization and scope
                    ↓
Repository governance and product contracts
                    ↓
Protected invariants
                    ↓
Governed Coding Upgrade skill
                    ↓
Governed Change Profile
                    ↓
Frozen checklist
                    ↓
Compiled execution plan
                    ↓
Implementation + proof
```

A lower layer cannot silently override a higher layer.

## 3. Runtime roles

### Implementer

Builds only the frozen checklist, produces direct evidence, runs required verification, and reports the exact candidate head.

### Verifier

Executes deterministic repository and behavior checks. Verification must fail non-zero when a governed requirement is not satisfied.

### Independent auditor

Inspects the actual exact-head implementation and proof. The auditor does not accept an implementation report as proof by itself and does not authorize a different SHA than the one inspected.

### Release authority

Provides whatever merge, deploy, release, or activation approval the repository and current user instructions require. Passing audit is necessary but does not silently create release authorization.

## 4. Project adapter

The `Governed Change Profile` prevents every work package from rediscovering the same repository facts. It records:

- package/runtime systems;
- narrow, acceptance, regression, build, static-analysis, and security commands;
- CI exact-head verification method;
- protected invariants;
- migration and lockfile policies;
- external-call restrictions;
- rollback mechanism;
- merge/release authorization rules.

Unknown facts remain `UNRESOLVED`; they are not guessed.

## 5. Evidence architecture

Evidence is attached to stable checklist IDs. A checklist item is complete only when its proof supports the exact governed claim.

Strong evidence includes assertions, state, artifacts, hashes, counts, commands, exact diffs, exact SHAs, and CI runs tied to those SHAs.

Weak evidence includes prose, test names, comments, confidence scores, and green CI with no connection to the specific requirement.

## 6. Correction architecture

Independent audit failures are grouped into one bounded correction package containing only failed IDs. Accepted scope is not reopened unless the correction directly requires it. The corrected exact head is then fully verified and independently re-audited.

This design reduces correction loops without lowering the acceptance threshold.
