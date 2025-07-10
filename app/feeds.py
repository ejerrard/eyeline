import feedparser


def fetch_items(rss_url: str, max_items: int = 5):
    """
    Fetches and returns items from an RSS feed.
    """

    feed = feedparser.parse(rss_url)
    entries = feed.entries[:max_items]
    return entries
