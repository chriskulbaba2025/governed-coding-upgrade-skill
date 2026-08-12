# Production Closure Template

Use this template when the goal is to finish a production-readiness correction, close all known defects on one production path, or continue until the path is clean.

```text
Read and obey the governed-coding-upgrade skill v1.1.0 before editing.
Activate PRODUCTION_CLOSURE mode.

Repository:
<ROOT>

Branch:
<BRANCH>

PR:
<PR OR N/A>

Required starting SHA:
<SHA>

Current working-tree condition:
<CLEAN OR DESCRIBE ACTIVE CORRECTION CHANGES>

Governing sources:
- <SOURCE>

Objective:
Make <PRODUCTION PATH> satisfy <GOVERNING CONTRACTS> from <ENTRY BOUNDARY>
through <TERMINAL BOUNDARY>, and prove it with deterministic controlled tests.

Known production blockers:
- <BLOCKER>

Authorization locks:
- Live paid/provider calls: <ALLOWED/PROHIBITED>
- Live LLM calls: <ALLOWED/PROHIBITED>
- Production mutations: <ALLOWED/PROHIBITED>
- Deployment: <ALLOWED/PROHIBITED>
- Merge/release: <ALLOWED/PROHIBITED>

Required operating rule:
Do not stop after discovering a repository-owned missing component. A missing
schema, migration, table, durable worker, validator, transport abstraction,
retry identity, replay cache, endpoint, publication boundary, integration
harness, recovery test, or negative proof is implementation work when it is
required by an already-governed production-path contract.

Before new implementation:
1. Verify repo, branch, SHA, and remote identity.
2. Capture git status, diff stat, and complete diff.
3. Protect valid pre-existing work; do not reset/stash it merely to create a clean baseline.
4. Map all known blockers to one frozen production-closure checklist.
5. Define exact permitted and prohibited files.
6. Define positive, negative, integration, persistence, and lifecycle proof for each item.

Acceptance architecture:
Use the real production implementation with controlled dependencies:

real production adapter/service
+
injected controlled transport/client
+
production validator
+
real persistence/artifact boundary
+
real orchestrator/web/service path

Do not inject hand-written successful normalized results downstream as proof
that a production adapter works.

Required proof classes where applicable:
- complete request/config persistence and round trip;
- source-specific contract validation;
- malformed AVAILABLE/SUCCESS evidence fails closed;
- artifact integrity/provenance;
- validation before persistence/lifecycle advancement;
- finalization gate execution;
- complete validated render/view model before renderer;
- renderer receives exact validated model;
- durable job state;
- restart/recovery;
- completed steps do not repeat after recovery;
- retryable vs terminal failure classification;
- paid-task/request ID reuse across retries;
- duplicate paid-task prevention;
- AbortSignal/cancellation propagation;
- zero prohibited side effects after abort;
- deterministic MOCK/REPLAY execution;
- LIVE client/budget/retry controls using an injected fake client;
- publication/terminal lifecycle state;
- actual web/API path;
- draft/incomplete/unauthorized access rejection;
- permanent negative regression proofs.

Negative proof pattern:
operation rejects
AND
persisted state equals governed failure state
AND
prohibited later events do not exist
AND
prohibited later calls equal zero
AND
prohibited artifacts/writes do not exist

Implementation loop:
inspect
→ prove failure
→ implement
→ narrow verify
→ integrated verify
→ full regression
→ scope/diff check
→ commit/push under repository governance
→ independent exact-head audit
→ consolidated correction for failed IDs
→ re-verify
→ re-audit

Continue the same production-closure objective until:
1. every required checklist ID is PASS; or
2. a genuine external blocker is proved.

A valid final external blocker must be outside repository control and unable to
be simulated through a controlled dependency, such as unavailable account
authorization, explicitly prohibited destructive production action, or withheld
merge/deployment authorization.

Do not use these as final blockers when repository-owned:
requires DB migration
requires a new table
requires durable job execution
requires source-specific schema
requires transport abstraction
requires endpoint
requires cache
requires model-client interface
requires budget gate
requires integration harness
requires recovery test
requires negative proof

Do not merge, deploy, release, or make prohibited live calls.

Final report:
PRODUCTION CLOSURE REPORT
Starting SHA:
Final SHA:
Branch:
PR:
Exact files changed:
Checklist evidence:
Persistence/migrations:
Production adapter/service proof:
Negative proofs:
Recovery/restart proof:
Idempotency/retry proof:
Abort proof:
Renderer/output proof:
Publication/web proof:
Full regression:
Acceptance:
Exact-head CI:
Independent exact-head audit:
Live provider calls:
Live LLM calls:
Paid calls:
Production mutations:
Git status:
Ready for authorized merge/release: YES/NO
Final: PASS/BLOCKED

Do not return PASS while any required checklist item is open or failing.
```
