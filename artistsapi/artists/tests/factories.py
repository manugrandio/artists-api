import random
import factory
from factory.django import DjangoModelFactory

from ..models import Artist, Album, Track


class ArtistFactory(DjangoModelFactory):
    class Meta:
        model = Artist

    name = factory.Faker("name")


class AlbumFactory(DjangoModelFactory):
    class Meta:
        model = Album

    name = factory.Faker("name")
    artist = factory.SubFactory(ArtistFactory)


class TrackFactory(DjangoModelFactory):
    class Meta:
        model = Track

    name = factory.Faker("name")
    album = factory.SubFactory(AlbumFactory)
    milliseconds = factory.LazyAttribute(lambda obj: random.randrange(1_000, 1_000_000))
