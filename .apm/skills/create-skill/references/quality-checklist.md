# Skill Quality Checklist

Load this checklist for the final review of a new or substantially changed skill.

## Intent and Boundary

- The capability can be described without joining unrelated jobs with "and."
- Trigger prompts share the same core workflow and completion criteria.
- Neighboring capabilities are named or otherwise easy to distinguish.
- The skill is neither one command disguised as a capability nor an entire role bundled together.

## Discovery

- `name` matches the parent directory and uses lowercase letters, numbers, and hyphens.
- `description` begins with user intent and includes realistic trigger situations.
- The description covers indirect requests, not only exact terminology.
- Non-trigger examples are unlikely to select the skill accidentally.

## Context Design

- `SKILL.md` contains only always-relevant workflow, decisions, and guardrails.
- Optional detail is stored in an appropriate resource directory.
- Every reference is linked directly from `SKILL.md` with a load condition.
- No authoritative instruction is duplicated across files.
- Scripts are used only where deterministic execution is safer or cheaper than regenerated code.

## Safety and Portability

- Examples contain no secrets, personal data, private endpoints, internal identifiers, or proprietary business rules.
- Absolute machine-specific paths are avoided or clearly target-specific.
- Client-specific behavior is isolated and documented.
- Side effects, required confirmation, and authorization boundaries are explicit.

## Verification

- At least three trigger prompts and two non-trigger prompts were assessed.
- A normal path and an important failure path were walked through.
- Validation commands and the definition of done are explicit.
- APM validation and audit complete successfully.
