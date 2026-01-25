"""
CLI entrypoint for sinner.
"""

import typer
from typing import Optional
from sinner.core.controller import Controller
from sinner.utils.git_integration import GitIntegration

app = typer.Typer(
    name="sinner",
    help="local-first CLI agent that turns messy intent into clean output",
    add_completion=False,
)

BANNER = r"""
     _                      
 ___(_)_ __  _ __   ___ _ __ 
/ __| | '_ \| '_ \ / _ \ '__|
\__ \ | | | | | | |  __/ |   
|___/_|_| |_|_| |_|\___|_|   
                              
local-first CLI agent · private by design
"""

SIGNATURE = "════ sinner · zero fluff, pure function ════"


def echo_result(result: str):
    """Echo result with signature line."""
    typer.echo(result)
    typer.echo(f"\n{SIGNATURE}")


@app.command()
def name(
    context: str = typer.Argument(..., help="Description of what you're naming"),
):
    """
    Generate a professional name for a variable, function, class, or module.
    
    Example:
        sinner name "a function that validates email addresses"
    """
    try:
        controller = Controller()
        result = controller.run("name", context)
        echo_result(result)
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def commit(
    changes: str = typer.Argument(..., help="Description of your changes"),
):
    """
    Generate a conventional-style commit message.
    
    Example:
        sinner commit "added user authentication with JWT tokens"
    """
    try:
        controller = Controller()
        result = controller.run("commit", changes)
        echo_result(result)
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def pr(
    count: int = typer.Option(5, "--count", "-c", help="Number of recent commits to analyze"),
    since: Optional[str] = typer.Option(None, "--since", help="Get commits since this date"),
):
    """
    Generate a formal PR description from git history (title + bullets).
    
    Examples:
        sinner pr
        sinner pr --count 10
        sinner pr --since "2 weeks ago"
    """
    try:
        if not GitIntegration.is_git_repo():
            typer.echo("Error: Not in a git repository", err=True)
            raise typer.Exit(1)
        
        commits = GitIntegration.get_recent_commits(count=count, since=since)
        
        if not commits:
            typer.echo("No commits found", err=True)
            raise typer.Exit(1)
        
        commits_text = "\n".join(commits)
        controller = Controller()
        result = controller.run("pr", commits_text)
        echo_result(result)
        
    except RuntimeError as e:
        typer.echo(f"Git error: {e}", err=True)
        raise typer.Exit(1)
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def squash(
    count: int = typer.Option(5, "--count", "-c", help="Number of recent commits to analyze"),
    since: Optional[str] = typer.Option(None, "--since", help="Get commits since this date"),
):
    """
    Generate a single commit message for squash merges.
    
    Examples:
        sinner squash
        sinner squash --count 8
        sinner squash --since "1 week ago"
    """
    try:
        if not GitIntegration.is_git_repo():
            typer.echo("Error: Not in a git repository", err=True)
            raise typer.Exit(1)
        
        commits = GitIntegration.get_recent_commits(count=count, since=since)
        
        if not commits:
            typer.echo("No commits found", err=True)
            raise typer.Exit(1)
        
        commits_text = "\n".join(commits)
        controller = Controller()
        result = controller.run("squash", commits_text)
        echo_result(result)
        
    except RuntimeError as e:
        typer.echo(f"Git error: {e}", err=True)
        raise typer.Exit(1)
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def comment(
    count: int = typer.Option(3, "--count", "-c", help="Number of recent commits to analyze"),
    since: Optional[str] = typer.Option(None, "--since", help="Get commits since this date"),
):
    """
    Generate an informal, detailed summary of recent changes.
    
    Examples:
        sinner comment
        sinner comment --count 5
        sinner comment --since "yesterday"
    """
    try:
        if not GitIntegration.is_git_repo():
            typer.echo("Error: Not in a git repository", err=True)
            raise typer.Exit(1)
        
        commits = GitIntegration.get_recent_commits(count=count, since=since)
        
        if not commits:
            typer.echo("No commits found", err=True)
            raise typer.Exit(1)
        
        commits_text = "\n".join(commits)
        controller = Controller()
        result = controller.run("comment", commits_text)
        echo_result(result)
        
    except RuntimeError as e:
        typer.echo(f"Git error: {e}", err=True)
        raise typer.Exit(1)
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def explain(
    content: str = typer.Argument(..., help="Code snippet or concept to explain"),
):
    """
    Get a clear explanation of code or a technical concept.
    
    Example:
        sinner explain "what is a closure in Python?"
    """
    try:
        controller = Controller()
        result = controller.run("explain", content)
        echo_result(result)
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def config(
    init: bool = typer.Option(False, "--init", help="Initialize global config file")
):
    """
    Show current configuration or initialize global config.
    
    Use --init to create ~/.config/sinner/.env
    """
    import os
    from pathlib import Path
    from dotenv import load_dotenv
    
    config_dir = Path.home() / ".config" / "sinner"
    env_file = config_dir / ".env"
    
    if init:
        # Create config directory if it doesn't exist
        config_dir.mkdir(parents=True, exist_ok=True)
        
        # Create .env file with defaults if it doesn't exist
        if env_file.exists():
            typer.echo(f"⚠️  Config already exists at {env_file}")
            overwrite = typer.confirm("Overwrite it?")
            if not overwrite:
                typer.echo("Cancelled.")
                raise typer.Exit()
        
        # Create default .env content
        default_config = """# sinner configuration
LMSTUDIO_BASE_URL=http://127.0.0.1:1234/v1
LMSTUDIO_API_KEY=lm-studio
MODEL_ID=google/gemma-3n-e4b
"""
        env_file.write_text(default_config)
        typer.echo(f"✓ Created config at {env_file}")
        typer.echo("\nEdit this file to customize your LLM settings.")
        typer.echo("Then start LM Studio and load your model.")
        raise typer.Exit()
    
    # Show current config
    if env_file.exists():
        load_dotenv(env_file)
        typer.echo(f"Configuration file: {env_file}")
    else:
        load_dotenv()
        typer.echo("Configuration: Using local .env (run 'sinner config --init' to create global config)")
    
    typer.echo("\nCurrent Settings:")
    typer.echo(f"  Base URL: {os.getenv('LMSTUDIO_BASE_URL', 'http://127.0.0.1:1234/v1')}")
    typer.echo(f"  Model: {os.getenv('MODEL_ID', 'google/gemma-3n-e4b')}")
    typer.echo(f"  API Key: {'set' if os.getenv('LMSTUDIO_API_KEY') else 'not set (using default)'}")


def version_callback(value: bool):
    """Handle --version flag."""
    if value:
        from sinner import __version__
        typer.echo(BANNER)
        typer.echo(f"version {__version__}\n")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Show version and exit"
    ),
):
    """
    sinner - local-first CLI agent for developers
    
    Turn messy intent into clean, professional output.
    """
    pass


if __name__ == "__main__":
    app()
