"""
Unified LLM client supporting OpenRouter (any model) and local inference (Ollama).

Usage:
    # OpenRouter (default)
    client = LLMClient(provider="openrouter", model="google/gemini-2.0-flash-001")

    # Local Ollama
    client = LLMClient(provider="local", model="qwen3:72b", base_url="http://localhost:11434/v1")
"""

import os
import re
from typing import Dict, Optional

try:
    from openai import OpenAI
except ImportError:
    raise ImportError("Please install openai: pip install openai")


class LLMClient:
    """Unified client for OpenRouter and local (Ollama/vLLM) inference."""

    OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
    OLLAMA_BASE_URL = "http://localhost:11434/v1"

    def __init__(
        self,
        provider: str = "openrouter",
        model: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
    ):
        """
        Args:
            provider: "openrouter" or "local" (Ollama/vLLM/any OpenAI-compatible server)
            model: Model identifier. For OpenRouter, e.g. "google/gemini-2.0-flash-001".
                   For local, e.g. "qwen3:72b".
            api_key: API key (auto-detected from OPENROUTER_API_KEY for openrouter,
                     not needed for local).
            base_url: Override API endpoint.
        """
        self.provider = provider
        self.model = model or self._default_model()

        if provider == "openrouter":
            self.api_key = api_key or os.environ.get("OPENROUTER_API_KEY")
            if not self.api_key:
                raise ValueError(
                    "OPENROUTER_API_KEY not set. Add it to .env or export it."
                )
            self.base_url = base_url or self.OPENROUTER_BASE_URL
        else:
            # Local: no API key needed, default to Ollama
            self.api_key = api_key or "ollama"
            self.base_url = base_url or self.OLLAMA_BASE_URL

        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)

        # Cost tracking
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.request_count = 0

    def _default_model(self) -> str:
        if self.provider == "openrouter":
            return "google/gemini-2.0-flash-001"
        return "qwen3:72b"

    def complete(
        self,
        prompt: str,
        system: Optional[str] = None,
        temperature: float = 0.0,
        max_tokens: int = 8192,
    ) -> str:
        """
        Send a completion request and return the response text.

        Args:
            prompt: User prompt
            system: Optional system prompt
            temperature: Sampling temperature
            max_tokens: Max output tokens

        Returns:
            Response text (stripped)
        """
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        extra = {}
        if self.provider == "openrouter":
            extra["extra_headers"] = {
                "HTTP-Referer": "https://github.com/l-pommeret/THIVLVC",
                "X-Title": "THIVLVC Latin Parser",
            }

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            **extra,
        )

        content = response.choices[0].message.content or ""

        # Track usage
        if hasattr(response, "usage") and response.usage:
            self.total_input_tokens += getattr(response.usage, "prompt_tokens", 0)
            self.total_output_tokens += getattr(response.usage, "completion_tokens", 0)
        self.request_count += 1

        return content.strip()

    def get_stats(self) -> Dict:
        return {
            "provider": self.provider,
            "model": self.model,
            "requests": self.request_count,
            "input_tokens": self.total_input_tokens,
            "output_tokens": self.total_output_tokens,
        }


def extract_conllu(response_text: str) -> str:
    """Extract CoNLL-U block from an LLM response (handles markdown fences)."""
    match = re.search(r'```(?:conllu|text|)\s*\n?(.*?)```', response_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return response_text.strip()
