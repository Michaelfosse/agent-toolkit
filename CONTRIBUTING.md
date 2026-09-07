# Contributing

## Design a Skill

Start with at least five realistic user prompts. Group prompts only when they share the same workflow, tools, risks, and completion criteria.

Create a separate skill when the capability has a materially different trigger, output, tool requirement, risk level, user group, or release cycle.

Do not split a capability merely because it contains several commands or functions.

## Authoring Rules

- Store skills under `.apm/skills/<skill-name>/SKILL.md`.
- Use lowercase letters, numbers, and hyphens for the directory and frontmatter `name`.
- Keep `SKILL.md` focused on the always-relevant workflow.
- Move optional detail to directly linked files under `references/`.
- Put deterministic or fragile operations in `scripts/` only when an executable is more reliable than prose.
- Put reusable templates and fixtures in `assets/` or `examples/`.
- Do not create chains of references. Link each optional reference directly from `SKILL.md`.
- Do not duplicate authoritative guidance between `SKILL.md` and references.

## Description Rules

The description controls discovery and triggering:

- Begin with `Use when` or another intent-first imperative.
- Include phrases users are likely to type.
- Describe indirect triggers, not only slash commands.
- Distinguish the skill from neighboring skills.
- Keep the description within the Agent Skills limit of 1024 characters.

## Review Process

1. Confirm that the source workflow is durable and not project trivia.
2. Classify every source example as generic, private work context, personal data, or secret.
3. Rewrite from principles rather than copying internal identifiers or business logic.
4. Test at least three expected triggers and two non-triggers.
5. Follow the completion and quality checklist linked from the skill.
6. Run APM validation and audit commands.
7. Review the final diff for sensitive content before committing.

## Validation

```bash
apm compile --validate
apm install --dry-run --target claude,opencode
apm audit
apm pack
```

Test the package from a separate scratch project before tagging a release. Do not validate an installation by writing generated client files into the package source tree and then committing them.
