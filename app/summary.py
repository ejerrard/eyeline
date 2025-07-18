"""
summary.py  –  tiny Cohere wrapper
"""

import os

import cohere

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
assert COHERE_API_KEY, "COHERE_API_KEY environment variable must be set"

co = cohere.ClientV2(api_key=COHERE_API_KEY)

MODEL = "command-light"  # good, fast, free
MESSAGE = "Generate a concise summary of this text\n{text}"


def summarise(text: str) -> str:
    """
    Returns a short plain‑English summary of `text`.
    """

    response = co.chat(
        model=MODEL,
        messages=[{"role": "user", "content": MESSAGE.format(text=text)}],  # type: ignore[call-arg]
    )

    return response.message.content[0].text  # type: ignore[return-value]
