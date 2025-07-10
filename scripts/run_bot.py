from app.feeds import fetch_items


def main():
    rss_url = "https://www.aph.gov.au/senate/rss/new_inquiries"
    items = fetch_items(rss_url)

    for item in items:
        print(f"Title: {item.title}")
        print(f"Link: {item.link}")
        print(f"Published: {item.published}")
        print("---")


if __name__ == "__main__":
    main()
