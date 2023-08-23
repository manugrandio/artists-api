from django.test import TestCase

from ..views import ArtistList
from .factories import ArtistFactory


class TestArtistList(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.artists = [ArtistFactory() for _ in range(5)]

    def test_artist_list(self):
        response = self.client.get("/artists/")

        existing_artists_names = [artist.name for artist in self.artists]
        fetched_artists_names = [artist["name"] for artist in response.json()]
        self.assertEqual(fetched_artists_names, existing_artists_names)
