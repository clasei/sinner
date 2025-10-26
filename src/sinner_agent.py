import os
import requests
from dotenv import load_dotenv

load_dotenv()  # reads your .env file

class SinnerAgent:
    """
    SinnerAgent — disciplined rule-breaker.
    Generates expressive names and meaningful commit messages
    with the calm precision of Jannik Sinner.
    """

    def __init__(self):
        self.base_url = os.getenv("LMSTUDIO_BASE_URL", "http://127.0.0.1:1234/v1").rstrip("/")
        self.api_key = os.getenv("LMSTUDIO_API_KEY", "lm-studio")
        self.model = os.getenv("MODEL_ID", "google/gemma-3-4b")
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def _ask(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
        }
        resp = requests.post(f"{self.base_url}/chat/completions",
                             headers=self.headers, json=payload, timeout=30)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"].strip()


    def suggest_name(self, context: str) -> str:
        return self._ask(
            f"You are a senior software architect. "
            f"Decide whether the user request is about naming or about a commit message.\n\n"
            f"Context:\n{context}\n\n"
            f"If it's about naming, suggest a concise, meaningful, and professional name "
            f"following best practices in Java, Python, or general OOP style. "
            f"Provide only the name unless an explanation is explicitly requested.\n\n"
            f"If it's about a commit, write a short, sweet, and professional conventional-style "
            f"git commit message describing the change.\n"
        )


    def synthesize_commit(self, changes: str) -> str:
        return self._ask(f"Write a short, conventional-style git commit message for:\n{changes}")

if __name__ == "__main__":
    agent = SinnerAgent()
    print("class →", agent.suggest_name("a class that manages authentication tokens for API requests"))
    print("commit →", agent.synthesize_commit("refactored authentication module for token reuse"))
