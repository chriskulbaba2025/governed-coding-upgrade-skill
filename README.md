<p align="center">
  <img src="branding/logo.svg" alt="Governed Coding Upgrade" width="760">
</p>

<p align="center">
  <strong>A deterministic governance and production-closure protocol for AI-assisted software changes.</strong><br>
  Frozen scope. Sequential proof. Real-path acceptance. Balanced machine checks. Exact-head audit. Evidence-based release.
</p>

<p align="center">
  <code>v1.2.0 — Sequential Evidence Gates</code> · <strong>99/100 semantic quality score</strong> · <strong>All 5 areas ≥19/20</strong>
</p>

> **Official canonical repository.** This repository is maintained and controlled by **Chris Kulbaba (@chriskulbaba2025)**. Public forks and derivative copies are not official releases and cannot represent themselves as the canonical Governed Coding Upgrade repository.

---

# Governed Coding Upgrade v1.2.0 — Sequential Evidence Gates

**Governed Coding Upgrade (GCU)** is a project-agnostic execution skill for coding agents and engineering teams. It converts software changes from an informal edit/test loop into a controlled lifecycle with explicit scope, stable checklist IDs, direct proof, sequential section gates, real-production-path acceptance, balanced machine verification, independent exact-head audit, and evidence-based release authorization.

The machine-facing skill name remains `governed-coding-upgrade` so existing v1.x installations continue to work.

## What v1.2.0 adds

- **Sequential Evidence Gates:** complex closure work runs section by section using `inspect → define proof → implement → narrow verify → section audit → auto-continue on PASS`.
- **Balanced machine verification:** narrow checks after each section, affected integration checks only when boundaries are crossed, then one full terminal verification after all sections pass.
- **Terminal machine release gate:** a repository command such as `change:release-gate` becomes the authoritative machine decision for release readiness; agent prose cannot override a failed gate.
- **Governance-hold state:** mandatory external CI/platform unavailability no longer gets mislabeled as a code defect or falsely converted into PASS. Verified code can be reported as `CODE VERIFIED / GOVERNANCE HOLD` until the unchanged exact SHA receives the required external proof.
- **Controlled credential isolation:** provider/LLM acceptance should sandbox real credentials, inject controlled transports below production adapters, fail unexpected live network calls, and measure actual call counters.
- **Interrupted-session resume:** API/agent connection loss resumes from repository evidence and the last proven section rather than restarting completed work.
- **Cross-section integration review:** upstream validated objects are checked against downstream consumers before the full release gate.
- **Reusable machine gate template:** [`templates/MACHINE_RELEASE_GATE_TEMPLATE.md`](templates/MACHINE_RELEASE_GATE_TEMPLATE.md).

See [`CHANGELOG.md`](CHANGELOG.md) for release history.

## Governed lifecycle

### Standard governed change

```text
INTAKE
  ↓
PREFLIGHT
  ↓
PROJECT PROFILE
  ↓
FROZEN CHECKLIST
  ↓
BUILD
  ↓
VERIFY
  ↓
INDEPENDENT EXACT-HEAD AUDIT
  ↓
CONSOLIDATED CORRECTION
  ↓
RE-AUDIT
  ↓
CLOSE / RELEASE
```

### Production Closure Mode v1.2.0

```text
INTAKE
  ↓
PREFLIGHT
  ↓
ONE PRODUCTION-CLOSURE CHECKLIST
  ↓
SEQUENTIAL EVIDENCE GATES
  ↓
CROSS-SECTION REVIEW
  ↓
FULL TERMINAL VERIFICATION
  ↓
MACHINE RELEASE GATE
  ↓
INDEPENDENT EXACT-HEAD AUDIT
  ↓
CORRECTION / RE-AUDIT WHEN REQUIRED
  ↓
RELEASE READY OR GOVERNANCE HOLD / BLOCKED
```

## Non-negotiable controls

- Scope is explicit before implementation.
- Every checklist item has a stable ID and direct proof.
- Permitted and prohibited files are explicit.
- Protected invariants are identified before editing.
- Multi-section work closes each section before dependent work proceeds.
- Acceptance executes the real production implementation with controlled dependencies.
- Controlled tests must not silently use real credentials or network paths when isolation is feasible.
- Negative paths prove persisted state and prohibited side effects, not only thrown exceptions.
- Repository-owned missing infrastructure is implementation work during Production Closure Mode.
- Full regression is balanced: narrow verification during sections, full terminal verification after all sections pass.
- Required exact-head CI cannot be replaced by a local substitute.
- The implementation cannot authorize its own release or override the machine release gate.
- Merge, deploy, release, activation, and live paid calls remain subject to explicit authorization.

## Repository structure

