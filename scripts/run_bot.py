from dotenv import load_dotenv

load_dotenv()

import logging

from app.feeds import get_new_items, load_feeds
from app.notify import notify

logging.basicConfig(level=logging.INFO, format="> %(message)s")


def main():
    feeds = load_feeds()

    for feed in feeds:
        new_items, is_first_run = get_new_items(feed["url"])

        for item in new_items:
            details = (
                f"Feed: {feed['name']}\n"
                f"Title: {item.get('title', '')}\n"
                f"Link: {item.get('link', '')}\n"
                f"Published: {item.get('published', '')}"
            )

            if not is_first_run:
                logging.info(details)
                notify(details)

        if is_first_run:
            logging.info(f"This is the first run for the RSS feed: {feed['name']}")


if __name__ == "__main__":
    main()
