---
name: start-workshop
description: Walks a workshop participant through setup for the Live Poll SDLC workshop. It checks the agentic-sdlc kit and the Python environment, runs the tests, creates a feature branch, and helps pick a feature from FEATURES.md. Use when the user runs /start-workshop or asks how to get started with the workshop.
disable-model-invocation: true
---

# Start the workshop

Get the participant from a fresh clone to their first `/spec` in about ten minutes. Be
brief and friendly. Do one step at a time, and fix problems before moving on. Never commit
or push in this skill.

## 1. The SDLC kit

Check whether the agentic-sdlc commands are installed:

```bash
claude plugin list 2>/dev/null | grep -i agentic-sdlc \
  || ls ~/.claude/commands/spec.md ~/.cursor/commands/spec.md 2>/dev/null
```

- Found: say so and move on.
- Not found: show the install commands from WORKSHOP.md step 1. Offer to run
  `claude plugin marketplace add haco29/agentic-sdlc` and
  `claude plugin install agentic-sdlc@haco29` for them, and only run them on a yes. Remind
  them to restart Claude Code afterwards and to check that `/spec` shows up when they type
  `/`.

## 2. Their own copy

```bash
git remote get-url origin 2>/dev/null
```

If `origin` is `haco29/sdlc-workshop` itself and they have `gh`, suggest making their own
copy from the template (WORKSHOP.md step 2), so `/pr` opens a PR in their repo and not in
the template. Without GitHub, working locally is fine: `/pr` will write `pr.md` instead.

## 3. Python and tests

```bash
python3 --version          # needs 3.10+
```

If there's no active virtualenv and no `.venv/`, create one
(`python3 -m venv .venv && source .venv/bin/activate`). Then:

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
```

Both must be green before anything changes. If something fails, help fix the environment;
don't touch the app's code.

## 4. Feature branch

Ask which feature they'll build (summarize the five in FEATURES.md in one line each, and
recommend #1 when the room builds the same thing). Then:

```bash
git checkout main && git checkout -b feat/<short-name>
```

## 5. Hand off

Tell them:

- Run `streamlit run app.py` once, to see the app they're changing.
- Their first command is `/spec <the feature in a sentence>`, and it will grill them. The
  questions are the point.
- The loop and what to watch for at each step are in WORKSHOP.md step 5.
- `/sdlc-score` at the end grades how they worked.
