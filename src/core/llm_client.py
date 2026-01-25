import os
import requests
from dotenv import load_dotenv

load_dotenv()


class LLMClient:
    """
    Isolated LLM client for interacting with LM Studio.
    Handles all direct API communication.
    """

    def __init__(self):
        self.base_url = os.getenv("LMSTUDIO_BASE_URL", "http://127.0.0.1:1234/v1").rstrip("/")
        self.api_key = os.getenv("LMSTUDIO_API_KEY", "lm-studio")
        self.model = os.getenv("MODEL_ID", "google/gemma-3n-e4b")
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def ask(self, prompt: str, temperature: float = 0.7) -> str:
        """
        Send a prompt to the LLM and return the response.
        
        Args:
            prompt: The prompt to send
            temperature: The temperature for generation (default: 0.7)
            
        Returns:
            The LLM's response as a string
            
        Raises:
            requests.exceptions.HTTPError: If the API request fails
        """
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
        }
        resp = requests.post(
            f"{self.base_url}/chat/completions",
            headers=self.headers,
            json=payload,
            timeout=30
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"].strip()
