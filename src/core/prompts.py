"""
Prompt templates for sinner agent.
Each action gets its own focused prompt.
"""


def prompt_name(context: str) -> str:
    """Prompt for naming things (variables, functions, classes, etc.)"""
    return f"""You are a senior software architect focused on naming conventions.

Given this context:
{context}

Provide a concise, meaningful, and professional name following best practices.
Consider:
- Clarity and expressiveness
- Standard naming conventions (camelCase, snake_case, PascalCase as appropriate)
- Domain context and purpose

Respond with ONLY the suggested name. No explanations, no alternatives, no commentary."""


def prompt_commit(changes: str) -> str:
    """Prompt for generating commit messages"""
    return f"""You are a technical lead reviewing changes for a git commit.

Changes:
{changes}

Write a clear, professional commit message following conventional commits format.
- Use imperative mood ("add" not "added")
- Be concise but descriptive
- Start with type: feat, fix, refactor, docs, style, test, chore
- Keep subject line under 72 characters

Respond with ONLY the commit message. No explanations."""


def prompt_comment_squash(commits: list[str]) -> str:
    """Prompt for squash merge comments"""
    commits_text = "\n\n".join(f"- {c}" for c in commits)
    return f"""You are creating a squash merge summary for a pull request.

Commits being squashed:
{commits_text}

Write a clear, professional summary of what these commits accomplish together.
- Focus on the overall outcome, not individual commits
- Use past tense
- 2-4 short paragraphs maximum
- No emojis, no markdown headers
- Professional tone

Respond with ONLY the summary text."""


def prompt_comment_merge(commits: list[str]) -> str:
    """Prompt for merge request / pull request comments"""
    commits_text = "\n\n".join(f"- {c}" for c in commits)
    return f"""You are writing a merge/pull request description.

Recent commits:
{commits_text}

Write a clear, professional description for this merge request.
- Explain what changed and why
- Highlight key improvements or fixes
- 2-4 short paragraphs maximum
- No emojis, no markdown headers
- Professional tone

Respond with ONLY the description text."""


def prompt_explain(code_or_concept: str) -> str:
    """Prompt for explaining code or concepts"""
    return f"""You are a technical mentor explaining a concept clearly and concisely.

{code_or_concept}

Provide a clear explanation:
- Start with the core idea
- Be precise but accessible
- Use 2-3 short paragraphs
- Avoid unnecessary jargon
- No emojis

Respond with ONLY the explanation."""
