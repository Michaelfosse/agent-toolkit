# Security

Agent packages are executable in effect. Instructions can influence tool use, scripts execute directly, MCP servers add external trust boundaries, and hooks run automatically.

## Content Boundary

Do not add:

- Tokens, passwords, private keys, connection strings, or environment-file contents.
- Personal data, banking data, user identifiers, or raw production records.
- Employer or client workspace IDs, tenant IDs, endpoint URLs, service-principal identities, internal hostnames, or proprietary repository URLs.
- Business schemas, field registries, report names, schedules, or operational details unless the repository has explicitly been classified for that content.
- Absolute home-directory paths in portable package content.

Use synthetic names and values in examples. Describe a reusable method rather than copying a project runbook.

## Executable Content

Before adding `scripts/`, hooks, plugins, or MCP declarations:

1. Document when the code runs and with which permissions.
2. Make dry-run or read-only behavior the default where practical.
3. Avoid printing secrets or source content to notifications and logs.
4. Use the least required network and filesystem access.
5. Keep authoritative enforcement in CI, pre-commit, or platform policy when correctness matters.
6. Review target-specific adapters separately because APM portability does not imply runtime equivalence.

## Before Publication

- Run `apm audit`.
- Search the complete Git history for secrets and private identifiers.
- Review every example and fixture, not only executable files.
- Confirm dependency sources and pinned versions.
- Add a license only after deciding what may be reused publicly.

Report a suspected disclosure privately to the repository owner. Do not open a public issue containing secret values.
