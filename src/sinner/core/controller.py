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
            command: The command to execute (name, commit, comment, explain)
            input_data: The input data for the command
            **flags: Additional flags (squash, merge, etc.)
            
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
            return self._handle_comment(input_data, **flags)
        elif command == "explain":
            return self._handle_explain(input_data)
        else:
            raise ValueError(
                f"Unsupported command: '{command}'. "
                f"Supported commands: name, commit, comment, explain"
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

    def _handle_comment(self, commits_or_data: str, **flags) -> str:
        """Generate a comment for squash or merge."""
        commits = commits_or_data.split("\n") if commits_or_data else []
        
        if flags.get("squash"):
            prompt = prompts.prompt_comment_squash(commits)
        elif flags.get("merge"):
            prompt = prompts.prompt_comment_merge(commits)
        else:
            # Default to merge style
            prompt = prompts.prompt_comment_merge(commits)
        
        result = self.llm.ask(prompt, temperature=0.6)
        return self.formatter.clean_output(result)

    def _handle_explain(self, content: str) -> str:
        """Explain code or concepts."""
        prompt = prompts.prompt_explain(content)
        result = self.llm.ask(prompt, temperature=0.7)
        return self.formatter.clean_output(result)
