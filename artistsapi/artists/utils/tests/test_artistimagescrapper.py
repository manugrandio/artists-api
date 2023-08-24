from unittest import TestCase

from ..artistimagescrapper import SearchPage


class TestSearchPage(TestCase):
    def test_get_image_url(self):
        img_src = "https://www.images.com/the-image.jpg"
        html = f"""\
        <div>
            <ul class="search-results">
                <li class="artist">
                    <div class="photo">
                        <a>
                            <img src="{img_src}">
                        </a>
                    </div>
                    <div class="info">
                        <h4>Artist</h4>
                    </div>
                </li>
            </ul>
        </div>
        """

        fetched_img_src = SearchPage(html).get_image_url()

        self.assertEqual(fetched_img_src, img_src)
