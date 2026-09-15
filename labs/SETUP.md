# Setting up the CCDV-F labs on a Mac

The same guide is inside the study tracker at https://www.amitphadke.com/learning/ccdv-f/tracker/ (Chapter 0 → *Set up your Mac for the labs*).

## Do this once — your Mac, start to finish

Everything below is copy-paste. Open **Terminal** (Spotlight `⌘ Space` → type `Terminal` → Enter) and work through it in order. Where a step says *check*, the output should look roughly like the line shown — if it doesn't, stop there and fix that step before moving on.

### 1. Homebrew (the package installer)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

It will ask for your Mac password (typing shows nothing — that's normal) and may ask to install Apple's Command Line Tools; say yes. At the end it prints two `echo ... >> ~/.zprofile` lines on Apple Silicon — **run them**, then close and reopen Terminal.

*Check:* `brew --version` → `Homebrew 4.x.x`

### 2. Python, git and VS Code

```bash
brew install python@3.12 git
brew install --cask visual-studio-code
```

*Check:* `python3.12 --version` → `Python 3.12.x` · `git --version` → `git version 2.x` · `code --version` → three lines starting with a version number.

If `code` is not found, open VS Code, press `⇧⌘P`, type *Shell Command: Install 'code' command in PATH*, press Enter, then reopen Terminal.

### 3. Tell git who you are

```bash
git config --global user.name "Amit Phadke"
git config --global user.email "amitrameshphadke@gmail.com"
git config --global init.defaultBranch main
```

### 4. Get the labs onto your Mac

The labs live in your website repo, under `labs/`. If you already have it cloned (you do — `~/dev/amitrphadke.github.io`), just update it:

```bash
cd ~/dev/amitrphadke.github.io && git pull
```

If you are starting on a fresh machine instead:

```bash
mkdir -p ~/dev && cd ~/dev
git clone https://github.com/amitrphadke/amitrphadke.github.io.git
cd amitrphadke.github.io
```

### 5. Create the Python environment

```bash
cd ~/dev/amitrphadke.github.io/labs
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Your prompt now starts with `(.venv)`. **Every time you open a new Terminal to do a lab, run `cd ~/dev/amitrphadke.github.io/labs && source .venv/bin/activate` first** — that one line is the whole ritual.

*Check:* `python -c "import anthropic, pytest; print('ok')"` → `ok`

### 6. Your keys, in a file git will never commit

```bash
cp .env.example .env
code .env
```

VS Code opens `.env`. Fill in two lines and save (`⌘S`):

```
ANTHROPIC_API_KEY=sk-ant-...        # console.anthropic.com → API keys → Create key
GH_TOKEN=github_pat_...             # the same fine-grained token the tracker uses
```

`ANTHROPIC_API_KEY` is billed per use — set a spend limit of $10 in the Console under **Billing → Spend limits**. The labs default to the cheapest model and the whole set costs well under $5. `GH_TOKEN` is what lets `check.py` tick a lab off in this tracker.

*Check that git will not leak it:*

```bash
git check-ignore -v .env
```

It must print a line mentioning `labs/.gitignore`. If it prints nothing, stop — your key would get committed. (`.gitignore` in `labs/` already lists `.env`; if the file is missing, recreate it with `printf '.env\n.venv/\n__pycache__/\n' > .gitignore`.)

### 7. Prove the whole loop works

```bash
python check.py ch2/d4
```

That lab needs no API key, so it runs anywhere. You will see `FAIL` — correct, you haven't written the code yet. Now open it in VS Code:

```bash
code ~/dev/amitrphadke.github.io/labs
```

Fill in the `TODO`s in `ch2/d4_errors_backoff/lab.py`, save, and run `python check.py ch2/d4` again. When it turns **PASS**, look at this tracker — the lab ticks itself within a minute.

### 8. Optional but worth it

```bash
brew install --cask claude        # the Claude desktop app
npm i -g @anthropic-ai/claude-code   # Claude Code CLI, then run: claude
```

Chapter 6's labs and lab 4.2 use Claude Code with your Max subscription instead of the API key, so having it installed and logged in (`claude` → follow the browser login) saves you later.

### Daily ritual, once all of the above is done

```bash
cd ~/dev/amitrphadke.github.io/labs && source .venv/bin/activate
python check.py ch1/d0        # today's lab
```

### When something breaks

`command not found: python3.12` — reopen Terminal, or re-run the two `echo` lines from step 1.
`ModuleNotFoundError` — you forgot `source .venv/bin/activate`.
`check.py` says *GH_TOKEN not set* — the tests passed but the tracker was not updated; fix `.env` and run it again.
`401` or `403` from the API — the key in `.env` is wrong or has no credit; check **Billing** in the Console.
