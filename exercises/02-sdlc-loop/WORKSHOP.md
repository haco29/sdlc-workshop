# The SDLC workshop: your playbook

Today you'll add one small feature to this poll app. The feature is the excuse. The goal is
to **run the whole loop once, for real**, and to read what every step produces:

```text
/spec  →  /plan  →  /build  →  /test  →  /review  →  /code-simplify  →  /pr
```

It doesn't matter whether you're backend, frontend or QA: everyone runs the same loop on
the same app.

> **Shortcut:** start Claude Code in this folder (`exercises/02-sdlc-loop`) and run
> **`/start-workshop`**. It checks your setup, makes your branch, and points you at a feature.

## You need

- Git, uv and Claude Code, set up as in [SETUP.md](../../SETUP.md). uv brings its own
  Python, so you don't need to install it.
- No GitHub account. `/pr` writes the PR description to a file instead. If you already use
  GitHub and want a real pull request, see "Optional: a real pull request" below.

## Step 1: Install the SDLC kit (once)

In Claude Code:

```text
/plugin marketplace add haco29/agentic-sdlc
/plugin install agentic-sdlc@haco29
```

Restart Claude Code and type `/`: you should see `/spec`, `/plan`, `/build`, `/test`,
`/review`, `/code-simplify` and `/pr`.

Using Cursor? Clone [agentic-sdlc](https://github.com/haco29/agentic-sdlc) and run
`scripts/install.sh --cursor`, then restart Cursor.

## Step 2: Open the app

You cloned this repo during setup. Go to this exercise's folder:

```bash
cd sdlc-workshop/exercises/02-sdlc-loop
```

Everything from here on runs in `exercises/02-sdlc-loop`, and that's where you start Claude
Code: the agent's instructions for this app and `/start-workshop` live in this folder, and
the loop writes its artifacts to `sdlc/<branch>/` here. Then, one at a time:

```bash
uv run pytest -q              # green before you change anything
uv run streamlit run app.py   # create a poll, vote, get a feel for it
```

### Optional: a real pull request

Only if you already use GitHub and have the `gh` CLI. Make your own repository from this
template instead of the plain clone, so your PR lands in your repo:

```bash
gh repo create my-sdlc-workshop --template haco29/sdlc-workshop --private --clone
```

Then work in `my-sdlc-workshop/exercises/02-sdlc-loop`.

## Step 3: Make a feature branch

```bash
git checkout -b feat/<short-name>      # e.g. feat/percentages
```

Every artifact the loop writes goes to `sdlc/<your-branch>/`, so the branch matters. The
commands refuse to run on `main`.

## Step 4: Pick a feature

Open [FEATURES.md](FEATURES.md) and choose one. Small is the point.

## Step 5: Run the loop, one command at a time

Read what each command produces before you run the next one.

| Command | Produces | Watch for |
|---|---|---|
| `/spec <feature>` | `spec.md` | It grills you, one question at a time. Answering well is the most valuable part of the day. |
| `/plan` | `plan.md`, `todo.md` | Are the tasks small? Does each one name the test that proves it? |
| `/build` | One task, one commit | Logic in `poll/core.py`. The failing test comes first. Run it once per task, or `/build auto` for all of them. |
| `/test` | Tests for the gaps | Every success criterion and edge case in the spec should map to a test. |
| `/review` | `review.md` | A reviewer agent with fresh eyes. Read every finding, and decide fix or won't-fix. |
| `/code-simplify` | A `refactor:` commit | Tests stay green the whole time. "Nothing to simplify" is a fine answer. |
| `/pr` | A PR, or `pr.md` | It checks six gates first. A failing gate means a draft, not a ready PR. |

## Step 6: Score yourself

```text
/sdlc-score
```

It reads your artifacts, commits, tests and PR, and grades **how you worked** out of 100,
with the three things to do differently next time. Not how clever the feature is.

## Step 7: Debrief

- What did `/sdlc-score` take points off for?
- Where did the `/spec` grilling change what you were going to build?
- Which `/review` axis found the most?
- Same feature, different roles: how did your specs and tests differ?
- What would you change in the process itself?

## Tips

- Trust the process even when a step feels like overkill for a small feature. That's the
  muscle we're building.
- Stuck? The goal is a complete loop, not a perfect feature. Ask a facilitator.
- Dummy data only.
