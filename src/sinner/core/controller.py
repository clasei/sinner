"""
Agent controller - the mother.
Explicit command routing. No LLM intent detection.
"""

from typing import Optional
from .llm_client import LLMClient
from . import prompts
from ..utils.formatter import OutputFormatter


class Controller:
    """
    Routes commands explicitly to their handlers.
    The LLM never decides intent - we do.
    """

    def __init__(self, llm_client: Optional[LLMClient] = None):
        self.llm = llm_client or LLMClient()
        self.formatter = OutputFormatter()

    def run(self, command: str, input_data: str, **flags) -> str:
        """
        Execute a command with explicit routing.
        
        Args:
            command: The command to execute (name, commit, comment, pr, squash, explain)
            input_data: The input data for the command
            **flags: Additional flags (currently unused, kept for compatibility)
            
        Returns:
            The result of the command execution
            
        Raises:
            ValueError: If command is not supported
        """
        command = command.lower().strip()
        
        if command == "name":
            return self._handle_name(input_data)
        elif command == "commit":
            return self._handle_commit(input_data)
        elif command == "comment":
            return self._handle_comment(input_data)
        elif command == "pr":
            return self._handle_pr(input_data)
        elif command == "squash":
            return self._handle_squash(input_data)
        elif command == "explain":
            return self._handle_explain(input_data)
        else:
            raise ValueError(
                f"Unsupported command: '{command}'. "
                f"Supported commands: name, commit, comment, pr, squash, explain"
            )

    def _handle_name(self, context: str) -> str:
        """Generate a name suggestion."""
        prompt = prompts.prompt_name(context)
        result = self.llm.ask(prompt, temperature=0.7)
        return self.formatter.clean_output(result)

    def _handle_commit(self, changes: str) -> str:
        """Generate a commit message."""
        prompt = prompts.prompt_commit(changes)
        result = self.llm.ask(prompt, temperature=0.5)
        return self.formatter.clean_output(result)

    def _handle_comment(self, commits_or_data: str) -> str:
        """Generate informal, detailed summary of recent changes."""
        commits = commits_or_data.split("\n") if commits_or_data else []
        prompt = prompts.prompt_comment(commits)
        result = self.llm.ask(prompt, temperature=0.7)
        return self.formatter.clean_output(result)

    def _handle_pr(self, commits_or_data: str) -> str:
        """Generate formal PR description (title + bullets)."""
        commits = commits_or_data.split("\n") if commits_or_data else []
        prompt = prompts.prompt_comment_pr(commits)
        result = self.llm.ask(prompt, temperature=0.6)
        return self.formatter.format_pr_comment(result)

    def _handle_squash(self, commits_or_data: str) -> str:
        """Generate single commit message for squash merge."""
        commits = commits_or_data.split("\n") if commits_or_data else []
        prompt = prompts.prompt_comment_squash(commits)
        result = self.llm.ask(prompt, temperature=0.5)
        return self.formatter.clean_output(result)

    def _handle_explain(self, content: str) -> str:
        """Explain code or concepts."""
        prompt = prompts.prompt_explain(content)
        result = self.llm.ask(prompt, temperature=0.7)
        return self.formatter.clean_output(result)
