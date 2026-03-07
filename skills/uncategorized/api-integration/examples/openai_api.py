# Example: OpenAI API integration (reference only)
import requests


def chat_completion(
    messages: list[dict],
    model: str = "gpt-4",
    api_key: str = "",
) -> dict:
    """Send a chat completion request to OpenAI API."""
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": messages,
        },
    )
    response.raise_for_status()
    return response.json()


def create_embedding(text: str, api_key: str = "") -> list[float]:
    """Create an embedding vector for text."""
    response = requests.post(
        "https://api.openai.com/v1/embeddings",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": "text-embedding-3-small",
            "input": text,
        },
    )
    response.raise_for_status()
    return response.json()["data"][0]["embedding"]
