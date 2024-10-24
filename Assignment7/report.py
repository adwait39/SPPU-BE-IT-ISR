def print_report(pages):
    """Prints a report of all crawled pages and the number of links found."""
    print("=============================")
    print("REPORT")
    print("=============================")
    sorted_pages = sort_pages(pages)

    for url, hits in sorted_pages:
        print(f"Found {hits} links on page: {url}")

    print("=============================")
    print("END REPORT")
    print("=============================")

def sort_pages(pages):
    """Sorts pages based on the number of hits."""
    return sorted(pages.items(), key=lambda item: item[1], reverse=True)
