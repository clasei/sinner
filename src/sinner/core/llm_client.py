"""
Core LLM client for sinner.
Handles communication with LM Studio (local-first).
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()


class LLMClient:
    """
    Local-first LLM client.
    Communicates with LM Studio for all LLM operations.
    """

    def __init__(self):
        self.base_url = os.getenv("LMSTUDIO_BASE_URL", "http://127.0.0.1:1234/v1").rstrip("/")
        self.api_key = os.getenv("LMSTUDIO_API_KEY", "lm-studio")
        self.model = os.getenv("MODEL_ID", "google/gemma-3-4b")
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def ask(self, prompt: str, temperature: float = 0.7) -> str:
        """
        Send a prompt to the LLM and return the response.
        
        Args:
            prompt: The prompt to send
            temperature: Sampling temperature (default: 0.7)
            
        Returns:
            The LLM's response as a string
        """
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
        }
        
        try:
            resp = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=30
            )
            resp.raise_for_status()
            return resp.json()["choices"][0]["message"]["content"].strip()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"LLM request failed: {e}")
