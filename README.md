<p align="center">
  <img src="branding/logo.svg" alt="Governed Coding Upgrade" width="760">
</p>

<p align="center">
  <strong>Governed, surgical, evidence-based software change for AI coding agents and engineering teams.</strong><br>
  Preserve the requirement. Prove the cause. Freeze the smallest justified change. Verify the real path. Audit the exact head.
</p>

<p align="center">
  <code>v2.3.0 — Surgical Determinacy</code>
</p>

> **Official canonical repository.** Maintained and controlled by **Chris Kulbaba (@chriskulbaba2025)**. Public forks and derivatives are not official releases.

# Governed Coding Upgrade v2.3.0 — Surgical Determinacy

Governed Coding Upgrade (GCU) is an LLM-agnostic governance protocol for intentional software changes.

It gives coding agents and engineering teams a deterministic operating model for deciding **what must change, what must not change, how the change will be proven, and when the result is allowed to be called complete**.

GCU does not depend on a particular language, framework, CI provider, cloud, repository layout, coding agent, model provider, or billing system.

The stable machine-facing skill name remains:

```text
governed-coding-upgrade
```

## The problem GCU solves

AI coding agents can produce working code while still creating engineering risk:

- solving the wrong interpretation of the requirement;
- changing more of the system than the requirement needs;
- refactoring adjacent code because it appears related;
- expanding scope after discovering new issues;
- testing a substitute path rather than the real one;
- declaring success from green tests without proving the terminal result;
- auditing their own narrative instead of the exact candidate commit.

GCU treats those as governance failures, not style preferences.

## What v2.3 adds

v2.3 adds **Surgical Determinacy** to the existing GCU production-correctness and orchestration controls.

Before implementation, every governed change must preserve the original requirement and freeze a bounded causal change contract containing:

1. the exact required outcome;
2. the evidence and change hypothesis;
3. the causal boundary;
4. the expected change surface;
5. the protected surface;
6. a structural change budget;
7. the acceptance proof;
8. explicit conditions that require the gate to be reopened.

After implementation, a **Causal Necessity Audit** and **Surgical Determinacy Audit** verify that every material changed boundary was actually required.

The central rule is:

> **Discovery does not create authorization. Every material production change must be causally traceable to the frozen required outcome.**

“Useful,” “related,” “cleaner,” “safer,” and “while we are here” are not sufficient justification for expanding a governed change.

## How GCU works

```text
INTAKE
→ PREFLIGHT
→ PROJECT DISCOVERY / ADAPTER CHECK
→ REQUIREMENT PRESERVATION
→ SURGICAL CHANGE DETERMINACY GATE
→ CHANGE TIER + RELEASE INTENT
→ AGENT / EXECUTION-CONTROL CHECKS when applicable
→ PRODUCTION SPINE / CONTRACT MAP when applicable
→ ACCEPTANCE FREEZE
→ FROZEN CHECKLIST + TEST AREA MAP
→ SEQUENTIAL BUILD / VERIFY
→ CAUSAL NECESSITY AUDIT
→ CHALLENGE
→ TERMINAL / SYSTEM VERIFICATION when applicable
→ MACHINE GATE
→ EXACT-HEAD + SURGICAL DETERMINACY AUDIT
→ CORRECT / RE-AUDIT
→ CLOSE
```

## Surgical does not mean “few lines”

GCU deliberately does **not** use line-count or arbitrary diff-size limits as a definition of minimality.

A surgical change is the **smallest causally justified architectural surface** that can satisfy the frozen requirement correctly.

A change budget therefore governs surfaces such as:

- production modules;
- public contracts and schemas;
- persistence boundaries;
- dependencies;
- external integrations;
- configuration;
- abstractions;
- migrations.

If implementation needs to exceed that budget, the agent must stop and reopen the determinacy gate. It may not silently broaden the work.

## What GCU already governs

v2.3 retains the established GCU controls:

- Project Discovery and Project Adapters;
- Change Tiers and Release Intent;
- optional Scout, Planner, Builder, Challenger, Verifier, Auditor, and Release Authority roles;
- provider-neutral execution-control-plane integration;
- capability-based Test Area Maps;
- Production Spine tracing;
- Producer → Contract → Consumer mapping;
- proof-first acceptance freeze and false-PASS rejection;
- Sequential Evidence Gates;
- real-path and negative-path proof;
- durable-job and external-call controls;
- terminal-path and full-system readiness proof;
- machine release gating;
- exact-head audit;
- truthful `SELF_AUDIT` classification;
- governance hold when required external proof is unavailable;
- optional governed learning-memory integration.

## Change Tiers

- **T1_LOCAL** — contained local behavior.
- **T2_BOUNDARY** — contract, schema, API, auth, data-shape, dependency, or component-boundary work.
- **T3_SYSTEM** — cross-boundary, persistence, async, provider, security-sensitive, multi-component, or end-to-end work.
- **T4_RELEASE** — staging/production readiness or protected release work.

Release Intent remains separate:

- `CHANGE_ONLY`
- `STAGING_READY`
- `PRODUCTION_READY`

The Surgical Change Determinacy Gate applies to every intentional code change. Its documentation depth scales with the Change Tier; its causal requirement does not disappear for T1 work.

## Start here

