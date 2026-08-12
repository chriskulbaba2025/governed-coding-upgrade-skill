# Governed Coding Upgrade Skill — Semantic Quality Scorecard

**Version evaluated:** 1.1.0  
**Release name:** Governed Coding Upgrade v1.1.0 — Production Closure  
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
- genuine external-blocker protocol;
- binary PASS/BLOCKED outcomes.

**Reason for score:** The control model covers ordinary governed changes and production-closure work without allowing repository-owned implementation gaps to be relabeled as completion blockers.

## 2. Execution Process & Determinism — 20/20

**Evidence in the skill:**
- deterministic standard lifecycle;
- dedicated Production Closure Mode;
- stable checklist IDs;
- exact observable behavior language;
- one production-path closure package;
- proof-first implementation order;
- real production path acceptance with controlled dependencies;
- deterministic correction and exact-head re-audit;
- durability, restart, retry, idempotency, and abort extensions when applicable.

**Reason for score:** The skill defines a complete execution state machine while allowing repository-specific commands and architecture to remain in the Governed Change Profile.

## 3. Testing, Evidence & Audit Quality — 20/20

**Evidence in the skill:**
- direct-proof requirement;
- validation-before-transition rule;
- complete-object validation before rendering/publication/exposure;
- negative-path/fail-closed proof including persisted state and prohibited side effects;
- production adapter/service testing with injected controlled transports;
- permanent regression rule;
- exact call-count/idempotency proof;
- restart/resume proof;
- independent exact-head audit;
- re-audit after correction.

**Reason for score:** Completion cannot be supported by prose, fabricated normalized success objects, confidence, test names, or CI alone. Runtime behavior and repository state must be proven through the real governed implementation boundary.

## 4. Automation & Delivery Efficiency — 19/20

**Evidence in the skill:**
- reusable Governed Change Profile reduces rediscovery;
- stable command responsibility interface;
- production-closure template reduces repeated prompt reconstruction;
- repository-owned blocker classification prevents repeated discovery-only handoffs;
- repeatable checks are targeted for automation;
- WIP limits and bounded prompts;
- cycle-time and first-pass metrics;
- default ≥55% cycle-time reduction target without weakening acceptance quality.

**Why not 20:** The skill defines stronger reusable automation and closure contracts, but repository-specific verification commands still must be implemented in each adopting repository.

## 5. Generalizability & Portability — 20/20

**Evidence in the skill:**
- stable machine-facing identifier across compatible versions;
- no product-specific repository path, package manager, CI vendor, language, framework, or provider is mandatory;
- project adapter/profile layer holds repository-specific facts;
- production closure describes generic boundary classes rather than Prysm-specific components;
- N/A handling requires evidence;
- ordinary and production-closure change modes remain project-agnostic.

**Reason for score:** The production-closure capability applies to web applications, APIs, background workers, data systems, provider integrations, report pipelines, infrastructure, and other governed software paths without encoding a single product architecture.

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

**Versioning note:** v1.1.0 is a backward-compatible minor release. The machine-facing skill name remains `governed-coding-upgrade`; the human-visible release title carries the version and Production Closure designation.
