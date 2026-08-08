# Governed Coding Upgrade Skill — Semantic Quality Scorecard

**Version evaluated:** 1.0.0  
**Acceptance threshold:** Every semantic area must score **19/20 or higher**.

## 1. Governance & Control — 20/20

**Evidence in the skill:**
- explicit authority precedence;
- mandatory invocation boundary;
- verified repo/branch/SHA preflight;
- frozen scope;
- permitted/prohibited files;
- protected pre-existing work;
- stop conditions;
- explicit merge/release authorization;
- WIP limits;
- blocked protocol.

**Reason for score:** The control model is complete from intake through release and includes both code-scope governance and authorization governance.

## 2. Execution Process & Determinism — 20/20

**Evidence in the skill:**
- deterministic lifecycle: intake → preflight → profile → checklist → execution plan → build → verify → audit → correction → re-audit → close;
- stable checklist IDs;
- exact behavior language;
- one architectural boundary;
- strict scope-change protocol;
- exact assertions for order/count/identity;
- change-class extensions for defect, migration, dependency, security, performance, and refactor work.

**Reason for score:** The skill defines a complete execution state machine while allowing repository-specific command adaptation without allowing governance bypass.

## 3. Testing, Evidence & Audit Quality — 20/20

**Evidence in the skill:**
- direct-proof requirement;
- explicit valid/invalid evidence taxonomy;
- negative-path/fail-closed proof;
- protected-invariant checks;
- verification matrix;
- exact changed-file proof;
- permanent defect regression rule;
- independent exact-head audit;
- re-audit after correction;
- binary PASS/BLOCKED outcomes.

**Reason for score:** No completion state can be supported by prose, confidence, test names, or CI alone. Runtime behavior and repository state must be proven.

## 4. Automation & Delivery Efficiency — 19/20

**Evidence in the skill:**
- reusable Governed Change Profile prevents repeated rediscovery;
- repeatable checks are explicitly targeted for automation;
- stable command responsibility interface;
- bounded prompts compiled from frozen scope;
- consolidated corrections;
- WIP limits;
- cycle-time and first-pass metrics;
- default ≥55% cycle-time reduction target without weakening acceptance quality.

**Why not 20:** The skill defines the automation contract, but repository-specific automation commands cannot be considered implemented until the skill is installed and adapted inside each repository.

## 5. Generalizability & Portability — 20/20

**Evidence in the skill:**
- no project-specific product name, repository path, package manager, CI vendor, language, framework, or test runner is mandatory;
- project adapter/profile layer holds repository-specific facts;
- protected invariants are expressed as universal classes;
- N/A handling requires evidence rather than assumption;
- change classification covers the principal software-change modes;
- global invocation contract separates universal governance from repository configuration.

**Reason for score:** The same lifecycle applies across application code, APIs, data, infrastructure, dependencies, security, migrations, CI/build systems, and generated outputs without hard-coding Prysm-specific assumptions.

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
