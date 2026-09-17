# Deployment, Iteration, and Release

## Choose One Deployment Mode

Use **local candidate deployment** when screenshots must validate changes before
they are committed. The consuming repository must provide a reviewed Fabric CLI
deployment file. Run:

```bash
fab deploy --config <approved-config.yml> --target_env <development-environment>
```

The configuration must target the resolved development workspace, scope publish
to the intended report and semantic model, and set `unpublish.skip` for that
environment. Fabric CLI enables unpublish by default; never use an unreviewed
configuration or `--force` merely to avoid confirmation. Verify dependencies and
logical IDs before selective deployment.

Use **Git-sync deployment** only when each candidate has already been committed
and pushed. Call workspace Git status, then `updateFromGit` with the exact
`workspaceHead` and remote commit hash returned by the API. Poll the Fabric
long-running operation and fail on conflicts or head mismatch.

## Iteration

For each candidate:

1. Edit only approved source files and run PBIR/model validation.
2. Deploy using the selected mode and wait for completion.
3. Re-resolve report/model items and verify the report binding.
4. Refresh only when model/data changes require it and the human authorized it.
   Use `fab api -A powerbi` to submit and poll the refresh; credential failures
   are blockers, not retry loops.
5. Export explicit PNG scenarios, inspect the images, and run independent
   numerical checks.
6. Repeat for material defects. Retain the latest passing evidence and label
   superseded runs. Stop after three visual rounds unless extended by the human.

## Commit and Pull Request

After all required gates pass, inspect status and diff, stage only intended
source/configuration changes, run repository tests, commit, and push the feature
branch. For local candidate deployment, rerun workspace Git status after push.
The remote side should now contain the candidate commit; reconcile with
`updateFromGit` and verify `changes` is empty and `workspaceHead` equals
`remoteCommitHash` at the pushed commit. Stop if direct deployment and Git
content differ rather than forcing a conflict policy.

Create the pull request only after that reconciliation. Include the change
summary, validation gates, refresh/export evidence location, `not_run` checks,
and remaining risks. Follow repository conventions and never expose tokens,
private resource URLs, or confidential screenshots in the PR.
