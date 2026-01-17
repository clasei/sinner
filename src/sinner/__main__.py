"""
CLI entrypoint for sinner.
"""

import typer
from typing import Optional
from sinner.controller import SinnerController
from sinner.git_reader import GitReader

app = typer.Typer(help="sinner - local-first CLI agent for developers")
controller = SinnerController()

BANNER = '''
███████╗██╗███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔════╝██║████╗  ██║████╗  ██║██╔════╝██╔══██╗
███████╗██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
╚════██║██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
███████║██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝

sinner v0.1.0
local-first CLI agent for developers
'''


@app.command()
def name(context: str):
    """Generate a professional name suggestion.
    
    Example: sinner name "a class that handles API authentication"
    """
    try:
        result = controller.run("name", context)
        typer.echo(result)
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def commit(changes: str):
    """Generate a conventional commit message.
    
    Example: sinner commit "refactored auth module for token reuse"
    """
    try:
        result = controller.run("commit", changes)
        typer.echo(result)
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def comment(
    context: Optional[str] = typer.Argument(None, help="Manual context (or leave empty to read from git)"),
    count: int = typer.Option(5, "--count", "-n", help="Number of commits to read"),
    since: Optional[str] = typer.Option(None, "--since", help="Read commits since date/time"),
    squash: bool = typer.Option(False, "--squash", help="Generate squash commit message"),
    merge: bool = typer.Option(False, "--merge", help="Generate merge request description"),
):
    """Generate a PR comment or commit message.
    
    If no context is provided, reads recent commits from git.
    
    Examples:
      sinner comment
      sinner comment --count 10
      sinner comment --since "2 weeks ago"
      sinner comment --squash
      sinner comment "feat: add auth\nfix: bug" --merge
    """
    try:
        # If no manual context, read from git
        if not context:
            if not GitReader.is_git_repo():
                typer.echo("Error: Not in a git repository. Provide manual context or run in a git repo.", err=True)
                raise typer.Exit(1)
            
            commits = GitReader.get_recent_commits(count=count, since=since)
            if not commits:
                typer.echo("Error: No commits found.", err=True)
                raise typer.Exit(1)
            
            context = "\n".join(commits)
        
        result = controller.run("comment", context, squash=squash, merge=merge)
        typer.echo(result)
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def explain(code: str):
    """Explain code clearly and professionally.
    
    Example: sinner explain "def factorial(n): return 1 if n == 0 else n * factorial(n-1)"
    """
    try:
        result = controller.run("explain", code)
        typer.echo(result)
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def config():
    """Show current configuration.
    """
    import os
    typer.echo("Current configuration:")
    typer.echo(f"  LMSTUDIO_BASE_URL: {os.getenv('LMSTUDIO_BASE_URL', 'http://127.0.0.1:1234/v1')}")
    typer.echo(f"  MODEL_ID: {os.getenv('MODEL_ID', 'google/gemma-3-4b')}")


def version_callback(value: bool):
    """Show version and banner."""
    if value:
        typer.echo(BANNER)
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None, "--version", "-v", callback=version_callback, is_eager=True, help="Show version"
    )
):
    """sinner - local-first CLI agent for developers."""
    pass


if __name__ == "__main__":
    app()