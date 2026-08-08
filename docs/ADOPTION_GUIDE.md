# Adoption Guide

## Objective

Install Governed Coding Upgrade so every qualifying coding change uses the same governance lifecycle while each repository retains its own commands and protected invariants.

## 1. Install the skill

Place `SKILL.md` in the coding agent's reusable skill location under the skill name:

```text
governed-coding-upgrade
```

The agent must load the file as an authoritative execution skill rather than as optional reference material.

## 2. Install the global invocation rule

Add the contents of `GLOBAL_CLAUDE_RULE.md` to the global coding-agent instruction layer.

This is required because an available skill is not equivalent to a mandatory skill. The invocation rule makes qualifying code changes route through the governed lifecycle.

## 3. Create the repository profile

In each governed codebase, create:

```text
.governance/GOVERNED_CHANGE_PROFILE.md
```

Use [`../templates/GOVERNED_CHANGE_PROFILE_TEMPLATE.md`](../templates/GOVERNED_CHANGE_PROFILE_TEMPLATE.md).

Populate fields from verified repository state. Mark unknown fields `UNRESOLVED` rather than inferring them.

## 4. Establish protected invariants

Record the repository behaviors and artifacts that a change must not alter unless explicitly authorized. Examples:

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

## 5. Start each change with a frozen checklist

Use [`../templates/CHANGE_CHECKLIST_TEMPLATE.md`](../templates/CHANGE_CHECKLIST_TEMPLATE.md).

Every checklist item needs one behavior or condition, one stable ID, one implementation boundary, and direct proof.

## 6. Verify and audit

Run repository-specific verification from the Governed Change Profile. Then use [`../templates/INDEPENDENT_AUDIT_TEMPLATE.md`](../templates/INDEPENDENT_AUDIT_TEMPLATE.md) against the exact final head.

If audit blocks the change, compile a single correction package using [`../templates/CORRECTION_TEMPLATE.md`](../templates/CORRECTION_TEMPLATE.md), re-run verification, and audit the corrected exact head.

## 7. Close with evidence

Use [`../templates/FINAL_REPORT_TEMPLATE.md`](../templates/FINAL_REPORT_TEMPLATE.md). Do not replace missing proof with confidence language or prose assertions.

## Repository-level acceptance

Adoption is complete when:

- the skill is installed;
- the global invocation rule is active;
- the repository profile exists and contains no material guessed facts;
- protected invariants are registered;
- verification responsibilities map to executable commands;
- exact-head audit can be performed;
- merge/release authorization remains explicit.
