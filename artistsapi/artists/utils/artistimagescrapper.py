from urllib.parse import quote, urlsplit

from django.conf import settings
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://www.allmusic.com"
# It looks like the service doesn't return results if the user agent isn't mocked
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/116.0"


class ScrappingError(Exception):
    pass


class Scrapper:
    def get_artist_image(self, artist_name):
        artist_search = quote(artist_name)
        headers = {
            "User-Agent": USER_AGENT,
        }
        search_response = requests.get(
            f"{BASE_URL}/search/artists/{artist_search}", headers=headers
        )
        search_response.raise_for_status()
        image_url = SearchPage(search_response.content).get_image_url()

        image_path = settings.MEDIA_ROOT / artist_name
        with requests.get(image_url, stream=True) as image_response:
            image_response.raise_for_status()
            image_extension = urlsplit(image_url).path.split(".")[-1]
            with open(f"{image_path}.{image_extension}", "wb") as f:
                for chunk in image_response.iter_content(chunk_size=8192):
                    f.write(chunk)

        return image_path


class PageParsingError(Exception):
    pass


class SearchPage:
    def __init__(self, html_doc):
        self.soup = BeautifulSoup(html_doc, "html.parser")

    def get_image_url(self):
        """
        Apply the following heuristics: assume the first result in the search list is the right one
        """
        try:
            search_results = self.soup.find(class_="search-results")
            artist_li = search_results.find_all("li")[0]
            photo_div = artist_li.find(class_="photo")
            img = photo_div.find("img")
            return img["src"]
        except:
            raise PageParsingError
