"""
Agent controller (the mother).
Routes commands explicitly. LLM does NOT decide intent.
"""

from sinner.core import LLMClient
from sinner import prompts


class SinnerController:
    """
    The mother. Explicit command routing.
    LLM never decides what to do - only how to do it.
    """

    def __init__(self):
        self.llm = LLMClient()

    def run(self, command: str, input_data: str, **flags) -> str:
        """
        Main entry point. Routes by command.
        
        Args:
            command: The command to execute (name, commit, comment, explain)
            input_data: The input context/data
            **flags: Command-specific flags (squash, merge, etc.)
            
        Returns:
            The generated output
            
        Raises:
            ValueError: For unsupported commands
        """
        if command == "name":
            return self._handle_name(input_data)
        elif command == "commit":
            return self._handle_commit(input_data)
        elif command == "comment":
            return self._handle_comment(input_data, **flags)
        elif command == "explain":
            return self._handle_explain(input_data)
        else:
            raise ValueError(f"Unsupported command: {command}")

    def _handle_name(self, context: str) -> str:
        """Generate a naming suggestion."""
        prompt = prompts.prompt_name(context)
        return self.llm.ask(prompt)

    def _handle_commit(self, changes: str) -> str:
        """Generate a commit message."""
        prompt = prompts.prompt_commit(changes)
        return self.llm.ask(prompt)

    def _handle_comment(self, commits: str, **flags) -> str:
        """Generate a PR comment/description."""
        if flags.get("squash"):
            prompt = prompts.prompt_comment_squash(commits)
        elif flags.get("merge"):
            prompt = prompts.prompt_comment_merge(commits)
        else:
            prompt = prompts.prompt_comment_default(commits)
        return self.llm.ask(prompt)

    def _handle_explain(self, code: str) -> str:
        """Explain code."""
        prompt = prompts.prompt_explain(code)
        return self.llm.ask(prompt)