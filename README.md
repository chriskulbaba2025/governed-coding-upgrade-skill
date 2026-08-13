<p align="center">
  <img src="branding/logo.svg" alt="Governed Coding Upgrade" width="760">
</p>

<p align="center">
  <strong>A deterministic governance and production-readiness protocol for AI-assisted software changes.</strong><br>
  Production spine. Contract mapping. Proof-first acceptance. Sequential evidence. Terminal-path verification. Exact-head audit.
</p>

<p align="center">
  <code>v2.1.0 — Production Spine + Sequential Evidence</code> · <strong>100/100 semantic quality score</strong> · <strong>All 5 areas 20/20</strong>
</p>

> **Official canonical repository.** Maintained and controlled by **Chris Kulbaba (@chriskulbaba2025)**. Public forks and derivatives are not official releases.

# Governed Coding Upgrade v2.1.0 — Production Spine + Sequential Evidence

**Governed Coding Upgrade (GCU)** is a project-agnostic execution skill for coding agents and engineering teams. v2.1 combines the strongest operational controls from v1.2 with the production-correctness controls developed in the v2 line.

The machine-facing skill name remains `governed-coding-upgrade`.

## Why v2.1 exists

v1.2 was strong at *how work progresses*: sequential evidence gates, balanced verification, interruption resume, Production Closure, machine release gating, and Governance Hold.

The v2 production model strengthened *what must be proven across the real system*: production-spine tracing, Producer → Contract → Consumer mapping, acceptance freeze, false-PASS detection, validated-object continuity, terminal-path proof, and full-system production-readiness separation.

v2.1 unifies both.

## What v2.1 adds

- **Release intent:** `CHANGE_ONLY`, `STAGING_READY`, or `PRODUCTION_READY` before implementation.
- **Production Spine gate:** trace the real entry → persistence/jobs/services → transformation/rendering → publication/delivery → final retrieval path.
- **Producer → Contract → Consumer map:** prove every material handoff produces and validates what the downstream consumer actually requires.
- **Acceptance contract freeze:** define the real production modules, controlled dependency seam, positive/negative assertions, prohibited side effects, and external-call ceiling before production implementation.
- **False-PASS scan:** reject unconditional assertions, always-valid validators, fabricated normalized success, pre-seeded terminal states, hardcoded call/cost claims, and mocks above the production boundary under proof.
- **Single validated-object rule:** complete object → validate → retain/freeze → persist/transition/consume.
- **Evidence preservation:** raw evidence remains traceable through production normalization, validation, canonical persistence, and downstream consumption.
- **External-call contract:** task IDs, retries, timeouts, cancellation, recovery, reuse, duplicate-work prevention, and call/cost ceilings are explicit when applicable.
- **Durable-job contract:** asynchronous work must survive a fresh-process restart from persisted identity/config/checkpoint state.
- **Terminal-path gate:** intermediate states are not completion when publication, retrieval, authorization, or delivery still remains.
- **Full-system production-readiness gate:** scoped PASS is separated from system readiness.
- **Escaped-proof regression:** fix both the production defect and the proof system that allowed it through.
- **Vertical-spine rule:** new applications prove one real end-to-end slice before expanding horizontally.

## Retained from v1.2

- Sequential Evidence Gates.
- Dirty-tree continuation.
- Interrupted-session resume.
- Balanced narrow/affected/terminal verification.
- Production Closure Mode.
- Repository-owned-work classification.
- Controlled external-call isolation.
- Terminal machine release gate.
- `CODE VERIFIED / GOVERNANCE HOLD`.

## Governed lifecycle

```text
INTAKE
→ PREFLIGHT
→ RELEASE INTENT
→ PRODUCTION SPINE / CONTRACT MAP when applicable
→ ACCEPTANCE FREEZE
→ FROZEN CHECKLIST
→ SEQUENTIAL EVIDENCE GATES
→ CROSS-SECTION REVIEW
→ TERMINAL-PATH / FULL-SYSTEM READINESS when applicable
→ MACHINE RELEASE GATE
→ EXACT-HEAD AUDIT
→ CORRECTION / RE-AUDIT
→ CLOSE
```

