# Quick Start Guide

## Installation

1. **Clone and setup**

   ```bash
   git clone https://github.com/clasei/sinner.git
   cd sinner
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure your LLM**

   ```bash
   cp .env.example .env
   # Edit .env with your LM Studio settings
   ```

3. **Start LM Studio**
   - Open LM Studio
   - Load a model (e.g., google/gemma-3-4b)
   - Start the local server (usually on port 1234)

4. **Test sinner**
   ```bash
   python -m src.cli --version
   python -m src.cli config
   ```

## Usage Examples

### Generate a name

```bash
python -m src.cli name "a class that manages user authentication sessions"
```

### Create a commit message

```bash
python -m src.cli commit "refactored authentication module to use JWT tokens"
```

### Generate merge comment

```bash
# For squash merge (last 5 commits)
python -m src.cli comment --squash

# For pull request (last 10 commits)
python -m src.cli comment --merge --count 10
```

### Explain something

```bash
python -m src.cli explain "what are Python decorators?"
```

### Check configuration

```bash
python -m src.cli config
```

## Troubleshooting

### Connection refused

- Make sure LM Studio is running
- Check that the server is on the correct port (default: 1234)
- Verify your `.env` settings

### Module not found

```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Not in a git repository (for comment command)

- The `comment` command requires being in a git repository
- Initialize git if needed: `git init`

## Development

### Project Structure

```
sinner/
├── src/
│   ├── cli.py              # CLI interface
│   ├── core/
│   │   ├── controller.py   # Command routing
│   │   ├── llm_client.py   # LLM API client
│   │   └── prompts.py      # Prompt templates
│   └── utils/
│       ├── banner.py       # ASCII banner
│       └── git_integration.py  # Git operations
├── requirements.txt
├── .env                    # Your config (not in git)
└── README.md
```

### Adding a new command

1. Add prompt template in `src/core/prompts.py`
2. Add handler method in `src/core/controller.py`
3. Add CLI command in `src/cli.py`
4. Test it!

## What's Next?

Check the main [README.md](README.md) for more details and the project roadmap.
