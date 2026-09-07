---
name: create-skill
description: Use when creating, extracting, restructuring, or reviewing an Agent Skill; deciding skill boundaries; choosing between SKILL.md, references, scripts, assets, instructions, agents, or separate skills; or improving skill trigger reliability for Claude Code, OpenCode, and other Agent Skills clients.
---

# Create a Skill

Design one coherent, triggerable capability and package only the context needed to perform it reliably.

## Workflow

1. Capture the intended capability and expected result.
2. Collect realistic trigger and non-trigger prompts.
3. Inspect existing workflows, files, and conventions before drafting.
4. Decide whether the content is a skill or another primitive.
5. Set the skill boundary from the prompts and workflow.
6. Write concise frontmatter and the always-relevant procedure.
7. Move optional detail into directly linked resources.
8. Test discovery, behavior, and completion criteria.
9. Remove duplicated, sensitive, or low-value context.

## Capture Intent

Answer these questions before creating files:

- What task or decision should the skill enable?
- What would a user actually type when they need it?
- What output or state marks successful completion?
- Which tools, source files, or external systems does it require?
- Which mistakes, side effects, or security boundaries matter?
- Which existing patterns should it preserve?

If these answers are unclear, gather more context instead of drafting a broad skill.

## Choose the Primitive

Use a skill for a model-invoked workflow selected from user intent.

Use an instruction for a concise rule that should apply automatically, often to matching file paths.

Use a named agent for a specialist persona that users invoke explicitly and that needs its own role or tool boundaries.

Use a command for an explicitly invoked, parameterized procedure when the target clients support commands.

Use a script for deterministic, exact, or fragile operations. Keep judgment and decision points in Markdown.

Use target-specific hooks or plugins only for automatic lifecycle behavior. Do not disguise a runtime callback as a portable skill.

## Set the Boundary

Keep capabilities together when they share most triggers, workflow steps, tools, risks, and completion criteria.

Split a skill when parts have materially different:

- User triggers.
- Outputs or completion conditions.
- Tool or environment requirements.
- Side-effect or authorization risks.
- Intended users or release cycles.

Do not create one skill per function or command. Do not combine an entire professional role into one catch-all skill.

## Structure the Directory

```text
.apm/skills/<skill-name>/
|-- SKILL.md
|-- references/   # optional deep context loaded on demand
|-- scripts/      # optional deterministic helpers
|-- assets/       # optional templates or files used in output
`-- examples/     # optional sample inputs and outputs
```

`SKILL.md` is required. Keep information there when omitting it would usually make the agent perform the task incorrectly.

Put rare paths, extensive examples, troubleshooting, and domain details in references. Link every reference directly from `SKILL.md` and state when to load it. Avoid reference chains.

## Write Frontmatter

```yaml
---
name: example-skill
description: Use when the user asks to perform a specific task, describes a recognizable situation, or needs a related decision made under stated constraints.
---
```

The name must match the directory and use lowercase letters, numbers, and hyphens.

Make the description intent-first. Include realistic indirect triggers and distinguish it from neighboring skills. Do not rely only on the skill name or a slash command.

## Write the Body

Include:

- The goal in one or two sentences.
- The ordered workflow when sequence matters.
- Decision points the agent cannot infer safely.
- Non-negotiable guardrails and side-effect boundaries.
- Explicit directions for loading references or running scripts.
- Validation steps and the definition of done.

Exclude:

- Generic advice the model already knows.
- Installation notes unrelated to using the capability.
- Repeated content from repository instructions.
- Large reference tables needed only occasionally.
- Secrets, private identifiers, personal data, or copied proprietary examples.

Keep `SKILL.md` below the Agent Skills guidance of 500 lines and 5000 tokens. Prefer a much smaller controller document when the workflow allows it.

## Test the Skill

Create at least:

- Three prompts that should trigger the skill.
- Two similar prompts that should not trigger it.
- One ordinary successful path.
- One important edge or failure path.

Check whether the description selects the skill, the body provides enough context, optional resources are loaded only when relevant, and the completion test is objective.

For a final review, LOAD `references/quality-checklist.md`.

## Definition of Done

A skill is complete when its boundary is clear, discovery text is discriminating, the main workflow is executable, optional context is routed explicitly, sensitive details are absent or approved, and realistic trigger tests demonstrate the intended behavior.
