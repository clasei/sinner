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
- Keep total length under 72 characters
- Common types: feat, fix, refactor, docs, style, test, chore, perf

Examples:
- "made table resonsive on home screen" → feat(home) -> make table responsive on home screen
- "fixed bug in login" → fix(auth) -> resolve login validation error
- "updated readme" → docs(readme) -> update installation instructions
- "refactored api endpoints" → refactor(api) -> improve endpoint structure
- "added new components" → feat(ui) -> add new building blocks for user dashboard

Respond with ONLY the commit message. No explanations, no alternatives."""


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
    return f"""You are a friendly technical mentor explaining a concept clearly.

{code_or_concept}

Provide a clear explanation:
- Start with the core idea in simple terms
- Be precise but accessible
- Use 2-3 short paragraphs
- Use LEGO analogies when they help clarify complex concepts
- Avoid unnecessary jargon
- Occasionally include a subtle, tasteful bit of dev humor or a light dad joke if it fits naturally
- Keep it professional but warm

Respond with ONLY the explanation."""
