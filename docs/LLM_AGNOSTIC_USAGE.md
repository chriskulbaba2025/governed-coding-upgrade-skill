# LLM-Agnostic Use of Governed Coding Upgrade

GCU is designed around governance responsibilities rather than model brands.

The protocol can be used with Claude Code, ChatGPT, Codex, another coding agent, a local model harness, a multi-agent orchestrator, or a human engineering workflow.

## Separation of concerns

```text
GCU
→ defines change lifecycle, proof, scope, determinacy, audit and readiness rules

Coding agent / LLM
→ performs reasoning and implementation within those rules

Repository Project Adapter
→ supplies repository-specific commands and boundaries

Execution control plane when present
→ supplies provider/model routing, budgets, credentials and execution receipts

Release Authority
→ controls protected merge/deploy/release decisions
```

GCU does not require a particular provider/model.

## Minimum integration capability

An AI environment can apply GCU effectively when it can:

1. read the authoritative protocol and persistent invocation rule;
2. inspect the relevant repository/files or receive trustworthy snapshots;
3. preserve durable change evidence;
4. execute or truthfully delegate the required verification mechanisms;
5. distinguish actions actually performed from recommendations or simulations.

An environment lacking repository execution access can still use GCU for planning and review, but it must not claim proof it did not execute.

## Canonical installation contract

Every integration should provide equivalents of:

```text
Protocol source:
  SKILL.md

Persistent invocation:
  GLOBAL_AGENT_RULE.md

Repository truth:
  .governance/PROJECT_ADAPTER.md

Per-change determinacy:
  SURGICAL_CHANGE.md or equivalent frozen record

Evidence:
  commands/actions/artifacts/state/SHA references
```

## Agent-specific adapters

Agent-specific files are adapters, not forks of the protocol.

For example:

- `GLOBAL_CLAUDE_RULE.md` adapts GCU to Claude Code installation conventions;
- ChatGPT Project instructions adapt GCU to a Project instruction surface;
- custom GPT Instructions adapt GCU to a reusable GPT;
- another tool may use a repository instruction file, system prompt, policy file, or skill directory.

The adapter may change **how GCU is invoked**, but not the governing semantics of the authoritative `SKILL.md`.

## Model switching

Changing models does not change the governed change contract.

A different model may continue work only after it reads the repository state, durable governance artifacts, and evidence needed to resume correctly.

A stronger model does not create release authority or audit independence by itself.

## LLM-agnostic language

Repository documentation should prefer terms such as:

```text
coding agent
AI execution context
Builder
Auditor
model/provider
execution orchestrator
AI policy authority
```

Use vendor-specific names only in adapter/quickstart documentation.

This keeps the protocol reusable as coding tools and models change.
