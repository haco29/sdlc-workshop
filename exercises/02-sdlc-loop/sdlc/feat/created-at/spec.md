# Spec: Vote share and leader marker

Status: Approved (2026-10-17)

## Objective

Anyone viewing the poll sees each option's share of the vote as a label on its bar, and the leading option is marked with 🏆. Raw counts alone don't show who is winning at a glance.

## Scope

In scope:
- A pure function in `poll/core.py` that returns each option's share of total votes and which options lead.
- The results chart in `app.py` shows each share as a label on top of its bar, with 🏆 above the leading bar(s). Rendered with an Altair layer, since `st.bar_chart` can't label bars.
- Bar height and y-axis stay as vote counts.

Out of scope:
- Sorting bars (they keep creation order).
- Any change to the poll data shape or `poll.json`.
- Showing a percent in the "N votes so far" caption.
- New dependencies (Altair already ships with Streamlit).

## Success criteria

1. Given a poll with votes, when shares are computed, then each option's share is `votes / total * 100`, rounded to at most 2 decimals.
2. Given a share that is a whole number or has one significant decimal, when it is formatted, then trailing zeros are dropped (`50%`, `12.5%`, `33.33%`).
3. Given several options tied for the most votes, when leaders are computed, then all tied options are leaders.
4. Given a poll with zero total votes, when shares and leaders are computed, then every share is `0` (no division by zero) and there are no leaders.
5. Given a poll with votes, when the results render, then every bar carries its formatted share label and 🏆 appears above each leading bar only.
6. Given the results render, then bars stay in creation order and bar height is the vote count.
7. `uv run pytest -q` and `uv run ruff check .` pass; every new `poll/core.py` behavior has a test in `tests/test_core.py` written first, and `tests/test_app.py` only checks the wiring.

## Edge cases and decisions

| Case | Decision | Why |
|---|---|---|
| Tie for most votes | All tied options get 🏆 | Picking one would be arbitrary and misleading |
| Zero total votes | Every bar shows `0%`, nobody gets 🏆 | No one is leading yet; avoids divide by zero |
| Option with zero votes while others have votes | Shows `0%`, no 🏆 | Consistent with the zero-total case |
| Rounding | At most 2 decimals, trailing zeros dropped; labels may not sum to exactly 100 | Answer from the grilling; simplicity over forced-sum rounding |
| Sorting | Not changed, creation order | Out of scope |
| Chart type and y-axis | Keep the bar chart with vote counts | Percent is a label, not a new scale |

## Open questions

- None.

## Decisions

- None recorded as ADRs.
