# Mandatory Global Invocation Rule

Add this rule to the global coding-agent instruction layer so the skill is invoked consistently rather than merely being available:

```text
MANDATORY GOVERNED CODING CHANGES

For every task that changes code, tests, schemas, dependencies, executable
configuration, infrastructure-as-code, build/release logic, migrations,
persistence, or runtime behavior, invoke and obey the
`governed-coding-upgrade` skill before editing.

Do not bypass the skill because a change appears small.
Do not begin implementation until repository preflight, protected invariants,
permitted/prohibited file scope, and the frozen checklist are established.

When the user asks to finish a production-readiness correction, fix all known
blockers, make the complete path work, or continue until clean, activate the
skill's PRODUCTION_CLOSURE mode. Do not stop merely because an already-governed
requirement needs repository-owned infrastructure such as a migration, table,
durable worker, validator, transport abstraction, endpoint, cache, integration
harness, recovery test, or negative proof. Implement and prove repository-owned
requirements until all checklist IDs PASS or a genuine external blocker remains.

Acceptance must exercise the real production implementation with controlled
injected dependencies rather than fabricated downstream success objects.
Do not claim completion until direct proof, applicable verification, scope
check, complete diff review, and an independent exact-head audit all PASS.
Do not merge, deploy, release, activate, or make prohibited live paid/provider
calls without the authorization required by repository governance and the
current user instruction.
```