## Core rule

> A coding change is not complete because an agent says it is complete. It is complete when governed requirements are directly proven at the exact candidate head, and a production-ready claim additionally proves the real terminal path and applicable full-system responsibilities.

## Repository structure

| Path | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | Authoritative v2.1.0 execution skill |
| [`GLOBAL_CLAUDE_RULE.md`](GLOBAL_CLAUDE_RULE.md) | Mandatory invocation rule |
| [`SCORECARD.md`](SCORECARD.md) | Five-area semantic quality assessment |
| [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | Control architecture |
| [`docs/ADOPTION_GUIDE.md`](docs/ADOPTION_GUIDE.md) | Adoption procedure |
| [`templates/PRODUCTION_SPINE_TEMPLATE.md`](templates/PRODUCTION_SPINE_TEMPLATE.md) | Production-spine and contract-map record |
| [`templates/ACCEPTANCE_CONTRACT_TEMPLATE.md`](templates/ACCEPTANCE_CONTRACT_TEMPLATE.md) | Proof-first acceptance freeze |
| [`templates/PRODUCTION_CLOSURE_TEMPLATE.md`](templates/PRODUCTION_CLOSURE_TEMPLATE.md) | Full production-closure prompt |
| [`templates/MACHINE_RELEASE_GATE_TEMPLATE.md`](templates/MACHINE_RELEASE_GATE_TEMPLATE.md) | Terminal machine-gate contract |
| [`templates/`](templates/) | Profile, checklist, audit, correction, and final-report templates |
| [`scripts/validate-package.py`](scripts/validate-package.py) | Package integrity validator |
| [`.github/`](.github/) | Repository governance and CI |

## Installation

1. Install `SKILL.md` in the reusable skill location under `governed-coding-upgrade`.
2. Add `GLOBAL_CLAUDE_RULE.md` to the coding-agent global instruction layer.
3. Create/update `.governance/GOVERNED_CHANGE_PROFILE.md` using the profile template.
4. Populate v2.1 fields for release intent, production spine, contract map, acceptance freeze, false-PASS scan, terminal promise, system-readiness method, machine gate, and exact-head CI.
5. Use the production-spine and acceptance templates for cross-boundary or production-readiness work.

See [`docs/ADOPTION_GUIDE.md`](docs/ADOPTION_GUIDE.md).

## Proof model

Strong proof includes exact assertions, lifecycle/state history, persisted round trips, artifacts/hashes, production modules with controlled dependencies, call/task counters, restart/recovery evidence, object equality/identity where governed, exact changed-file scope, exact final SHA, exact-head CI, machine-gate result, terminal retrieval, and independent audit.

Weak proof includes prose, confidence, test names, comments, fabricated success objects, hardcoded call counts, or green CI by itself.

## Semantic quality

| Area | Score |
|---|---:|
| Governance & Control | **20/20** |
| Execution Process & Determinism | **20/20** |
| Testing, Evidence & Audit Quality | **20/20** |
| Automation & Delivery Efficiency | **20/20** |
| Generalizability & Portability | **20/20** |
| **Total** | **100/100** |

## Versioning

Semantic versioning applies to the protocol artifact. The machine-facing identifier remains stable across compatible installations; the human-visible version and profile obligations may advance.

**Display name:** Governed Coding Upgrade v2.1.0 — Production Spine + Sequential Evidence  
**Machine-facing name:** `governed-coding-upgrade`  
**Version:** 2.1.0  
**Canonical maintainer:** Chris Kulbaba (@chriskulbaba2025)  
**Copyright:** © 2026 Chris Kulbaba. All rights reserved.
