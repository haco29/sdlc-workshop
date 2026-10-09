# Before the workshop: setup

Please do this before the workshop, at your own desk. It takes about 15 minutes, most of it
downloading. Hit a problem? Send the error message to the facilitator before the day, not
during it.

You need three tools:

| Tool | Why |
|---|---|
| **Git** | Gets the exercises, and records your work as commits. On Windows it also brings Git Bash, which Claude Code uses to run commands. |
| **uv** | Runs Python for you. It downloads the right Python version itself, so you don't need to install Python. |
| **Claude Code** | The agent you'll work with. |

You don't need a GitHub account, an editor or anything else.

## Windows

Use **PowerShell**: open the Start menu and type `PowerShell`. After each install, **close
PowerShell and open it again**, so it finds the new command.

**1. Git for Windows.** Download and run the installer from
[git-scm.com/downloads/win](https://git-scm.com/downloads/win); the default options are
fine. Or, in PowerShell:

```powershell
winget install --id Git.Git -e
```

Check it: `git --version` prints a version number.

**2. uv.**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Check it: `uv --version` prints a version number.

**3. Claude Code.**

```powershell
irm https://claude.ai/install.ps1 | iex
```

Check it: `claude --version` prints a version number.

## macOS

Open **Terminal**.

**1. Git.** Run `git --version`. If Git isn't installed, macOS offers to install the command
line developer tools: accept, and wait for it to finish.

**2. uv.**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**3. Claude Code.**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Close Terminal, open it again, and check: `uv --version` and `claude --version`.

## Both: tell Git who you are

Git won't save a commit until it has a name and an email. Any name and email will do: they
only label your own commits on your own computer.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## Check that everything works

These commands work the same in PowerShell and in Terminal. Run them one at a time.

```bash
git clone https://github.com/haco29/sdlc-workshop.git
cd sdlc-workshop/exercises/01-agent-basics
uv run pytest -q
```

The first `uv run` downloads Python and the test tools, so give it a minute. It should end
with **11 passed**. Then get exercise 2 ready too, so nothing big downloads during the
workshop:

```bash
cd ../02-sdlc-loop
uv run pytest -q
```

It should end with **17 passed**. Finally:

```bash
claude --version
```

That's it. Don't start Claude Code in the exercise folders yet, and don't install anything
else: the workshop takes you through the rest. You'll get login details for Claude
separately.

## If something goes wrong

| You see | What to do |
|---|---|
| `'git'`, `'uv'` or `'claude'` is not recognized | Close the terminal and open a new one. Still failing? The install directory isn't on your PATH: see [Fix your PATH](https://code.claude.com/docs/en/troubleshoot-install). |
| `The token '&&' is not a valid statement separator` | You're in an older PowerShell. Run the commands one at a time, as written above. |
| `python3` opens the Microsoft Store | You don't need it. Use `uv run …` as shown, and uv brings its own Python. |
| An installer asks for administrator rights you don't have | Ask IT before the workshop. Claude Code and uv install without admin rights; Git for Windows may need them. |
| A download fails or times out | You may be behind a proxy or firewall. Try another network, or ask IT. |
| `Please tell me who you are` when committing | Run the two `git config` lines above. |

## Optional: GitHub

You can do the whole workshop without GitHub: your work stays as commits on your computer,
and `/pr` writes the pull request description to a file. If you already use GitHub and want
a real pull request at the end, also install the [GitHub CLI](https://cli.github.com/) and
run `gh auth login`. WORKSHOP.md in exercise 2 shows how.
