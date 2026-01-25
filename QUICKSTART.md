# Quick Start Guide

## Installation (3 steps, ~2 minutes)

1. **Clone and install**

   ```bash
   git clone https://github.com/clasei/sinner.git
   cd sinner
   ```

   Then choose one:

   **Virtual environment** (recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e .
   ```

   **pipx** (for global access):

   ```bash
   brew install pipx  # macOS/Linux
   pipx install -e .
   pipx ensurepath
   ```

2. **Initialize config**

   ```bash
   sinner config --init
   ```

3. **Start LM Studio**
   - Open [LM Studio](https://lmstudio.ai/)
   - Load a model (recommended: `llama-3.2-3b-instruct`)
   - Start the local server (default port 1234)

**That's it!** Now use sinner from any directory.

## Usage Examples

### Generate a name

```bash
sinner name "a class that manages user authentication sessions"
```

### Create a commit message

```bash
sinner commit "refactored authentication module to use JWT tokens"
```

### Generate merge comment

```bash
# For squash merge (last 5 commits)
sinner comment --squash

# For pull request (last 10 commits)
sinner comment --merge --count 10
```

### Explain something

```bash
sinner explain "what are Python decorators?"
```

### Check configuration

```bash
sinner config
```

## Troubleshooting

### Connection refused

- Make sure LM Studio is running
- Check that the server is on the correct port (default: 1234)
- Verify your config: `sinner config`

### Command not found: sinner

**If using venv:**

```bash
cd /path/to/sinner
source venv/bin/activate  # Activate the virtual environment
```

**If using pipx:**

```bash
pipx ensurepath  # Add ~/.local/bin to PATH
# Then restart your terminal or: source ~/.zshrc
```

### Change model

Edit `~/.config/sinner/.env` and update `MODEL_ID` to match your LM Studio model name.

### Not in a git repository (for comment command)

- The `comment` command requires being in a git repository
- Initialize git if needed: `git init`

## Development

### Project Structure

```
sinner/
├── src/sinner/
│   ├── __main__.py          # CLI interface
│   ├── core/
│   │   ├── controller.py    # Command routing
│   │   ├── llm_client.py    # LLM API client
│   │   └── prompts.py       # Prompt templates
│   └── utils/
│       ├── banner.py        # ASCII banner
│       ├── formatter.py     # Output cleaning
│       └── git_integration.py  # Git operations
├── requirements.txt
└── README.md
```

**Config location:** `~/.config/sinner/.env`

### Adding a new command

1. Add prompt template in `src/sinner/core/prompts.py`
2. Add handler method in `src/sinner/core/controller.py`
3. Add CLI command in `src/sinner/__main__.py`
4. Test it!

## What's Next?

Check the main [README.md](README.md) for more details and the project roadmap.
