# Using GCU with ChatGPT Projects and Custom GPTs

Governed Coding Upgrade is LLM-agnostic and can be used with ChatGPT as a governance reference and operating instruction.

The important distinction is between **reference material** and **behavioral instructions**.

## ChatGPT Project

A ChatGPT Project can keep chats, uploaded reference files, and project-specific instructions together.

Recommended setup:

### Project sources

Add:

- [`SKILL.md`](../SKILL.md) — authoritative protocol;
- [`GLOBAL_AGENT_RULE.md`](../GLOBAL_AGENT_RULE.md) — invocation contract;
- [`docs/SURGICAL_CHANGE_DETERMINACY.md`](SURGICAL_CHANGE_DETERMINACY.md) — deep surgical-control reference;
- the target repository's `.governance/PROJECT_ADAPTER.md` when available;
- any frozen per-change governance artifacts relevant to the work.

### Project instructions

Put the mandatory operating behavior from [`GLOBAL_AGENT_RULE.md`](../GLOBAL_AGENT_RULE.md) into the Project instructions, or add a concise instruction that explicitly requires the model to read and obey that rule and `SKILL.md` before any qualifying code change.

Do **not** rely on the uploaded file alone as the only behavioral control. Reference files supply source context; project instructions are the persistent place to state how ChatGPT should behave inside that project.

OpenAI Project documentation: https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt

## Custom GPT

For a custom GPT, use the same separation:

### Knowledge

Upload GCU protocol/reference files as Knowledge.

Recommended minimum:

```text
SKILL.md
GLOBAL_AGENT_RULE.md
docs/SURGICAL_CHANGE_DETERMINACY.md
```

Add repository-specific or domain documentation as Knowledge when appropriate.

### Instructions

Put the mandatory governance behavior in the GPT's Instructions.

A concise starting instruction is:

```text
For every qualifying coding change, follow the uploaded Governed Coding Upgrade
protocol. Treat SKILL.md as the authoritative GCU specification and GLOBAL_AGENT_RULE.md
as the mandatory invocation contract. Do not edit until Requirement Preservation and
the Surgical Change Determinacy Gate pass. Do not broaden scope from incidental
discovery. Run the required verification, Causal Necessity Audit, and exact-head
Surgical Determinacy Audit before making a completion claim.
```

OpenAI's GPT guidance distinguishes Instructions, which define behavior, from Knowledge, which provides reference material. That is why GCU should use both rather than treating a Knowledge upload as an executable policy by itself.

OpenAI GPT configuration documentation: https://help.openai.com/en/articles/8554397-creating-a-gpt

## When ChatGPT has repository/tool access

If the ChatGPT environment can directly inspect and edit a repository, GCU can govern the actual change lifecycle.

If it cannot access the repository or execute tests, it can still use GCU to:

- inspect supplied code/files;
- freeze requirement and determinacy artifacts;
- produce governed implementation instructions;
- review a supplied diff;
- perform a documentation-level audit.

It must not claim direct repository proof, exact-head CI, machine-gate PASS, or production readiness when those actions were not actually executed.

## ChatGPT Project versus custom GPT

Use a **Project** when you want GCU tied to an evolving body of work, repository context, files, and ongoing chats.

Use a **custom GPT** when you want a reusable GCU-configured assistant that can be applied across conversations or users, subject to the GPT's configured capabilities and access.

In both cases:

```text
reference files ≠ automatic execution authority
instructions ≠ proof
model confidence ≠ evidence
```

GCU completion claims still require the direct evidence specified by the protocol.