| Path | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | Authoritative Governed Coding Upgrade v1.2.0 skill |
| [`GLOBAL_CLAUDE_RULE.md`](GLOBAL_CLAUDE_RULE.md) | Mandatory global invocation rule |
| [`SCORECARD.md`](SCORECARD.md) | Five-area semantic quality assessment |
| [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | Control model and machine-gate architecture |
| [`docs/ADOPTION_GUIDE.md`](docs/ADOPTION_GUIDE.md) | Installation and repository onboarding procedure |
| [`templates/PRODUCTION_CLOSURE_TEMPLATE.md`](templates/PRODUCTION_CLOSURE_TEMPLATE.md) | Reusable production-closure execution prompt |
| [`templates/MACHINE_RELEASE_GATE_TEMPLATE.md`](templates/MACHINE_RELEASE_GATE_TEMPLATE.md) | Repository-level terminal release-gate contract |
| [`templates/`](templates/) | Profile, checklist, audit, correction, and final-report templates |
| [`.github/`](.github/) | Pull-request, issue, security, ownership, and CI governance |
| [`scripts/validate-package.py`](scripts/validate-package.py) | Zero-dependency package integrity validator |
| [`branding/`](branding/) | Repository logo, icon, and social-card assets |

## Installation model

GCU has two layers:

1. **Execution skill** — install `SKILL.md` wherever the coding agent loads reusable skills.
2. **Mandatory invocation rule** — add `GLOBAL_CLAUDE_RULE.md` to the global instruction layer.

Each repository supplies its actual commands and invariants through a **Governed Change Profile**. v1.2.0 adds fields for affected-integration verification, controlled-test credential policy, and the terminal machine release gate.

Start with [`docs/ADOPTION_GUIDE.md`](docs/ADOPTION_GUIDE.md).

## Sequential closure rule

For complex production closure, each section follows:

```text
inspect
→ define proof
→ reproduce failure when safe/feasible
→ implement complete section
→ narrow verify
→ section audit
→ automatically continue on PASS
```

A failed section is corrected before dependent sections proceed. Routine PASS does not require user approval to continue unless the next step crosses an explicit authorization boundary.

## Balanced verification rule

Use the lightest check that proves the current boundary, then pay the cost of full verification once at the terminal point:

```text
section narrow proof
→ affected integration when needed
→ all sections PASS
→ cross-section review
→ full acceptance/regression/invariant/scope verification
→ machine release gate
```

This is designed to reduce active cycle time without weakening final proof.

## Machine release rule

The preferred repository responsibility is:

```text
change:release-gate
```

The coding agent may not output `RELEASE READY` unless the configured required terminal gate passes. A mandatory external CI outage produces `CODE VERIFIED / GOVERNANCE HOLD`, not final PASS.

## Proof model

Strong proof includes:

- exact assertions;
- exact lifecycle/state history;
- persisted round-trip values;
- stored artifacts and hashes;
- real production adapter/service execution with injected controlled dependencies;
- controlled/live provider and model call counts;
- retry and duplicate-task counts;
- restart/resume proof;
- object identity/equality where governed;
- exact changed-file list;
- exact final SHA;
- required CI tied to that SHA;
- terminal release-gate result;
- independent exact-head audit.

Test names, comments, fabricated success objects, hardcoded PASS counters, prose, confidence, and green CI by itself are not substitutes for governed proof.

## Semantic quality gate

| Area | Score |
|---|---:|
| Governance & Control | **20/20** |
| Execution Process & Determinism | **20/20** |
| Testing, Evidence & Audit Quality | **20/20** |
| Automation & Delivery Efficiency | **19/20** |
| Generalizability & Portability | **20/20** |
| **Total** | **99/100** |

See [`SCORECARD.md`](SCORECARD.md) for the rationale.

## Versioning

The repository uses semantic versioning for the protocol artifact:

- patch: corrections that do not add protocol capability;
- minor: backward-compatible governance capability;
- major: incompatible invocation or protocol contract changes.

Version 1.2.0 is a minor release because sequential evidence gates and machine release controls add backward-compatible capability while preserving the stable `governed-coding-upgrade` invocation name.

## Design principle

> A coding change is not complete because an agent says it is complete. It is complete when governed requirements are directly proven at the exact candidate head and the configured machine and independent release gates agree.

## Status

**Display name:** Governed Coding Upgrade v1.2.0 — Sequential Evidence Gates  
**Machine-facing name:** `governed-coding-upgrade`  
**Version:** 1.2.0  
**Release state:** Proposed stable minor release pending PR review/merge  
**Canonical maintainer:** Chris Kulbaba (@chriskulbaba2025)  
**Copyright:** © 2026 Chris Kulbaba. All rights reserved.
