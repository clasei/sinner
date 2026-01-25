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
- Synthesize squash/merge comments from commit history
- Explain code and technical concepts clearly

**Private by design.** Everything runs locally on your machine. No cloud. No accounts. No telemetry.

---

## Installation

### Prerequisites

- Python 3.8+
- Git (for commit analysis features)
- Local LLM server (e.g., [LM Studio](https://lmstudio.ai/))

### Setup

1. **Clone and install sinner**

   ```bash
   git clone https://github.com/clasei/sinner.git
   cd sinner
   pip install -e .
   ```

2. **Initialize configuration**

   ```bash
   sinner config --init
   ```

   This creates `~/.config/sinner/.env` with default settings.

3. **Start your local LLM**
   - Open [LM Studio](https://lmstudio.ai/)
   - Load a model (recommended: `llama-3.2-3b-instruct`)
   - Start the local server (default: `http://127.0.0.1:1234`)

4. **You're ready!**

   ```bash
   sinner --help
   ```

   **Using a different model?**
   Edit `~/.config/sinner/.env` and update `MODEL_ID` to match the model name shown in LM Studio.

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

### Generate merge/squash comments

```bash
# Squash merge comment from last 5 commits (default)
sinner comment --squash

# Or specify the count explicitly
sinner comment --squash --count 5

# Pull request description from last 10 commits
sinner comment --merge --count 10

# Comments from commits since a date
sinner comment --since "2 weeks ago"
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

| Command                       | Description                                     | Examples                                  |
| ----------------------------- | ----------------------------------------------- | ----------------------------------------- |
| `name <context>`              | Generate a professional name                    | `name "class for handling user sessions"` |
| `commit <changes>`            | Create a conventional commit message            | `commit "refactored auth module"`         |
| `comment [--squash\|--merge]` | Generate merge/squash comments from git history | `comment --squash --count 8`              |
| `explain <content>`           | Explain code or concepts                        | `explain "async/await in JavaScript"`     |
| `config`                      | Show current configuration                      | `config`                                  |

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
- `prompt_comment_squash()` - Squash merge comments
- `prompt_comment_merge()` - Pull request descriptions
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

- ✅ Core commands: name, commit, comment, explain
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
