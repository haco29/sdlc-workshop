# Plan: Vote share and leader marker

Spec: [spec.md](spec.md)

## Approach

Business rules go in `poll/core.py` as pure functions over the poll dict: `shares`, `leaders` and `format_share`. `app.py` stays thin: it calls them and builds the chart. The chart becomes an Altair layer (bars of vote counts, a text layer with the share label, a text layer with 🏆 for leaders) rendered with `st.altair_chart`, since `st.bar_chart` can't label bars. Altair ships with Streamlit, so there is no new dependency. Bars keep creation order; no change to `store.py` or `poll.json`.

Core API:

- `shares(poll) -> list[tuple[str, float]]`: `(option, percent)` in creation order, rounded to 2 decimals; all `0.0` when there are no votes.
- `leaders(poll) -> list[str]`: options tied for the most votes; empty when there are no votes.
- `format_share(percent) -> str`: `f"{percent:g}%"`, which drops trailing zeros.

## Tasks

### Task 1: Share per option

- Acceptance criteria: spec #1, #2, #4 (shares part). Shares are `votes / total * 100` rounded to at most 2 decimals, in creation order. Zero total gives all `0`. `format_share` gives `50%`, `12.5%`, `33.33%`, `0%`, `100%`.
- Test that proves it: in `tests/test_core.py`: `shares` for a 1/1/1 poll (33.33 each), a 2/1/1 poll (50, 25, 25), and a new poll (all 0). Parametrized `format_share` cases.
- Files: `poll/core.py`, `tests/test_core.py`

### Task 2: Leaders

- Acceptance criteria: spec #3, #4 (leaders part). A single top option is the only leader; tied top options are all leaders; no votes means no leaders.
- Test that proves it: in `tests/test_core.py`: one leader, a tie, and a new poll (empty list).
- Files: `poll/core.py`, `tests/test_core.py`

### Task 3: Labeled chart in the view

- Acceptance criteria: spec #5, #6, #7. Each bar shows its formatted share above it, leaders get 🏆 above the label, bars stay in creation order with vote counts on the y-axis, and the caption is unchanged.
- Test that proves it: in `tests/test_app.py` (wiring only): after one vote, the page renders an Altair chart whose data carries the formatted labels and the 🏆 on the voted option. Then run the app and look at it, since chart layout is visual.
- Files: `app.py`, `tests/test_app.py`

## Risks

- Altair text layers can clip labels or the 🏆 at the top of the tallest bar. Add y-axis headroom and check the rendered page.
- `AppTest` exposes Altair charts only as a Vega-Lite spec. The smoke test asserts on the spec's data, not pixels, so a visual check by running the app is still needed.
- Shares like 33.33 ×3 don't sum to 100. Accepted in the spec.

## SDLC command coverage

- [x] /sdlc:spec: approved 2026-10-17 after 6 questions
- [x] /sdlc:plan: 3 tasks
- [x] /sdlc:build: tasks 1-3 done
- [x] /sdlc:test: 7 criteria, 1 gap closed (tied leaders in the view)
- [x] /sdlc:review: 7 findings: 3 fixed, 4 won't fix
- [x] /sdlc:code-simplify: nothing to simplify

## Test evidence

- 2026-10-17 · task 1 RED · `uv run pytest -q` → collection error, `format_share` not importable (expected)
- 2026-10-17 · task 1 GREEN · `uv run pytest -q && uv run ruff check .` → 25 passed, lint clean
- 2026-10-17 · task 2 RED · `uv run pytest -q` → collection error, `leaders` not importable (expected)
- 2026-10-17 · task 2 GREEN · `uv run pytest -q && uv run ruff check .` → 28 passed, lint clean
- 2026-10-17 · task 3 RED · `uv run pytest -q tests/test_app.py` → 1 failed (expected)
- 2026-10-17 · task 3 GREEN · `uv run pytest -q && uv run ruff check .` → 29 passed, lint clean
- 2026-10-17 · task 3 fix (label color follows theme) · `uv run pytest -q && uv run ruff check .` → 29 passed, lint clean; viewed in headless Chrome at :8502
- 2026-10-17 · /sdlc:test gap pass · `uv run pytest -q && uv run ruff check .` → 30 passed, lint clean
- 2026-10-17 · review fixes 1, 2, 6 · `uv run pytest -q && uv run ruff check .` → 31 passed, lint clean
- 2026-10-17 · /sdlc:code-simplify · `uv run pytest -q && uv run ruff check .` → 31 passed, lint clean; no changes
- 2026-10-17 · /sdlc:pr gate check · `uv run pytest -q && uv run ruff check .` → 31 passed, lint clean
