```
     _
 ___(_)_ __  _ __   ___ _ __
/ __| | '_ \| '_ \ / _ \ '__|
\__ \ | | | | | | |  __/ |
|___/_|_| |_|_| |_|\___|_|

local-first CLI agent · private by design
```

# sinner

**Turn messy intent into clean, professional output**

## What is sinner?

sinner takes your messy thoughts and turns them into clean, professional output:

- Generate meaningful names for variables, functions, and classes
- Create conventional commit messages from change descriptions
- Generate formal PR descriptions from git history
- Create squash commit messages from multiple commits
- Review recent work with informal summaries
- Explain code and technical concepts clearly

**Private by design.** Everything runs locally on your machine. No cloud. No accounts. No telemetry.

---

## Installation

### Prerequisites

- Python 3.8+
- Git (for commit analysis features)
- Local LLM server (e.g., [LM Studio](https://lmstudio.ai/))

### Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/clasei/sinner.git
   cd sinner
   ```

2. **Install sinner** (choose one method)

   **Option A: Virtual Environment** (recommended for most users)

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e .
   ```

   **Option B: pipx** (for global CLI tool access)

   ```bash
   brew install pipx  # macOS/Linux (see pipx.pypa.io for other platforms)
   pipx install -e .
   pipx ensurepath    # Adds ~/.local/bin to PATH
   ```

   _Note: Direct `pip3 install` may fail on macOS due to PEP 668 externally-managed environments._

3. **Initialize configuration**

   ```bash
   sinner config --init
   ```

   This creates `~/.config/sinner/.env` with default settings.

4. **Start your local LLM**
   - Open [LM Studio](https://lmstudio.ai/)
   - Load a model (recommended: `google/gemma-3n-e4b`)
   - Start the local server (default: `http://127.0.0.1:1234`)

5. **You're ready!**

   ```bash
   sinner --help
   ```

   **Switching models?**
   1. Load new model in LM Studio's Chat tab
   2. Restart the local server
   3. Update your config:
      ```bash
      nano ~/.config/sinner/.env
      ```
   4. Change `MODEL_ID` to match the model name shown in LM Studio
   5. Test: `sinner --version`

---

## Usage

sinner works from any directory once installed. No need to be in the sinner repo!

### Generate names

```bash
sinner name "a function that validates email addresses"
```

### Create commit messages

```bash
sinner commit "added user authentication with JWT tokens"
```

### Generate PR descriptions

```bash
# Formal PR description with title and bullets (last 5 commits)
sinner pr

# Specify number of commits
sinner pr --count 10

# PR from commits since a date
sinner pr --since "2 weeks ago"
```

### Generate squash commit messages

```bash
# Single commit message for squash merge (last 5 commits)
sinner squash

# Squash message from more commits
sinner squash --count 8

# Squash from commits since date
sinner squash --since "1 week ago"
```

### Review recent changes

```bash
# Informal summary of recent work (last 3 commits)
sinner comment

# Review more commits
sinner comment --count 5

# Review changes since date
sinner comment --since "yesterday"
```

### Explain code or concepts

```bash
sinner explain "what is a closure in Python?"
```

### Check configuration

```bash
sinner config
```

### Show version

```bash
sinner --version
```

---

## Commands

| Command             | Description                             | Examples                                  |
| ------------------- | --------------------------------------- | ----------------------------------------- |
| `name <context>`    | Generate a professional name            | `name "class for handling user sessions"` |
| `commit <changes>`  | Create a conventional commit message    | `commit "refactored auth module"`         |
| `pr`                | Generate formal PR description          | `pr --count 10`                           |
| `squash`            | Generate single commit for squash merge | `squash --count 8`                        |
| `comment`           | Informal summary of recent changes      | `comment --count 5`                       |
| `explain <content>` | Explain code or concepts                | `explain "async/await in JavaScript"`     |
| `config`            | Show current configuration              | `config`                                  |

---

## Project Structure

```
sinner/
├── src/
│   ├── __init__.py          # Package version
│   ├── __main__.py          # CLI entrypoint
│   ├── cli.py               # Typer CLI interface
│   ├── core/
│   │   ├── __init__.py
│   │   ├── controller.py    # Command routing (the mother)
│   │   ├── llm_client.py    # LLM API client
│   │   └── prompts.py       # Prompt templates
│   └── utils/
│       ├── __init__.py
│       ├── banner.py        # ASCII banner
│       └── git_integration.py  # Git commit reading
├── requirements.txt
├── .env                     # Your local config (not in repo)
└── README.md
```

---

## Design Principles

### v0.1 Rules

- ❌ no cloud
- ❌ no database
- ❌ no accounts
- ❌ no scope creep
- ✅ working > perfect
- ✅ ship v0.1

### Architecture

- **Explicit routing:** Commands are routed explicitly. The LLM never decides intent.
- **Isolated prompts:** One prompt per action. Small and focused.
- **Local-first:** Everything runs on your machine with your local LLM.
- **Clean output:** No emojis. No markdown noise. Paste-ready professional text.

---

## Customization

### Custom Prompts

Want to change the output format or style? Edit the prompts directly:

**Location:** `src/sinner/core/prompts.py`

Each command has its own prompt function:

- `prompt_name()` - Naming conventions
- `prompt_commit()` - Commit message format (currently: `type(scope) -> description`)
- `prompt_comment()` - Informal summaries of recent work
- `prompt_comment_pr()` - PR descriptions with title and bullets
- `prompt_comment_squash()` - Single commit message for squash merges
- `prompt_explain()` - Code explanations

**Example:** Change commit format from `type(scope) -> description` to `type: description`:

```python
# In src/sinner/core/prompts.py
def prompt_commit(changes: str) -> str:
    return f"""...
    Create a commit message in this EXACT format:
    type: description
    ..."""
```

After editing, reinstall: `pip install -e .`

### Remove Terminal Signature

Don't want the signature line? That's weird, but this is how you can remove it:

```python
# In src/sinner/__main__.py
def echo_result(result: str):
    """Echo result with signature line."""
    typer.echo(result)
    # typer.echo(f"\n{SIGNATURE}")  # Comment this out
```

After editing, reinstall: `pip install -e .`

---

## Development

### Run locally

```bash
python -m sinner <command>
```

### Test with your local LLM

1. **Start LM Studio** and load a model in the Chat tab
2. **Check the model name** shown at the top of LM Studio
3. **Update `.env`** if needed (MODEL_ID must match exactly)
4. **Test connection:** `python test_connection.py`
5. **Run sinner:** `python -m sinner name "test"`

**Switching models?** Just load a new model in LM Studio and update MODEL_ID in `.env`

---

## Contributing

This is v0.1 - a focused, working baseline. Contributions welcome, but let's keep scope tight:

- Bug fixes: always welcome
- New features: open an issue first to discuss
- Documentation: improvements appreciated

---

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

## Roadmap

### v0.1 (current)

- ✅ Core commands: name, commit, pr, squash, comment, explain
- ✅ Git integration (read commits)
- ✅ Local LLM support
- ✅ CLI with Typer

### Future (maybe)

- Configuration management
- Custom prompt templates
- Additional output formats
- Plugin system

---

**sinner v0.1** - built with quiet confidence 🎾
