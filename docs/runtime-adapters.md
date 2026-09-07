# Runtime Adapter Design

Version 0.1.0 documents but does not implement runtime callbacks.

## Problem

APM can route a hook descriptor to Claude Code, but APM v0.29.0 skips hooks for OpenCode. OpenCode instead loads executable JavaScript or TypeScript plugins.

The event adapters cannot be shared safely because the lifecycle names, callback payloads, permission model, and error behavior differ.

## Proposed Shape

```text
runtime/
|-- scripts/
|   `-- validate-package.sh
`-- adapters/
    |-- claude/
    |   `-- validate-on-stop.json
    `-- opencode/
        `-- validate-on-idle.ts
```

The shared script owns validation behavior. Each adapter should only translate a client event into a script invocation.

## Claude Adapter

A future Claude descriptor would be authored under `.apm/hooks/` and call a package-relative script with `${PLUGIN_ROOT}`. APM would merge it into `.claude/settings.json`.

Conceptual example:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "${PLUGIN_ROOT}/runtime/scripts/validate-package.sh",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

## OpenCode Adapter

A future OpenCode plugin would subscribe to the closest supported session or tool event and invoke the same script. It must be installed through an OpenCode-specific bootstrap or another explicit deployment mechanism because APM does not translate or deploy it as a hook.

Conceptual example:

```ts
export const PackageValidationPlugin = async ({ $, directory }) => ({
  event: async ({ event }) => {
    if (event.type === "session.idle") {
      await $`${directory}/runtime/scripts/validate-package.sh`
    }
  },
})
```

Confirm the current OpenCode plugin API before implementation. The example shows the architecture, not a pinned API contract.

## First Candidate

The lowest-risk first adapter is a completion notification, not an automatic formatter or mutating validator:

- Shared script sends a generic notification without source text or client names.
- Claude runs it on `Stop`.
- OpenCode runs it on the nearest idle/completion event.
- Failures do not block agent completion.

Package validation should remain an explicit command or CI check until callback frequency, performance, and event semantics are measured.

## Acceptance Criteria for Implementation

- Both adapters call one shared implementation.
- Event differences are covered by target-specific tests or reproducible manual scenarios.
- No secrets, prompts, source code, or project names appear in lock-screen notifications.
- The callback is idempotent and has a bounded timeout.
- Missing platform dependencies fail with an actionable message.
- CI remains authoritative for required validation.
