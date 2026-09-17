# Export-to-File Workflow

ExportToFile is asynchronous. For a workspace report, use the Power BI REST
endpoints through `fab api -A powerbi` to create the job and poll status:

```text
POST /v1.0/myorg/groups/{workspaceId}/reports/{reportId}/ExportTo
GET  /v1.0/myorg/groups/{workspaceId}/reports/{reportId}/exports/{exportId}
GET  /v1.0/myorg/groups/{workspaceId}/reports/{reportId}/exports/{exportId}/file
```

Request `PNG` with explicit page technical names. Discover those names from the
published report API; they differ from visible page titles. Supply approved
report-level filters, bookmarks, locale, or identity context when the scenario
requires them. Without a filter or bookmark, the export validates only the
default report state.

Poll using the server-provided retry guidance when available. Stop on `Failed`,
timeout, or a changed report/model binding. A multi-page PNG export is a ZIP
with one image per page.

`fab api` is suitable for JSON requests and status responses. Use an approved
binary-capable client for the final download and retain the original ZIP with
the extracted page PNGs. Do not print access tokens or presigned resource URLs
into chat, logs, or committed files.

Prerequisites and limits:

- The workspace requires Fabric, Premium, or Embedded capacity; PPU is not
  supported.
- The tenant setting for image export must be enabled.
- PNG exports do not support sensitivity labels.
- A job supports at most 50 report pages or visuals.
- Some custom and script-based visuals do not render in exported images.
