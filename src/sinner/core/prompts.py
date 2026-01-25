"""
Prompt templates for sinner agent.
Each action gets its own focused prompt.
"""


def prompt_name(context: str) -> str:
    """Prompt for naming things (variables, functions, classes, etc.)"""
    return f"""You are a senior software architect focused on clean naming conventions.

Context:
{context}

Provide a concise, meaningful, professional name following best practices:
- Use camelCase for functions/methods and variables (JavaScript, Java, etc.)
- Use snake_case for Python functions/variables
- Use PascalCase for classes in all languages
- Use UPPER_SNAKE_CASE for constants
- Be descriptive but not verbose
- Infer the language from context clues when possible
- Default to camelCase if language is ambiguous

Examples:
- "a function that validates emails" → validateEmail (or validate_email for Python)
- "a class for user sessions" → UserSession
- "maximum retry count constant" → MAX_RETRY_COUNT
- "variable storing user authentication token" → authToken (or auth_token for Python)

Respond with ONLY the suggested name. No explanations, no alternatives."""


def prompt_commit(changes: str) -> str:
    """Prompt for generating commit messages"""
    return f"""You are a technical lead writing a git commit message.

User's description of changes:
{changes}

Create a commit message in this EXACT format:
type(scope) -> description

Rules:
- Silently fix any typos or grammar errors
- Infer the best scope from context (e.g., ui, api, auth, home, db, config, tests)
- Use imperative mood ("make" not "made", "add" not "added", "fix" not "fixed")
- Make description clear and professional
- Description starts with lowercase letter
- Keep total length under 72 characters
- Common types: feat, fix, refactor, docs, style, test, chore, perf

Examples:
- "made table resonsive on home screen" (typo intentional) → feat(home) -> make table responsive on home screen
- "fixed bug in login" → fix(auth) -> resolve login validation error
- "updated readme" → docs(readme) -> update installation instructions
- "refactored api endpoints" → refactor(api) -> improve endpoint structure
- "added new components" → feat(ui) -> add new building blocks for user dashboard

Respond with ONLY the commit message. No explanations, no alternatives."""


def prompt_comment_squash(commits: list[str]) -> str:
    """Prompt for generating a single squash merge commit message"""
    commits_text = "\n\n".join(f"- {c}" for c in commits)
    return f"""Create ONE commit message that summarizes all these commits together.

Commits to squash:
{commits_text}

Output format: type(scope) -> description

Rules:
- ONE line only
- Format: type(scope) -> description
- Imperative mood (add, fix, update)
- Description starts with lowercase letter
- Under 72 characters
- Capture the main change across all commits

Examples:
- feat(auth) -> add JWT authentication system
- docs(install) -> update setup instructions for venv and pipx
- refactor(core) -> improve prompt handling and formatting

Your single commit message:"""


def prompt_comment_pr(commits: list[str]) -> str:
    """Prompt for PR descriptions (title + bullets)"""
    commits_text = "\n\n".join(f"- {c}" for c in commits)
    return f"""Summarize what changed.

Commits:
{commits_text}

Technical, simple, precise. No filler. To the point."""


def prompt_comment(commits: list[str]) -> str:
    """Prompt for informal, detailed summaries of recent work"""
    commits_text = "\n\n".join(f"- {c}" for c in commits)
    return f"""Summarize these recent changes in a casual, detailed way. Talk to the developer like a friendly colleague catching them up on what's been happening.

Recent commits:
{commits_text}

Style:
- Start with a casual greeting like "Hey!" or "So," 
- Use passive voice (things "were added", "got updated", not "we added")
- Conversational and natural tone
- Technical but not formal
- Include details about what changed and why
- 2-3 sentences max
- No bullet points, just flowing prose

Example: "Hey! So the auth system got a nice refactoring - JWT handling was moved into a separate service and refresh token support was added. Error handling also got cleaned up to make expired sessions more graceful."

Your summary:"""


def prompt_explain(code_or_concept: str) -> str:
    """Prompt for explaining code or concepts"""
    return f"""Explain this concept clearly and concisely.

{code_or_concept}

Guidelines:
- Start with core idea in one sentence
- Use 2-3 short paragraphs maximum
- Add a LEGO analogy if it helps
- Be technical but accessible
- Optional: subtle dev humor if natural
- No fluff, stay focused

Respond with explanation only."""