| If you want to… | Read |
|---|---|
| Understand GCU in plain language | [`docs/WHAT_GCU_DOES.md`](docs/WHAT_GCU_DOES.md) |
| Understand surgical determinacy | [`docs/SURGICAL_CHANGE_DETERMINACY.md`](docs/SURGICAL_CHANGE_DETERMINACY.md) |
| Install and use GCU with Claude Code | [`docs/CLAUDE_CODE_QUICKSTART.md`](docs/CLAUDE_CODE_QUICKSTART.md) |
| Use GCU in a ChatGPT Project or custom GPT | [`docs/CHATGPT_AND_CUSTOM_GPT_USAGE.md`](docs/CHATGPT_AND_CUSTOM_GPT_USAGE.md) |
| Use GCU with another coding agent or LLM | [`docs/LLM_AGNOSTIC_USAGE.md`](docs/LLM_AGNOSTIC_USAGE.md) |
| Adopt GCU in an existing repository | [`docs/ADOPTION_GUIDE.md`](docs/ADOPTION_GUIDE.md) |
| See the authoritative protocol | [`SKILL.md`](SKILL.md) |

## Installation model

GCU separates the **protocol** from the **agent-specific adapter**.

```text
SKILL.md
  authoritative protocol

GLOBAL_AGENT_RULE.md
  vendor-neutral invocation rule

agent-specific adapter
  Claude Code / ChatGPT / custom GPT / Codex / other coding agent

Project Adapter
  repository-specific commands, boundaries, CI and release facts
```

This separation is what makes GCU LLM-agnostic.

### Claude Code

Use `SKILL.md` as the reusable skill and install the invocation rule described in [`docs/CLAUDE_CODE_QUICKSTART.md`](docs/CLAUDE_CODE_QUICKSTART.md).

`GLOBAL_CLAUDE_RULE.md` remains available for backward compatibility, but the canonical vendor-neutral rule is now [`GLOBAL_AGENT_RULE.md`](GLOBAL_AGENT_RULE.md).

### ChatGPT Projects and custom GPTs

Yes: GCU can be used as reference material in ChatGPT.

For a **ChatGPT Project**, add `SKILL.md` and the relevant GCU documents as project sources, then put the mandatory invocation behavior from `GLOBAL_AGENT_RULE.md` into the Project instructions.

For a **custom GPT**, upload the GCU files as Knowledge and place the mandatory operating behavior in the GPT's Instructions. The distinction matters: reference files provide source material; instructions define the persistent behavior expected from the GPT.

See [`docs/CHATGPT_AND_CUSTOM_GPT_USAGE.md`](docs/CHATGPT_AND_CUSTOM_GPT_USAGE.md).

## Repository structure

| Path | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | Authoritative v2.3.0 protocol |
| [`GLOBAL_AGENT_RULE.md`](GLOBAL_AGENT_RULE.md) | Canonical LLM-agnostic invocation rule |
| [`GLOBAL_CLAUDE_RULE.md`](GLOBAL_CLAUDE_RULE.md) | Claude Code compatibility/install rule |
| [`docs/WHAT_GCU_DOES.md`](docs/WHAT_GCU_DOES.md) | Plain-language explainer |
| [`docs/SURGICAL_CHANGE_DETERMINACY.md`](docs/SURGICAL_CHANGE_DETERMINACY.md) | Surgical determinacy specification and examples |
| [`docs/CLAUDE_CODE_QUICKSTART.md`](docs/CLAUDE_CODE_QUICKSTART.md) | Claude Code setup and use |
| [`docs/CHATGPT_AND_CUSTOM_GPT_USAGE.md`](docs/CHATGPT_AND_CUSTOM_GPT_USAGE.md) | ChatGPT Project/custom GPT setup |
| [`docs/LLM_AGNOSTIC_USAGE.md`](docs/LLM_AGNOSTIC_USAGE.md) | Generic agent integration contract |
| [`docs/UNIVERSAL_PROJECT_MODEL.md`](docs/UNIVERSAL_PROJECT_MODEL.md) | Project discovery, adapters, tiers, monorepo rules |
| [`docs/AGENT_ORCHESTRATION.md`](docs/AGENT_ORCHESTRATION.md) | Optional role-based orchestration |
| [`docs/EXECUTION_CONTROL_PLANE_INTEGRATION.md`](docs/EXECUTION_CONTROL_PLANE_INTEGRATION.md) | Capability, escalation, usage and authority boundaries |
| [`docs/TEST_AREAS.md`](docs/TEST_AREAS.md) | Capability-based proof areas |
| [`templates/SURGICAL_CHANGE_CONTRACT_TEMPLATE.md`](templates/SURGICAL_CHANGE_CONTRACT_TEMPLATE.md) | Per-change determinacy contract |
| [`templates/PROJECT_ADAPTER_TEMPLATE.md`](templates/PROJECT_ADAPTER_TEMPLATE.md) | Repository adapter |
| [`templates/CHANGE_CHECKLIST_TEMPLATE.md`](templates/CHANGE_CHECKLIST_TEMPLATE.md) | Frozen change checklist |
| [`templates/INDEPENDENT_AUDIT_TEMPLATE.md`](templates/INDEPENDENT_AUDIT_TEMPLATE.md) | Exact-head audit |
| [`scripts/validate-package.py`](scripts/validate-package.py) | Package integrity and control validator |

## Core completion rule

> A coding change is not complete because an agent says it is complete. It is complete only when the preserved requirement is satisfied by a causally justified change, the required real-path proof passes, protected surfaces remain protected, and the exact candidate head satisfies the applicable governance and audit gates.

## Versioning

- **Protocol version:** `2.3.0`
- **Project Adapter schema:** `1.0.0`
- **Execution-control contract:** `gcu-execution-control/1.0.0`
- **Governed learning-memory contract:** `gcu-learning-memory/1.0.0` when present
- **Machine-facing name:** `governed-coding-upgrade`

Compatible installations keep the machine-facing identifier stable while protocol obligations may advance under semantic versioning.

**Display name:** Governed Coding Upgrade v2.3.0 — Surgical Determinacy  
**Canonical maintainer:** Chris Kulbaba (@chriskulbaba2025)  
**Copyright:** © 2026 Chris Kulbaba. All rights reserved.
