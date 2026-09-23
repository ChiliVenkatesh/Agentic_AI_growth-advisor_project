import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

_client = None


def _get_client():
    global _client
    if _client is None:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not set in .env")
        _client = genai.Client(api_key=api_key)
    return _client


def ask_llm(system_prompt: str, user_prompt: str, max_tokens: int = 1500) -> str:
    """Send a single-turn prompt to Gemini and return plain text."""
    client = _get_client()
    model_name = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite")
    response = client.models.generate_content(
        model=model_name,
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            max_output_tokens=max_tokens,
        ),
    )
    return response.text