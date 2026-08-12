# Governed Coding Upgrade Skill — Semantic Quality Scorecard

**Version evaluated:** 1.2.0  
**Release name:** Governed Coding Upgrade v1.2.0 — Sequential Evidence Gates  
**Acceptance threshold:** Every semantic area must score **19/20 or higher**.

## 1. Governance & Control — 20/20

**Evidence in the skill:**
- explicit authority precedence;
- mandatory invocation boundary;
- verified repo/branch/SHA preflight;
- frozen scope and checklist IDs;
- permitted/prohibited files;
- protected pre-existing work and dirty-tree continuation;
- explicit merge/deploy/release authorization;
- production-closure blocker classification;
- terminal machine release gate that agent prose cannot override;
- explicit `GOVERNANCE HOLD` state for mandatory external release evidence that is temporarily unavailable;
- binary section PASS and governed terminal states.

**Reason for score:** The control model prevents repository-owned implementation gaps, agent interpretation, and temporary external CI outages from being mislabeled as final governed PASS.

## 2. Execution Process & Determinism — 20/20

**Evidence in the skill:**
- deterministic standard lifecycle;
- dedicated Production Closure Mode;
- Sequential Evidence Gate for ordered sections;
- stable checklist IDs;
- proof-first section execution;
- automatic continuation after direct section PASS;
- interrupted-session resume from repository evidence;
- balanced narrow/affected/full verification cadence;
- cross-section integration review;
- deterministic correction and exact-head re-audit;
- durability, restart, retry, idempotency, and abort extensions when applicable.

**Reason for score:** v1.2.0 adds a deterministic inner loop for large closure work while preserving the outer exact-head release lifecycle.

## 3. Testing, Evidence & Audit Quality — 20/20

**Evidence in the skill:**
- direct-proof requirement;
- real production path acceptance with injected controlled transports;
- validation-before-transition rule;
- complete-object validation before persistence/render/publication;
- negative-path/fail-closed proof including persisted state and prohibited side effects;
- credential isolation and unexpected-live-call failure guidance;
- measured controlled/live call counters rather than hardcoded PASS;
- restart/resume proof;
- cross-section validation of upstream/downstream contracts;
- independent exact-head audit;
- terminal release-gate evidence.

**Reason for score:** Completion cannot be supported by prose, fabricated success objects, hardcoded call counts, confidence, test names, or local substitutes for mandatory exact-head evidence.

## 4. Automation & Delivery Efficiency — 19/20

**Evidence in the skill:**
- reusable Governed Change Profile reduces rediscovery;
- sequential section gates reduce late defect accumulation;
- narrow checks run at section boundaries instead of full regression after every step;
- affected integration checks rerun only materially dependent boundaries;
- terminal machine release gate consolidates final decision evidence;
- interruption resume preserves completed work;
- production-closure and machine-gate templates reduce prompt reconstruction;
- cycle-time and first-pass metrics;
- default ≥55% cycle-time reduction target without weakening acceptance quality.

**Why not 20:** The protocol defines the machine-gate responsibility, but each adopting repository must still implement its repository-specific executable release command and CI integration.

## 5. Generalizability & Portability — 20/20

**Evidence in the skill:**
- stable machine-facing identifier across compatible versions;
- no product-specific path, package manager, CI vendor, language, framework, or provider is mandatory;
- Governed Change Profile holds repository-specific commands;
- sequential gates and release-gate responsibilities are expressed generically;
- controlled credential rules apply to provider, model, and other network integrations;
- N/A handling requires evidence;
- ordinary and production-closure modes remain project-agnostic.

**Reason for score:** The v1.2.0 controls apply to web apps, APIs, workers, provider integrations, report pipelines, data systems, infrastructure, and other governed software without encoding Prysm-specific architecture.

---

# Final score

| Semantic area | Score |
|---|---:|
| Governance & Control | **20/20** |
| Execution Process & Determinism | **20/20** |
| Testing, Evidence & Audit Quality | **20/20** |
| Automation & Delivery Efficiency | **19/20** |
| Generalizability & Portability | **20/20** |
| **Total** | **99/100 (19.8/20 average)** |

**Threshold result:** PASS — all five semantic areas are ≥19/20.

**Versioning note:** v1.2.0 is a backward-compatible minor release. The machine-facing skill name remains `governed-coding-upgrade`; the human-visible release title carries the Sequential Evidence Gates designation.
