# Mandatory Global Invocation Rule

Add this rule to the global coding-agent instruction layer so the skill is invoked consistently rather than merely being available:

```text
MANDATORY GOVERNED CODING CHANGES

For every task that changes code, tests, schemas, dependencies, executable
configuration, infrastructure-as-code, build/release logic, migrations, or
runtime behavior, invoke and obey the `governed-coding-upgrade` skill before
editing.

Do not bypass the skill because a change appears small.
Do not begin implementation until repository preflight, protected invariants,
permitted/prohibited file scope, and the frozen checklist are established.
Do not claim completion until direct proof, applicable verification, scope
check, complete diff review, and an independent exact-head audit all PASS.
Do not merge, deploy, release, or activate anything without the authorization
required by the repository and the current user instruction.
```
