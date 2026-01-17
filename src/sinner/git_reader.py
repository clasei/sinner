"""
Light git integration for sinner.
Reads commit history without parsing diffs.
"""

import subprocess
from typing import List, Optional


class GitReader:
    """
    Light git integration.
    Reads commit messages only (no diff parsing).
    """

    @staticmethod
    def get_recent_commits(count: int = 5, since: Optional[str] = None) -> List[str]:
        """
        Get recent commit messages from the current repository.
        
        Args:
            count: Number of commits to fetch (default: 5)
            since: Optional date/time string (e.g., "2 weeks ago", "2024-01-01")
            
        Returns:
            List of commit messages
            
        Raises:
            RuntimeError: If not in a git repository or git command fails
        """
        try:
            # Build git log command
            cmd = ["git", "log", f"-{{count}}", "--pretty=format:%s"]
            
            if since:
                cmd.append(f"--since={{since}}")
            
            # Execute git command
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True,
                timeout=5
            )
            
            # Parse output
            commits = result.stdout.strip().split("\n")
            return [c for c in commits if c]  # Filter empty lines
            
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Git command failed: {{e.stderr}}")
        except FileNotFoundError:
            raise RuntimeError("Git is not installed or not in PATH")
        except subprocess.TimeoutExpired:
            raise RuntimeError("Git command timed out")

    @staticmethod
    def is_git_repo() -> bool:
        """Check if current directory is a git repository."""
        try:
            subprocess.run(
                ["git", "rev-parse", "--git-dir"],
                capture_output=True,
                check=True,
                timeout=2
            )
            return True
        except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
            return False