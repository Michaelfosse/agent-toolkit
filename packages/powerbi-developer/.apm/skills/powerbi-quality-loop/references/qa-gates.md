# QA Gates and Evidence

| Gate | Minimum evidence | Does not prove |
| --- | --- | --- |
| Structure | Report validation output, reviewed PBIR diff, successful Desktop load | Correct numbers or interactions |
| Numbers | Independent expected result, provenance, actual query result, displayed visual value | Correct report layout |
| Visual communication | Screenshot reviewed against the page brief and design standard | Model bindings or behavior |
| Behavior and access | Recorded tests for affected slicers, reset, bookmarks, drillthrough, navigation, and applicable identities | General performance |
| Usability and performance | Actual-size review, keyboard/accessibility results, and realistic timing evidence | Business correctness |

Use `pass`, `fail`, or `not_run` for every applicable gate. Missing evidence is
`not_run`, not `pass`. Re-run affected gates after a fix. Test numbers with an
approved existing measure, controlled fixture, or independently checked source
calculation; do not validate a newly generated DAX formula with the same agent's
unreviewed calculation.
