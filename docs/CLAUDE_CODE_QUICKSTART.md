# Using Governed Coding Upgrade with Claude Code

GCU is not Claude-specific, but Claude Code can use it as a reusable coding-governance skill.

This guide keeps the installation model simple:

```text
GCU protocol
+ persistent Claude Code invocation rule
+ repository Project Adapter
= governed Claude Code changes
```

## 1. Install the skill

Place the authoritative [`SKILL.md`](../SKILL.md) in the reusable skill location your Claude Code installation uses for the machine-facing skill name:

```text
governed-coding-upgrade
```

Keep the skill name stable even when the protocol version advances.

If your Claude Code setup supports repository-local skills, you may keep the skill in the repository instead. The important requirement is that Claude Code can read the authoritative current `SKILL.md` before editing.

## 2. Install the persistent invocation rule

Use [`GLOBAL_AGENT_RULE.md`](../GLOBAL_AGENT_RULE.md) as the canonical rule.

[`GLOBAL_CLAUDE_RULE.md`](../GLOBAL_CLAUDE_RULE.md) is a Claude Code compatibility version of the same obligation.

Put an equivalent instruction into the persistent/global instruction layer used by your Claude Code installation so qualifying coding work invokes GCU **before editing**.

Do not rely on remembering to mention GCU in every prompt.

## 3. Adapt the target repository

In each repository, create:

```text
.governance/PROJECT_ADAPTER.md
```

Start from [`../templates/PROJECT_ADAPTER_TEMPLATE.md`](../templates/PROJECT_ADAPTER_TEMPLATE.md).

The adapter records repository facts such as:

- components and roots;
- build and test commands;
- CI/release mechanisms;
- persistence/migration rules;
- protected/generated paths;
- auth/privacy/tenant boundaries;
- external-call policy;
- repository-specific stop conditions.

GCU is universal; the Project Adapter is where repository-specific truth lives.

## 4. Start a governed change

A useful Claude Code request is:

```text
Use governed-coding-upgrade for this change.
Preserve the requested outcome exactly.
Do Project Discovery first.
Do not edit until Requirement Preservation and the Surgical Change Determinacy Gate pass.
Show me the frozen surgical change contract before implementation if repository governance requires a human checkpoint.
Then implement only inside that boundary, verify it, run the Causal Necessity Audit, and report the exact-head result truthfully.
```

If the persistent invocation rule is installed correctly, explicitly naming GCU should be redundant, but it can be useful during adoption/testing.

## 5. What Claude Code must do before editing

Claude Code should establish:

```text
repository / branch / starting SHA
Project Adapter status
original requested outcome
faithful governed interpretation
change hypothesis and evidence
causal boundary
expected change surface
protected surface
structural change budget
acceptance proof
scope-expansion conditions
Change Tier
Release Intent
applicable Test Areas
```

Material unknowns remain `UNRESOLVED`.

## 6. What happens if Claude discovers more work

Claude must not silently absorb it.

The required behavior is:

```text
new boundary discovered
→ STOP before modifying it
→ record evidence
→ reopen determinacy
→ prove that boundary is causally required
→ update contract/budget
→ continue only after PASS
```

If the finding is useful but not required, record it separately and keep it out of the current change.

## 7. Audit independence

If the same Claude Code context performs Builder and Auditor work, label the audit:

```text
SELF_AUDIT
```

Switching to a stronger/different model inside the same Builder context does not automatically make the audit independent.

For higher-risk work, use a genuinely separate audit context when repository governance requires it.

## 8. Protected operations

GCU does not give Claude Code authority to merge, deploy, activate, spend against paid providers, change model-routing policy, or bypass approval controls.

Those actions remain subject to current user instruction and repository/control-plane authorization.

## 9. Expected final result

The final report should show, at minimum:

- preserved requirement;
- determinacy result;
- exact changed files/boundaries;
- Causal Necessity Audit result;
- verification evidence;
- exact final SHA;
- exact-head CI/machine-gate state when required;
- audit separation;
- Surgical Determinacy Audit;
- truthful final readiness state.
