import os
import requests

EYELINE_TOPIC = os.getenv("EYELINE_TOPIC")
assert EYELINE_TOPIC, "EYELINE_TOPIC environment variable must be set"


def notify(message: str) -> None:
    """Send a notification via ntfy."""

    requests.post(f"https://ntfy.sh/{EYELINE_TOPIC}", data=message.encode("utf-8"))
