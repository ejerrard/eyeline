import feedparser
import hashlib
import json
import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
FEEDS_FILE = BASE_DIR / "feeds.yaml"
HISTORY_FILE = BASE_DIR / "rss_history.json"


def load_feeds() -> list[dict]:
    """
    Loads RSS feeds from the tiered feeds.yaml file and returns a flat list of feed entries.
    Each entry is a dict with 'name' and 'url' keys.
    """

    def walk(node, prefix=None):
        feeds = []
        prefix = prefix or []
        for key, value in node.items():
            if isinstance(value, dict) and "url" in value:
                feeds.append({"name": " - ".join(prefix + [key]), "url": value["url"]})
            else:
                feeds.extend(walk(value, prefix + [key]))
        return feeds

    with FEEDS_FILE.open("r") as f:
        data = yaml.safe_load(f)
        return walk(data)


def hash_item(item) -> str:
    """
    Generates a unique hash for an RSS item based on its link, title, and published date.
    """

    key = f"{item.link}{item.get('title', '')}{item.get('published', '')}"
    return hashlib.sha256(key.encode()).hexdigest()


def fetch_items(rss_url: str) -> list:
    """
    Fetches and returns items from an RSS feed.
    """

    feed = feedparser.parse(rss_url)
    return feed.entries


def get_new_items(rss_url: str) -> tuple[list, bool]:
    """
    Fetches items from an RSS feed and returns new items.
    Also returns whether this is the first run for the given RSS URL.
    """
    try:
        with HISTORY_FILE.open("r") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = {}

    is_first_run = rss_url not in history

    rss_history = set(history.get(rss_url, []))
    rss_latest = fetch_items(rss_url)
    rss_new = []

    for item in rss_latest:
        item_hash = hash_item(item)
        if item_hash in rss_history:
            continue

        rss_history.add(item_hash)
        rss_new.append(item)

    history[rss_url] = list(rss_history)

    with HISTORY_FILE.open("w") as f:
        json.dump(history, f, indent=2)

    return rss_new, is_first_run
