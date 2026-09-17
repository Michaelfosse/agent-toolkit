# Workspace Git Safety

Resolve the workspace ID from the human-provided name, then inspect its Git
connection and status before deployment:

```text
GET https://api.fabric.microsoft.com/v1/workspaces/{workspaceId}/git/connection
GET https://api.fabric.microsoft.com/v1/workspaces/{workspaceId}/git/status?includeFilesDetails=true
```

Use `fab api -A fabric` for these requests and poll Fabric long-running
operations when a response is `202`. With `fab api`, pass the endpoint relative
to its configured Fabric API base, for example
`workspaces/{workspaceId}/git/connection`. Compare the connection's provider,
repository, directory, and branch with the local checkout and its upstream.

Treat a workspace as clean only when status shows no `workspaceChange` and no
`Conflict`. Branch switching is safe only when the workspace is clean, the
provider/repository/directory already match, the intended remote branch exists,
and the human approves disconnect/reconnect. Otherwise stop without reconnecting.

A guarded branch change is:

1. Record the existing connection and status evidence.
2. Disconnect the workspace from Git.
3. Connect it to the same provider/repository/directory and intended branch.
4. Initialize the connection.
5. Follow the returned `requiredAction`; for a clean validation workspace this
   is normally `UpdateFromGit` using the returned `workspaceHead` and
   `remoteCommitHash`.
6. Poll completion and rerun connection and detailed status checks.

Never call `CommitToGit` to preserve unexpected workspace work, and never choose
`PreferRemote` or `PreferWorkspace` to resolve a conflict without explicit human
direction. A dirty or conflicted workspace is a blocker, not permission to erase
changes. Reconnection requires workspace admin permission; status and update
operations require the documented contributor/Git scopes.
