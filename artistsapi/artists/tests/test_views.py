from django.test import TestCase
from django.contrib.auth.models import User

from ..views import ArtistList
from ..utils.factories import ArtistFactory, AlbumFactory, TrackFactory


class TestArtistList(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.artists = [ArtistFactory() for _ in range(5)]

    def test_artist_list(self):
        response = self.client.get("/artists/")

        existing_artists_names = [artist.name for artist in self.artists]
        fetched_artists_names = [
            artist["name"] for artist in response.json()["results"]
        ]
        self.assertEqual(sorted(fetched_artists_names), sorted(existing_artists_names))


class TestArtistAlbumList(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.artist = ArtistFactory()
        cls.albums = [AlbumFactory(artist=cls.artist) for _ in range(3)]
        User.objects.create_user("john", "john@mail.com", "password")

    def test_album_list_without_auth(self):
        response = self.client.get(f"/artists/{self.artist.pk}/albums/")

        self.assertEqual(response.status_code, 403)

    def test_album_list_404(self):
        self.client.login(username="john", password="password")

        response = self.client.get(f"/artists/10000/albums/")

        self.assertEqual(response.status_code, 404)

    def test_artist_album_list(self):
        self.client.login(username="john", password="password")

        response = self.client.get(f"/artists/{self.artist.pk}/albums/")

        existing_album_names = [album.name for album in self.albums]
        fetched_album_names = [album["name"] for album in response.json()["results"]]
        self.assertEqual(sorted(existing_album_names), sorted(fetched_album_names))


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
            [track["name"] for track in album["tracks"]]
            for album in response.json()["results"]
        ]
        existing_albums_tracks = [
            [track.name for track in album.tracks.all()] for album in self.albums
        ]
        self.assertEqual(sorted(fetched_albums_tracks), sorted(existing_albums_tracks))


class TestDetailedAlbumList(TestCase):
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
        ]
        User.objects.create_user("john", "john@mail.com", "password")

    def test_album_list_without_auth(self):
        response = self.client.get("/albums-details/")

        self.assertEqual(response.status_code, 403)

    def test_get_detailed_album_list(self):
        self.client.login(username="john", password="password")

        response = self.client.get("/albums-details/")

        fetched_albums = sorted(
            response.json()["results"], key=lambda album: album["id"]
        )
        self.assertEqual(
            [album["artist"] for album in fetched_albums], ["Tortoise", "Slint"]
        )
        self.assertEqual([album["track_count"] for album in fetched_albums], [1, 1])
