<p align="center">
  <img src="branding/logo.svg" alt="Governed Coding Upgrade" width="760">
</p>

<p align="center">
  <strong>A deterministic governance and production-closure protocol for AI-assisted software changes.</strong><br>
  Frozen scope. Real-path proof. Fail-closed verification. Exact-head audit. Evidence-based release.
</p>

<p align="center">
  <code>v1.1.0 — Production Closure</code> · <strong>99/100 semantic quality score</strong> · <strong>All 5 areas ≥19/20</strong>
</p>

> **Official canonical repository.** This repository is maintained and controlled by **Chris Kulbaba (@chriskulbaba2025)**. Public forks and derivative copies are not official releases and cannot represent themselves as the canonical Governed Coding Upgrade repository.

---

# Governed Coding Upgrade v1.1.0 — Production Closure

**Governed Coding Upgrade (GCU)** is a project-agnostic execution skill for coding agents and engineering teams. It converts software changes from an informal edit/test loop into a controlled lifecycle with explicit scope, checklist IDs, direct evidence, deterministic verification, independent exact-head audit, governed correction, and release authorization.

Version 1.1.0 adds **Production Closure Mode** for the failure pattern where repeated audits identify more repository-owned infrastructure and the coding loop keeps ending with another partial report. Production closure turns the complete governed production path into one acceptance package and requires the agent to continue implementing repository-controlled dependencies until the path passes or a genuine external blocker remains.

The machine-facing skill name remains `governed-coding-upgrade` so existing installations and invocation rules do not break when upgrading from v1.0.0.

## What v1.1.0 adds

- **Production Closure Mode** for end-to-end production-readiness correction.
- **Repository-owned blocker classification:** migrations, tables, validators, queues, caches, endpoints, transport abstractions, recovery harnesses, and negative proofs are implementation work when already required by the governed production contract.
- **Dirty-tree continuation:** active correction work is captured, mapped, preserved, and corrected rather than reset solely to create a clean baseline.
- **Real production path acceptance:** production adapters/services run with injected controlled transports instead of fabricated downstream success objects.
- **Validation-before-transition:** complete objects are validated before persistence, lifecycle advancement, rendering, publication, or exposure.
- **Durability and recovery proof:** restart/resume, completed-step call counts, retry classification, paid-task idempotency, and abort propagation are first-class closure responsibilities when applicable.
- **Keep-going correction:** production closure continues through repository-controlled failures after governed process review instead of handing ordinary infrastructure gaps back as a new discovery report.
- **Reusable production-closure template** under [`templates/PRODUCTION_CLOSURE_TEMPLATE.md`](templates/PRODUCTION_CLOSURE_TEMPLATE.md).

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

### Production Closure Mode

```text
INTAKE
  ↓
PREFLIGHT
  ↓
ONE PRODUCTION-CLOSURE CHECKLIST
  ↓
PROVE FAILURES
  ↓
IMPLEMENT REPOSITORY-OWNED DEPENDENCIES
  ↓
REAL-PATH ACCEPTANCE
  ↓
FULL REGRESSION
  ↓
INDEPENDENT EXACT-HEAD AUDIT
  ↓
CONSOLIDATED CORRECTION
  ↓
RE-AUDIT
  ↓
PASS OR GENUINE EXTERNAL BLOCKER
```

## Non-negotiable controls

- Scope is explicit before implementation.
- Every checklist item has a stable ID and direct proof.
- Permitted and prohibited files are explicit.
- Protected invariants are identified before editing.
- Completion requires executable evidence rather than prose or confidence.
- Acceptance executes the real production implementation with controlled dependencies.
- Negative paths prove persisted state and prohibited side effects, not only thrown exceptions.
- Repository-owned missing infrastructure is not relabeled as a final blocker during production closure.
- CI and audit correspond to the exact final head.
- The implementation cannot authorize its own release.
- Merge, deploy, release, activation, and live paid calls remain subject to explicit authorization.

