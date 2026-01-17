"""
CLI entrypoint for sinner.
"""

import typer
from typing import Optional
from sinner.controller import SinnerController

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
    context: str,
    squash: bool = typer.Option(False, "--squash", help="Generate squash commit message"),
    merge: bool = typer.Option(False, "--merge", help="Generate merge request description"),
):
    """Generate a PR comment or commit message.
    
    Examples:
      sinner comment "feat: add auth\nfix: bug"
      sinner comment "feat: add auth\nfix: bug" --squash
      sinner comment "feat: add auth\nfix: bug" --merge
    """
    try:
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