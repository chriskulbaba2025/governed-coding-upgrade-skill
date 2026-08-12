# Adoption Guide

## Objective

Install Governed Coding Upgrade v1.2.0 so qualifying coding changes use the same governance lifecycle while each repository retains its own commands, invariants, CI, and release controls.

## 1. Install the skill

Place `SKILL.md` in the coding agent's reusable skill location under:

```text
governed-coding-upgrade
```

The agent must load the file as an authoritative execution skill rather than optional reference material.

## 2. Install the global invocation rule

Add the contents of `GLOBAL_CLAUDE_RULE.md` to the global coding-agent instruction layer.

This is required because an available skill is not equivalent to a mandatory skill.

## 3. Create or upgrade the repository profile

In each governed codebase, create or update:

```text
.governance/GOVERNED_CHANGE_PROFILE.md
```

Use [`../templates/GOVERNED_CHANGE_PROFILE_TEMPLATE.md`](../templates/GOVERNED_CHANGE_PROFILE_TEMPLATE.md).

For v1.2.0, explicitly populate:

- narrow-test command;
- affected-integration command;
- acceptance/integration command;
- full-regression command;
- controlled-test credential isolation policy;
- unexpected live-network behavior;
- controlled/live call-counter source;
- terminal machine release-gate command;
- exact-head CI verification method.

Mark unknown fields `UNRESOLVED` rather than inferring them.

## 4. Establish protected invariants

Record repository behaviors and artifacts that a change must not alter unless explicitly authorized. Examples:

- public APIs and schemas;
- data isolation;
- lifecycle/state transitions;
- authentication and authorization;
- migrations;
- golden masters or snapshots;
- generated output;
- dependency compatibility;
- external/paid provider restrictions;
- deployment and rollback rules.

## 5. Adopt Sequential Evidence Gates

For changes with multiple ordered boundaries, group checklist IDs into sections and execute:

```text
inspect
→ define proof
→ reproduce failure when safe/feasible
→ implement
→ narrow verify
→ section audit
→ automatically continue on PASS
```

Do not proceed past a failed section.

Do not require routine user approval between passed sections unless the next action crosses an explicit authorization boundary such as live provider execution, production mutation, deployment, merge, or release.

## 6. Adopt balanced verification

Do not default to a full regression after every section.

Configure three levels:

1. **Narrow section proof** after each section.
2. **Affected integration proof** only when a changed boundary can invalidate earlier passed behavior.
3. **Full terminal verification** after all sections and cross-section review pass.

This is the default v1.2.0 balance between cycle time and release confidence.

## 7. Isolate controlled tests from real credentials

Where external providers/models exist:

- inject deterministic controlled transports or clients below real production adapters;
- unset, shadow, or sandbox real credentials for controlled acceptance when feasible;
- fail unexpected live network/provider execution;
- record actual controlled/live call counters;
- do not hardcode zero-call or zero-cost PASS results.

## 8. Add the terminal machine release gate

Use [`../templates/MACHINE_RELEASE_GATE_TEMPLATE.md`](../templates/MACHINE_RELEASE_GATE_TEMPLATE.md).

Implement one stable repository command, preferably:

```text
change:release-gate
```

or a repository-native equivalent.

The command should exit `0` only when every machine-enforceable mandatory release condition is satisfied at the exact candidate head.

When exact-head CI is mandatory but temporarily unavailable, the gate must not silently accept local substitution. The correct disposition is:

```text
CODE VERIFIED / GOVERNANCE HOLD
```

Rerun the external proof and gate against the unchanged exact SHA when available.

## 9. Verify and audit

Run repository-specific terminal verification from the Governed Change Profile, then use [`../templates/INDEPENDENT_AUDIT_TEMPLATE.md`](../templates/INDEPENDENT_AUDIT_TEMPLATE.md) against the exact final head.

If audit blocks the change, compile a bounded correction, rerun the owning section and affected later sections, then run terminal verification and audit the corrected exact head.

## 10. Recover interrupted agent sessions

After an API/agent/terminal interruption:

1. reopen the same repository and branch;
2. inspect HEAD, working tree, diff, checklist/task state, and test evidence;
3. identify the last directly proven section;
4. resume from the first unproven or failed section;
5. do not restart completed valid work solely because the conversational response ended.

## 11. Close with evidence

Use [`../templates/FINAL_REPORT_TEMPLATE.md`](../templates/FINAL_REPORT_TEMPLATE.md).

Do not replace missing proof with confidence language or prose assertions.

## Repository-level acceptance

v1.2.0 adoption is complete when:

- the skill is installed;
- the global invocation rule is active;
- the repository profile contains no material guessed facts;
- protected invariants are registered;
- sequential section checks map to executable commands;
- affected integration verification is defined;
- controlled credential/live-call policy is defined where applicable;
- full terminal verification is executable;
- the machine release gate is implemented;
- exact-head audit can be performed;
- merge/release authorization remains explicit.
