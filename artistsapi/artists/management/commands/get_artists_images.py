from os import remove
from concurrent import futures
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.core.files import File

from artistsapi.artists.models import Artist, ArtistImage
from artistsapi.artists.utils.artistimagescrapper import (
    Scrapper,
    PageParsingError,
    ScrappingError,
)


MAX_WORKERS = 10


class Command(BaseCommand):
    help = "Fetch artists images from AllMusic"

    def handle(self, *args, **options):
        artists = self.get_artists()
        if artists:
            max_workers = min(MAX_WORKERS, len(artists))
            with futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                res = executor.map(self.process_artist_image, artists)

            try:
                list(res)
            except Exception as exc:
                raise CommandError(exc.args)

            self.stdout.write(self.style.SUCCESS("Artists images fetched successfully"))
        else:
            self.stdout.write(
                self.style.WARNING(
                    "There are no artists without images. No images to fetch"
                )
            )

    def get_artists(self):
        return Artist.objects.filter(image__isnull=True)

    def process_artist_image(self, artist):
        image_path = self.get_artist_image(artist.name)
        self.store_artist_image(artist, image_path)
        remove(image_path)

    def get_artist_image(self, artist_name):
        try:
            image_path = Scrapper().get_artist_image(artist_name)
        except ScrappingError:
            raise CommandError(f"Error fetching the {artist_name} page")
        except PageParsingError:
            raise CommandError(f"Error parsing the search results for {artist_name}")

        return image_path

    def store_artist_image(self, artist, image_path):
        path = Path(image_path)
        with path.open(mode="rb") as f:
            image_file = File(f, name=path.name)
            artist_image = ArtistImage(artist=artist, file=image_file)
            artist_image.save()
