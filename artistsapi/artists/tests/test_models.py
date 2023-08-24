from django.test import TestCase

from ..models import Album
from ..utils.factories import ArtistFactory, AlbumFactory, TrackFactory


class TestAlbum(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.artists = [ArtistFactory(name="Tortoise"), ArtistFactory(name="Slint")]
        cls.albums = [
            AlbumFactory(artist=cls.artists[0]),
            AlbumFactory(artist=cls.artists[1]),
        ]
        tracks = [
            TrackFactory(album=cls.albums[0], milliseconds=10_000),
            TrackFactory(album=cls.albums[1], milliseconds=5_000),
            TrackFactory(album=cls.albums[1], milliseconds=2_000),
        ]

    def test_get_detailed_album_list(self):
        albums = Album.objects.get_detailed_albums()

        self.assertEqual([album.artist.name for album in albums], ["Tortoise", "Slint"])
        self.assertEqual([album.track_count for album in albums], [1, 2])
        self.assertEqual([album.total_duration for album in albums], [10_000, 7_000])
        self.assertEqual([album.min_duration for album in albums], [10_000, 2_000])
        self.assertEqual([album.max_duration for album in albums], [10_000, 5_000])
