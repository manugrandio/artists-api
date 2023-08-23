from django.test import TestCase
from django.contrib.auth.models import User

from ..views import ArtistList
from .factories import ArtistFactory, AlbumFactory, TrackFactory


class TestArtistList(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.artists = [ArtistFactory() for _ in range(5)]

    def test_artist_list(self):
        response = self.client.get("/artists/")

        existing_artists_names = [artist.name for artist in self.artists]
        fetched_artists_names = [artist["name"] for artist in response.json()]
        self.assertEqual(sorted(fetched_artists_names), sorted(existing_artists_names))


class TestAlbumList(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.albums = [AlbumFactory(), AlbumFactory()]
        tracks = [
            TrackFactory(album=cls.albums[0]),
            TrackFactory(album=cls.albums[1]),
            TrackFactory(album=cls.albums[1]),
        ]
        User.objects.create_user("john", "john@mail.com", "password")

    def test_album_list_without_auth(self):
        response = self.client.get("/albums/")

        self.assertEqual(response.status_code, 403)

    def test_album_list(self):
        self.client.login(username="john", password="password")
        response = self.client.get("/albums/")

        fetched_albums_tracks = [
            [track["name"] for track in album["tracks"]] for album in response.json()
        ]
        existing_albums_tracks = [
            [track.name for track in album.tracks.all()] for album in self.albums
        ]
        self.assertEqual(sorted(fetched_albums_tracks), sorted(existing_albums_tracks))
