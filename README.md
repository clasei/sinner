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

1. **Clone the repository**

   ```bash
   git clone https://github.com/clasei/sinner.git
   cd sinner
   ```

2. **Install dependencies and sinner**

   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

3. **Configure your LLM endpoint**

   Create a `.env` file in the project root:

   ```env
   LMSTUDIO_BASE_URL=http://127.0.0.1:1234/v1
   LMSTUDIO_API_KEY=lm-studio
   MODEL_ID=llama-3.2-3b-instruct
   ```

   **Using a different model?**
   - Load your model in LM Studio's Chat tab
   - Copy the exact model name shown at the top
   - Update `MODEL_ID` in `.env` to match
   - Or use: `python update_model.py "your-model-name"`

4. **Run sinner**
   ```bash
   python -m sinner --help
   ```

---

## Usage

### Generate names

```bash
python -m sinner name "a function that validates email addresses"
```

### Create commit messages

```bash
python -m sinner commit "added user authentication with JWT tokens"
```

### Generate merge/squash comments

```bash
# Squash merge comment from last 5 commits
python -m sinner comment --squash

# Pull request description from last 10 commits
python -m sinner comment --merge --count 10

# Comments from commits since a date
python -m sinner comment --since "2 weeks ago"
```

### Explain code or concepts

```bash
python -m sinner explain "what is a closure in Python?"
```

### Check configuration

```bash
python -m sinner config
```

### Show version

```bash
python -m sinner --version
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
