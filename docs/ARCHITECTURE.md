# Architecture

## 1. Purpose

Governed Coding Upgrade separates **universal change governance** from **repository-specific implementation facts**.

The universal layer defines non-bypassable lifecycle and proof requirements. The repository adapter layer records actual commands, invariants, CI behavior, controlled-test policies, and release controls.

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
Sequential Evidence Gates
                    ↓
Balanced machine verification
                    ↓
Terminal machine release gate
                    ↓
Independent exact-head audit
                    ↓
Release authority
```

A lower layer cannot silently override a higher layer.

## 3. Runtime roles

### Implementer

Builds only governed scope, produces direct evidence, closes ordered sections sequentially, and reports the exact candidate head. The implementer cannot override a failed terminal gate.

### Section verifier

Runs the narrowest executable proof after each section. It verifies required negative behavior and checks earlier boundaries only when the new section can materially invalidate them.

### Terminal verifier

After all sections pass, runs cross-section review, full acceptance, full regression, invariant/scope checks, and the repository terminal machine release gate.

### Independent auditor

Inspects the actual exact-head implementation and proof. The auditor does not accept the implementation report as proof by itself and does not authorize a different SHA than the one inspected.

### Release authority

Provides merge, deploy, release, or activation approval required by repository and user instructions. Passing code verification does not silently create release authorization.

## 4. Governed Change Profile

The profile prevents every work package from rediscovering the same repository facts. It records:

- package/runtime systems;
- narrow, affected-integration, acceptance, regression, build, static-analysis, and security commands;
- terminal machine release-gate command;
- CI exact-head verification method;
- protected invariants;
- migration, persistence, and rollback rules;
- external-call restrictions;
- controlled-test credential isolation;
- call-counter source;
- merge/release authorization rules.

Unknown facts remain `UNRESOLVED`; they are not guessed.

## 5. Sequential evidence architecture

Large changes are decomposed into ordered sections that share architectural boundaries.

```text
section N
  inspect
  → define proof
  → implement
  → narrow verify
  → section audit
  → PASS
      ↓
section N+1
```

Dependent work does not proceed through a failed section. Routine section PASS automatically continues unless the next step crosses an explicit authorization boundary.

This reduces late defect accumulation without requiring the full repository suite after every edit.

## 6. Balanced verification architecture

Verification has three levels:

### A. Narrow section verification

Fast direct proof for the current boundary.

### B. Affected integration verification

Runs only when a new section can invalidate an earlier boundary or contract.

### C. Terminal verification

Runs after all sections pass:

```text
cross-section review
→ full production acceptance
→ full regression
→ static/build/security/invariant checks
→ scope/diff verification
→ terminal machine release gate
```

The full gate pays the expensive verification cost once at the release boundary rather than repeatedly during isolated section work.

## 7. Evidence architecture

Evidence is attached to stable checklist IDs. A checklist item is complete only when proof supports the exact governed claim.

Strong evidence includes assertions, state, artifacts, hashes, counts, exact diffs, exact SHAs, production-path execution, transport/client counters, release-gate exit status, and CI runs tied to the exact SHA.

Weak evidence includes prose, test names, comments, confidence scores, fabricated downstream success objects, hardcoded zero-call claims, and local substitutes for mandatory exact-head CI.

## 8. Controlled external-call architecture

Provider/model acceptance should place deterministic control **below real production adapters**.

```text
production adapter/service
        ↓
injected controlled transport/client
        ↓
deterministic fixture
```

Controlled test processes should isolate real credentials where technically feasible and fail unexpected live execution. Call counts are read from actual transport/client counters.

## 9. Terminal release decision architecture

The agent is not the release authority.

A repository command such as `change:release-gate` evaluates machine-enforceable release conditions and exits non-zero when any mandatory condition is missing or failed.

```text
machine gate exit 0 + required independent audit + authorization
→ RELEASE READY

local code verification PASS + mandatory external CI unavailable
→ CODE VERIFIED / GOVERNANCE HOLD

repository-controlled required condition FAIL
→ BLOCKED
```

This prevents prose from turning an environmental exception into a false governed PASS.

## 10. Correction architecture

When a section, terminal gate, or independent audit fails, assign the failure to the owning checklist ID, correct the smallest governed boundary, rerun its narrow proof and affected later sections, then rerun terminal verification and exact-head audit.

This design reduces correction loops without lowering the acceptance threshold.
