# PR: feat: show vote share and leader on the results chart

Base: `main` (haco29/sdlc-workshop)

## Why

Raw vote counts don't show who is winning at a glance. Each bar now carries its share of the vote, and the leader is marked with 🏆. See [spec.md](spec.md).

## What changed

1. Task 1: `shares()` and `format_share()` in `poll/core.py` (up to 2 decimals, trailing zeros dropped).
2. Task 2: `leaders()` in `poll/core.py` (all tied options; none at zero votes).
3. Task 3: `app.py` draws the results as an Altair chart with a percent label on each bar and 🏆 above the leader(s). Vote counts stay on the y-axis.
4. `pyproject.toml`: `streamlit>=1.46` (first version with `st.context.theme`, used for label color); `uv.lock` updated to match.
5. `.claude/settings.json`: enables the sdlc plugin for this project.

## How it was tested

- 2026-10-17 · task 3 GREEN · `uv run pytest -q && uv run ruff check .` → 29 passed, lint clean
- 2026-10-17 · /sdlc:test gap pass · `uv run pytest -q && uv run ruff check .` → 30 passed, lint clean
- 2026-10-17 · review fixes 1, 2, 6 · `uv run pytest -q && uv run ruff check .` → 31 passed, lint clean
- 2026-10-17 · /sdlc:code-simplify · `uv run pytest -q && uv run ruff check .` → 31 passed, lint clean; no changes
- 2026-10-17 · /sdlc:pr gate check · `uv run pytest -q && uv run ruff check .` → 31 passed, lint clean

## Gates

| Gate | Result | Evidence |
|---|---|---|
| G1 Spec | pass | `spec.md` Approved (2026-10-17) |
| G2 Plan | pass | `plan.md` has 3 tasks with acceptance criteria, coverage and evidence |
| G3 Tasks | pass | all 3 boxes ticked in `todo.md` |
| G4 Evidence | pass | `uv run pytest -q` 31 passed, `uv run ruff check .` clean, after the last code change |
| G5 Alignment | pass | criteria 1-4 `tests/test_core.py`; 5-6 `tests/test_app.py`; 7 the suite; no changes outside the spec's scope |
| G6 Coverage | pass | every coverage line ticked |

## Review

7 findings in [review.md](review.md): 3 fixed (Streamlit version floor, `leaders()` computed once, zero-vote share test) and 4 won't fix with reasons (latent `max()` risk, chart constants, small test helper, `.claude/settings.json` kept on purpose).

## Out of scope

No sorting of bars, no change to the poll data or `poll.json`, no percent in the "N votes so far" caption, no new dependencies.
