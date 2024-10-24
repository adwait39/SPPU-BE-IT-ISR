import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def normalize_url(url):
    """Normalizes the URL by removing trailing slashes and converting to lowercase."""
    parsed_url = urlparse(url)
    normalized_url = f"{parsed_url.hostname}{parsed_url.path}".rstrip('/')
    return normalized_url

def get_urls_from_html(html_body, base_url):
    """Extracts all URLs from the HTML body."""
    urls = []
    soup = BeautifulSoup(html_body, 'html.parser')
    for link_element in soup.find_all('a'):
        href = link_element.get('href')
        if href:
            if href.startswith('/'):
                # Relative URL, convert to absolute
                url = urljoin(base_url, href)
                urls.append(url)
            else:
                # Absolute URL
                urls.append(href)
    return urls

def crawl_page(base_url, current_url, pages):
    """Crawls a web page and retrieves all internal links."""
    parsed_base_url = urlparse(base_url)
    parsed_current_url = urlparse(current_url)

    if parsed_base_url.hostname != parsed_current_url.hostname:
        return pages

    normalized_current_url = normalize_url(current_url)
    if normalized_current_url in pages:
        pages[normalized_current_url] += 1
        return pages

    pages[normalized_current_url] = 1
    print(f"Actively crawling: {current_url}")

    try:
        response = requests.get(current_url)
        if response.status_code > 399:
            print(f"Error in fetching with status code: {response.status_code} on page: {current_url}")
            return pages

        if 'text/html' not in response.headers.get('Content-Type', ''):
            print(f"Non-HTML response, content type: {response.headers.get('Content-Type')} on page: {current_url}")
            return pages

        html_body = response.text
        next_urls = get_urls_from_html(html_body, base_url)

        for next_url in next_urls:
            pages = crawl_page(base_url, next_url, pages)
    except requests.RequestException as e:
        print(f"Error fetching from {current_url}: {e}")

    return pages
