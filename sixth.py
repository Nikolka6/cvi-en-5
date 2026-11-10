
import sys
import requests
from html.parser import HTMLParser


class HrefParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href" and value is not None:
                    self.hrefs.append(value)


def download_url_and_get_all_hrefs(url):
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Chyba při stahování stránky")
        hrefs = re.findall(r'<a[^>]*href=["\']([^"\']+)["\']',)

    parser = HrefParser()
    parser.feed(response.text)

    return parser.hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)
        print(hrefs)

    except Exception as e:
        print(f"Program skončil s chybou: {e}")
