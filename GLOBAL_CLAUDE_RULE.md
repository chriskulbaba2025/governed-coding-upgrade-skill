# Claude Code — Mandatory GCU Invocation Rule

`GLOBAL_CLAUDE_RULE.md` is retained for backward compatibility with existing Claude Code installations.

The canonical vendor-neutral instruction is [`GLOBAL_AGENT_RULE.md`](GLOBAL_AGENT_RULE.md). Claude Code installations should enforce an equivalent rule in their persistent instruction layer and load the authoritative [`SKILL.md`](SKILL.md) before qualifying edits.

## Claude Code rule

```text
For every qualifying coding change, invoke and obey `governed-coding-upgrade` before
editing. Read the authoritative SKILL.md and the repository Project Adapter/governed
profile.

Run Project Discovery. Preserve the original requested requirement. Before editing,
pass the Surgical Change Determinacy Gate by freezing the required outcome, evidence,
change hypothesis, causal boundary, expected change surface, protected surface,
structural change budget, acceptance proof, and expansion conditions.

Discovery does not create authorization. Incidental defects, refactors, cleanup,
hardening, dependency changes, renames, reorganization, and adjacent features stay out
of the active change unless direct evidence proves they are causally required for the
frozen outcome.

If implementation needs a boundary outside the frozen contract, STOP and reopen the
Surgical Change Determinacy Gate. Never broaden scope automatically. The change budget
measures architectural surface, not line count or arbitrary diff size.

Classify Change Tier as T1_LOCAL, T2_BOUNDARY, T3_SYSTEM, or T4_RELEASE. Declare
Release Intent as CHANGE_ONLY, STAGING_READY, or PRODUCTION_READY. Select applicable
Test Areas and do not convert unknowns to N/A.

Use Production Spine and Producer → Contract → Consumer mapping where applicable.
Freeze acceptance and reject false-PASS proof. Use the Sequential Evidence Gate for
ordered work and a Challenger gate before terminal acceptance for T2+ work.

When an external execution control plane is present, obey `gcu-execution-control/1.0.0`.
GCU must not choose concrete providers/models, store provider credentials, silently
escalate, duplicate the usage ledger, or model-dispatch Release Authority. Preserve
applicable usage-receipt and approval references.

If governed learning memory is present, recalled practices are ADVISORY_ONLY and the
producing run must not auto-promote its own lesson candidate.

After implementation, run the Causal Necessity Audit. Every material changed boundary
must map to a frozen requirement and direct causal evidence. If Builder and Auditor are
the same Claude Code context, label the result SELF_AUDIT; a different model in the
same context does not create independence.

For staging/production claims, prove the terminal path and applicable system readiness.
At exact head, run the Surgical Determinacy Audit, complete diff review, required CI,
machine gate, and exact-head audit.

Do not claim RELEASE READY without all mandatory proof and authorization. If code is
verified but a mandatory external condition is unavailable, report CODE VERIFIED /
GOVERNANCE HOLD.
```

See [`docs/CLAUDE_CODE_QUICKSTART.md`](docs/CLAUDE_CODE_QUICKSTART.md) for installation and use.
