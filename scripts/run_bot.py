from app.feeds import fetch_items
from app.summary import summarise


def main():
    rss_url = "https://www.aph.gov.au/senate/rss/new_inquiries"

    items = fetch_items(rss_url, max_items=1)  # fetch just the latest item

    for item in items:
        raw_text = f"{item.title}\n\n{getattr(item, 'summary', '')}"
        summary = summarise(raw_text)

        print("== Item ==")
        print(f"Title: {item.title}")
        print(f"Link: {item.link}")
        print(f"Published: {item.published}")

        print("== Summary ==")
        print(summary)


if __name__ == "__main__":
    main()
