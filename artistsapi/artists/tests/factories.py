from factory import Faker
from factory.django import DjangoModelFactory

from ..models import Artist


class ArtistFactory(DjangoModelFactory):
    class Meta:
        model = Artist

    name = Faker("name")
