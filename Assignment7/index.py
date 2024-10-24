import sys
from crawl import crawl_page
from report import print_report

def main():
    if len(sys.argv) < 2:
        print("No website provided")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("Too many arguments!")
        sys.exit(1)

    base_url = sys.argv[1]
    print(f"Starting crawl of {base_url}")
    
    # Start the crawling process
    pages = crawl_page(base_url, base_url, {})
    
    # Print the report
    print_report(pages)

if __name__ == "__main__":
    main()
