from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from artistsapi.artists.utils import factories


class Command(BaseCommand):
    help = "Adds sample data to the database for manual testing"

    def handle(self, *args, **options):
        User.objects.create_user("user", "user@mail.com", "password")

        # Real artists and albums
        tortoise, slint, shellac = [
            factories.ArtistFactory(name=artist)
            for artist in ("Tortoise", "Slint", "Shellac")
        ]
        tnt, standards, catastrophist = [
            factories.AlbumFactory(artist=tortoise, name=album)
            for album in ("TNT", "Standards", "Catastrophist")
        ]
        thousand_hurts, dude_incredible = [
            factories.AlbumFactory(artist=shellac, name=album)
            for album in ("1000 Hurts", "Dude Incredible")
        ]
        spiderland = factories.AlbumFactory(artist=slint, name="Spiderland")

        albums = [
            tnt,
            standards,
            catastrophist,
            thousand_hurts,
            dude_incredible,
            spiderland,
        ]

        # Fake number of tracks and track titles
        for album in albums:
            for _ in range(12):
                factories.TrackFactory(album=album)

        self.stdout.write(self.style.SUCCESS("This nice command is running"))
