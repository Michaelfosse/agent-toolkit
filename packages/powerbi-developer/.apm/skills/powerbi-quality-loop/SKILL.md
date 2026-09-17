---
name: powerbi-quality-loop
description: Use when authoring, reviewing, improving, validating, or redesigning a Power BI PBIP/PBIR report page with AI, especially when rendered screenshots, chart choice, layout quality, numerical correctness, or interaction behavior must be checked. Do not use for general Fabric engineering or for standalone semantic-model changes without report work.
---

# Power BI Quality Loop

Use Microsoft's installed Power BI skills for planning, design, PBIR mechanics,
and semantic-model work. This skill defines the required quality loop around
those operations.

1. Confirm the requested report page, intended audience, question or decision,
   approved model objects, filter behavior, and out-of-scope model changes.
2. For new or redesigned pages, create an approved design brief before changing
   PBIR. For targeted changes, record the expected visual and binding change.
3. Inspect the model before binding visuals. Use `powerbi-modeling-mcp` for a
   local PBIP/Desktop/Fabric model; use `powerbi-remote` only to inspect or
   query a published model or report.
4. Make one small, reviewable PBIR change. Prefer native visuals; use a custom
   visual only when it has a clear analytical benefit and approved dependency.
5. Validate the report definition. If Power BI Desktop Bridge is available,
   reload the intended Desktop process and capture the affected page. Never
   overwrite unsaved Desktop changes.
6. Review the actual screenshot with a vision-capable reviewer at the intended
   user viewport. Fix material defects and repeat no more than three visual
   revision rounds before reporting unresolved issues.
7. Record structural, numerical, visual, behavior, and usability/performance
   evidence. A screenshot alone does not prove measure correctness, visual
   bindings, slicers, drillthrough, bookmarks, or access behavior.

For service-rendered evidence after deployment or refresh, hand off to
`powerbi-deploy-screenshot-loop`. It requires explicit human-provided target
names and authorization for every deployment, refresh, and export action.

Read these references when needed:

- [Desktop Bridge workflow](references/desktop-bridge.md)
- [Visualization design standard](references/design-standard.md)
- [QA gates and evidence](references/qa-gates.md)

Completion means the approved scope is implemented and every applicable QA gate
has evidence, a documented failure, or an explicit `not_run` status.
