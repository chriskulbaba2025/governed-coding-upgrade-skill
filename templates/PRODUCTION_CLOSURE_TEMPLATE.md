# Production Closure Template

Use this template when the goal is to finish a production-readiness correction, close all known defects on one production path, or continue until the path is clean.

```text
Read and obey the governed-coding-upgrade skill v1.2.0 before editing.
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

Before implementation:
1. Verify repository, branch, SHA, remote identity, and active PR.
2. Capture git status, diff stat, and complete diff.
3. Preserve valid active correction work; do not reset/stash merely to create a clean baseline.
4. Convert all known blockers on the same governed path into one frozen checklist.
5. Define exact permitted and prohibited files.
6. Define direct positive, negative, integration, persistence, lifecycle, and side-effect proof for every checklist ID.
7. Define the repository terminal machine-gate command or adopt the MACHINE_RELEASE_GATE_TEMPLATE.

MANDATORY SEQUENTIAL SECTION RULE

For every ordered section/checklist group:

INSPECT
→ DEFINE PROOF
→ REPRODUCE FAILURE when safe/feasible
→ IMPLEMENT COMPLETE SECTION
→ NARROW VERIFY
→ SECTION AUDIT
→ AUTO-CONTINUE ON PASS

For each section:
- inspect the existing real production path before editing;
- identify the exact defect and owning boundary;
- define the exact proof before implementation;
- implement the complete bounded section;
- run the narrowest executable proof for that section;
- verify required negative behavior and prohibited side effects;
- verify earlier passed sections that could be affected;
- mark SECTION PASS only from direct evidence;
- automatically continue when PASS;
- correct the same section before advancing when FAIL;
- stop only for a genuine governance, authorization, safety, or external blocker.

Do not run the entire regression suite after every section unless repository governance requires it.

BALANCED MACHINE CHECKS

Layer A — after each section:
- narrow unit/contract proof;
- required negative proof;
- exact state/artifact/call-count assertions.

Layer B — when a section crosses an already-passed boundary:
- affected integration checks only;
- rerun only earlier sections materially at risk.

Layer C — after all sections pass:
- cross-section integration review;
- full production acceptance;
- full regression;
- type/static/build/security checks where applicable;
- persistence/migration/recovery/idempotency checks where applicable;
- invariant checks;
- scope/diff check;
- complete diff inspection;
- terminal machine release gate.

Acceptance architecture:

real production adapter/service
+
injected controlled transport/client
+
production validator
+
real normalization/persistence/artifact boundary
+
real orchestrator/web/service path

Do not inject hand-written successful normalized results downstream as proof that production adapters work.

CONTROLLED EXTERNAL CALL SAFETY

- Controlled tests must not accidentally inherit real provider/LLM credentials when isolation is technically possible.
- Inject controlled transports/clients below production adapters.
- Unset, shadow, or sandbox real credentials for controlled acceptance processes.
- Fail if unexpected real network/provider execution occurs.
- Measure controlled and live call counts from the transport/client boundary.
- Never hardcode provider-call, LLM-call, or cost PASS assertions.
- If an accidental external call occurs, record it as an incident and rerun governed verification under isolated credentials.

Required proof classes where applicable:
- complete request/config persistence and exact round trip;
- source-specific contract validation;
- malformed AVAILABLE/PARTIAL/SUCCESS evidence fails closed;
- no fabricated unavailable/not-connected defaults;
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
- LIVE client/budget/retry controls using injected fake clients;
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

INTERRUPTION RESUME RULE

If the agent/API/terminal response is interrupted:
1. resume the same repository and branch;
2. inspect HEAD, working tree, task/checklist state, diff, and available test results;
3. determine the last section with direct PASS evidence;
4. preserve valid completed work;
5. resume from the first unproven/failing section;
6. do not restart the whole closure merely because the response connection ended.

CROSS-SECTION REVIEW

After all sections pass, inspect each dependency edge:
upstream governed output → downstream consumer.
Confirm downstream code consumes the exact validated upstream result and does not bypass validation or mutate it after proof.

If a cross-section defect is found, correct the owning section, rerun its narrow proof and affected later sections, then repeat cross-section review.

TERMINAL MACHINE RELEASE GATE

Preferred command:
change:release-gate
or repository-native equivalent.

The agent may not output final governed PASS/RELEASE READY unless the required gate exits 0.
Local substitutes, prose explanations, confidence, and environmental exceptions cannot override a failed required gate.

If mandatory exact-head CI is temporarily unavailable but all local controlled code verification passes:
report CODE VERIFIED / GOVERNANCE HOLD.
Do not call it final governed PASS.
When CI becomes available, run it against the unchanged exact SHA and rerun the terminal gate.

Continue the same production-closure objective until:
1. every repository-controlled checklist ID is PASS; and
2. terminal release conditions are satisfied; or
3. a genuine external blocker/hold is proved.

A genuine external blocker is outside repository control and cannot be simulated through a controlled dependency, such as unavailable account authorization, explicitly prohibited destructive production action, mandatory external CI/platform capability currently unavailable, or withheld merge/deployment authorization.

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
Skill version: 1.2.0
Starting SHA:
Final SHA:
Branch:
PR:
Exact files changed:
Sequential section results:
Cross-section review:
Persistence/migrations:
Production adapter/service proof:
Negative proofs:
Recovery/restart proof:
Idempotency/retry proof:
Abort proof:
Renderer/output proof:
Publication/web proof:
Controlled provider calls:
Live provider calls:
Controlled model calls:
Live LLM calls:
Measured cost:
Full regression:
Acceptance:
Scope check:
Terminal machine release gate command + exit:
Exact-head CI:
Independent exact-head audit:
Git status:
PR state:
Final status: CODE VERIFIED / STAGING CANDIDATE / GOVERNANCE HOLD / RELEASE READY / BLOCKED

Do not return RELEASE READY while any required checklist, machine gate, exact-head CI, or independent audit condition is open or failing.
```
