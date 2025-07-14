"""
summary.py  –  tiny Cohere wrapper
"""

import os

import cohere
from dotenv import load_dotenv

load_dotenv()  # loads .env into env vars

API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.ClientV2(api_key=API_KEY)

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
