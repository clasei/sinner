"""
CLI interface for sinner using Typer.
Clean, obvious command structure.
"""

import typer
from typing import Optional
from pathlib import Path

from .core import Controller
from .utils import GitIntegration, show_banner
from . import __version__

app = typer.Typer(
    name="sinner",
    help="Local-first CLI agent that turns messy intent into clean output",
    add_completion=False,
)


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
        typer.echo(result)
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
        typer.echo(result)
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def comment(
    count: int = typer.Option(5, "--count", "-c", help="Number of recent commits to analyze"),
    since: Optional[str] = typer.Option(None, "--since", help="Get commits since this date"),
    squash: bool = typer.Option(False, "--squash", help="Generate squash merge comment"),
    merge: bool = typer.Option(False, "--merge", help="Generate merge/pull request comment"),
):
    """
    Generate a comment for squash or merge requests based on recent commits.
    
    Examples:
        sinner comment --squash
        sinner comment --merge --count 10
        sinner comment --since "2 weeks ago"
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
        result = controller.run("comment", commits_text, squash=squash, merge=merge)
        typer.echo(result)
        
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
        typer.echo(result)
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def config():
    """
    Show current configuration (LLM endpoint, model, etc.).
    """
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    
    typer.echo("Current Configuration:")
    typer.echo(f"  Base URL: {os.getenv('LMSTUDIO_BASE_URL', 'http://127.0.0.1:1234/v1')}")
    typer.echo(f"  Model: {os.getenv('MODEL_ID', 'google/gemma-3n-e4b')}")
    typer.echo(f"  API Key: {'set' if os.getenv('LMSTUDIO_API_KEY') else 'not set (using default)'}")


def version_callback(value: bool):
    """Handle --version flag."""
    if value:
        show_banner()
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
