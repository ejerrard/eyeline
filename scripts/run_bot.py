from dotenv import load_dotenv

load_dotenv()

from app.feeds import get_new_items
from app.notify import notify


def main():
    rss_url = "https://www.aph.gov.au/senate/rss/new_inquiries"

    items, is_first_run = get_new_items(rss_url)

    for item in items:
        print("== Item ==")
        print(f"Title: {item.title}")
        print(f"Link: {item.link}")
        print(f"Published: {item.published}")   
        print(f"Summary: {item.summary}")

        if not is_first_run:
            notify(item.summary)
    
    if is_first_run:
        print("This is the first run for this RSS URL. No previous items to compare against.")
    
    if not items:
        print("No new items found in the RSS feed.")


if __name__ == "__main__":
    main()
