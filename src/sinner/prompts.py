"""
Tight, focused prompts for sinner.
One prompt per action. No mega-prompts.
"""

def prompt_name(context: str) -> str:
    """Generate a naming suggestion prompt."""
    return f"""You are a senior software architect.

Suggest a concise, meaningful, and professional name for:
{context}

Follow best practices for naming in Python, Java, or general OOP style.
Provide only the name. No explanation unless explicitly requested."""

def prompt_commit(changes: str) -> str:
    """Generate a commit message prompt."""
    return f"""Write a short, conventional-style git commit message.

Changes:
{changes}

Format: <type>: <description>
Types: feat, fix, docs, style, refactor, test, chore

Keep it under 72 characters. Be specific and professional."""

def prompt_comment_default(commits: str) -> str:
    """Generate a default PR comment prompt."""
    return f"""Write a short, professional pull request comment.

Recent commits:
{commits}

Guidelines:
- No emojis
- No markdown noise
- Short paragraphs
- Paste-ready format
- Focus on what changed and why"""

def prompt_comment_squash(commits: str) -> str:
    """Generate a squash PR comment prompt."""
    return f"""Write a professional squash commit message for a pull request.

Commits to squash:
{commits}

Guidelines:
- Single conventional commit format
- Summarize all changes concisely
- No emojis
- No markdown formatting
- Under 72 characters for subject
- Optional body if needed"""

def prompt_comment_merge(commits: str) -> str:
    """Generate a merge PR comment prompt."""
    return f"""Write a professional merge request description.

Commits to merge:
{commits}

Guidelines:
- Clear summary of changes
- Highlight key modifications
- Short paragraphs
- No emojis
- No excessive markdown
- Paste-ready format"""

def prompt_explain(code: str) -> str:
    """Generate a code explanation prompt."""
    return f"""Explain this code clearly and professionally.

Code:
{code}

Guidelines:
- Clear, concise explanation
- Highlight key logic
- Mention any patterns or best practices
- No emojis
- Short paragraphs"""