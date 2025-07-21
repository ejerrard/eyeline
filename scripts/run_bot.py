from dotenv import load_dotenv

load_dotenv()

from app.feeds import get_new_items, load_feeds
from app.notify import notify

import logging

logging.basicConfig(level=logging.INFO, format="> %(message)s")


def main():
    feeds = load_feeds()

    for feed in feeds:
        items, is_first_run = get_new_items(feed["url"])

        for item in items:
            logging.info("== Item ==")
            logging.info(f"Title: {item.get('title', '')}")
            logging.info(f"Link: {item.get('link', '')}")
            logging.info(f"Published: {item.get('published', '')}")

            if not is_first_run:
                notify(item.summary)

        if is_first_run:
            logging.info("This is the first run for this RSS URL.")

        if not items:
            logging.info("No new items found in the RSS feed.")


if __name__ == "__main__":
    main()
