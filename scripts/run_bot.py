from app.feeds import fetch_items


def main():
    rss_url = "https://parlinfo.aph.gov.au/parlInfo/feeds/rss.w3p;adv=yes;orderBy=date-eFirst;page=0;query=Date%3AthisYear%20Dataset%3Abillsdgs;resCount=100"  # Official APH bills feed
    items = fetch_items(rss_url)

    for item in items:
        print(f"Title: {item.title}")
        print(f"Link: {item.link}")
        print(f"Published: {item.published}")
        print("---")


if __name__ == "__main__":
    main()
