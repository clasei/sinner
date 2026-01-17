"""
Light git integration for reading commit history.
No diff parsing today.
"""

import subprocess
from typing import Optional


class GitIntegration:
    """Read commit messages from git repositories."""

    @staticmethod
    def get_recent_commits(count: int = 5, since: Optional[str] = None) -> list[str]:
        """
        Get recent commit messages from the current repository.
        
        Args:
            count: Number of commits to retrieve (default: 5)
            since: Optional date string (e.g., "2 weeks ago", "2024-01-01")
            
        Returns:
            List of commit messages
            
        Raises:
            RuntimeError: If not in a git repository or git command fails
        """
        try:
            cmd = ["git", "log", f"-{count}", "--pretty=format:%s"]
            
            if since:
                cmd.insert(2, f"--since={since}")
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            
            commits = [line.strip() for line in result.stdout.split("\n") if line.strip()]
            return commits
            
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Git command failed: {e.stderr.strip()}")
        except FileNotFoundError:
            raise RuntimeError("Git not found. Is git installed?")

    @staticmethod
    def is_git_repo() -> bool:
        """Check if current directory is in a git repository."""
        try:
            subprocess.run(
                ["git", "rev-parse", "--git-dir"],
                capture_output=True,
                check=True
            )
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