## Repository structure

| Path | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | Authoritative Governed Coding Upgrade v1.1.0 skill |
| [`GLOBAL_CLAUDE_RULE.md`](GLOBAL_CLAUDE_RULE.md) | Mandatory global invocation rule |
| [`SCORECARD.md`](SCORECARD.md) | Five-area semantic quality assessment |
| [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | Control model, gates, roles, and project adapter architecture |
| [`docs/ADOPTION_GUIDE.md`](docs/ADOPTION_GUIDE.md) | Installation and repository onboarding procedure |
| [`templates/PRODUCTION_CLOSURE_TEMPLATE.md`](templates/PRODUCTION_CLOSURE_TEMPLATE.md) | Reusable full production-closure execution prompt |
| [`templates/`](templates/) | Profile, checklist, audit, correction, and final-report templates |
| [`.github/`](.github/) | Pull-request, issue, security, ownership, and CI governance |
| [`scripts/validate-package.py`](scripts/validate-package.py) | Zero-dependency package integrity validator |
| [`branding/`](branding/) | Repository logo, icon, and social-card assets |

## Installation model

GCU has two layers:

1. **Execution skill** — install `SKILL.md` wherever the coding agent loads reusable skills.
2. **Mandatory invocation rule** — add `GLOBAL_CLAUDE_RULE.md` to the global instruction layer so qualifying coding changes cannot silently bypass the skill.

Each codebase supplies repository-specific facts through a **Governed Change Profile**. The profile maps the universal protocol to the repository's actual commands, CI, protected invariants, migration rules, external-call rules, persistence/recovery conventions, rollback mechanism, and release controls.

Start with [`docs/ADOPTION_GUIDE.md`](docs/ADOPTION_GUIDE.md).

## Production Closure Mode

Activate Production Closure Mode when the request is materially equivalent to:

- finish the production-readiness correction;
- fix all known blockers and verify the complete path;
- continue until all governed defects are clean;
- stop returning partial audits and make the system work.

The root rule is simple:

> If a missing component is repository-owned and required by an already-governed production contract, it is implementation work. It is not a final blocker merely because it requires infrastructure.

A valid final blocker must be genuinely external or explicitly prohibited, such as unavailable third-party authorization or withheld deployment/merge permission.

## Proof model

A completion claim is valid only when the relevant evidence is inspectable. Examples include:

- exact test assertions;
- exact lifecycle/state history;
- persisted state and round-trip values;
- stored artifacts and hashes;
- provider/adapter call counts;
- retry and duplicate-task counts;
- abort/cancellation side-effect counts;
- restart/resume proof;
- exact changed-file list;
- exact final SHA;
- CI tied to that SHA;
- independent audit result.

Test names, comments, green CI by itself, prose claims, manually constructed success objects, and confidence percentages are not substitutes for governed proof.

## Semantic quality gate

Version 1.1.0 preserves the five-area quality threshold used by the project.

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

Version 1.1.0 is a minor release because Production Closure Mode adds capability while preserving the stable `governed-coding-upgrade` invocation name.

## Maintainer authority

The canonical repository, protected branches, releases, tags, and official version designations are controlled by the repository maintainer. Contributions may be proposed through pull requests, but no external contributor is granted write or release authority by default. See [`MAINTAINERS.md`](MAINTAINERS.md).

## Design principle

> A coding change is not complete because an agent says it is complete. It is complete when governed requirements are satisfied by direct evidence at the exact release-candidate head and the required independent audit passes.

## Status

**Display name:** Governed Coding Upgrade v1.1.0 — Production Closure  
**Machine-facing name:** `governed-coding-upgrade`  
**Version:** 1.1.0  
**Release state:** Proposed stable minor release pending PR review/merge  
**Canonical maintainer:** Chris Kulbaba (@chriskulbaba2025)  
**Copyright:** © 2026 Chris Kulbaba. All rights reserved.
