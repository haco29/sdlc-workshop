# Review: Vote share and leader marker

Reviewed by the `code-reviewer` agent against the branch diff, `spec.md` and `plan.md`.

| # | Severity | Where | Finding | Fix | Status |
|---|---|---|---|---|---|
| 1 | Important | `pyproject.toml:12`, `app.py:42`, `app.py:54` | Floor is `streamlit>=1.30`, but the view uses `st.context.theme.type` and `width="stretch"`, which need a newer Streamlit. An older allowed version would raise. | Raise the floor to the first version that has both (the lock file has 1.65.0), or drop those APIs. | fixed: floor raised to `streamlit>=1.46` (first version with `st.context.theme`); dropped `width="stretch"`, it is the default |
| 2 | Suggestion | `app.py:39-40` | `leaders(poll)` is called once per option, and `shares(poll)` recomputes the tally. | Compute `leading = set(leaders(poll))` once and use `option in leading`. | fixed |
| 3 | Suggestion | `poll/core.py` `leaders()` | `max()` reads the raw votes dict while the list comes from `tally()`. Latent only: `create_poll` guarantees options. | Derive both from `tally(poll)`. | won't fix: latent only, `create_poll` guarantees at least two options |
| 4 | Suggestion | `app.py:42-53` | `dy=-22`, `fontSize=18`, `padding top 30` and the hex colors are unexplained. | One-line comments saying why. | won't fix: the values are plain chart-layout constants, not worth comment noise |
| 5 | Suggestion | `tests/test_app.py` | The Arrow decoding is duplicated in both new tests; `pyarrow` is an undeclared, implicit dependency. | Extract a `chart_rows(app)` helper. | won't fix: two uses, three similar lines beat a premature helper (DRY/YAGNI) |
| 6 | Suggestion | `tests/test_core.py` | No `shares` case where one option has 0 votes while the total is above 0. | Add the test. | fixed |
| 7 | Suggestion | `.claude/settings.json` | Staged but not part of the feature. | Confirm it's intended, or unstage it. | won't fix: kept on purpose, not part of the feature |

Security: nothing found. Option text only goes into the chart as data.
