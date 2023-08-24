from rest_framework import reverse
from rest_framework import serializers
from rest_framework.fields import IntegerField

from .models import Artist, Album, Track


class ArtistImageField(serializers.Field):
    def get_attribute(self, instance):
        return instance

    def to_representation(self, instance):
        if instance.image:
            return instance.image.file.url

        return None


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    image = ArtistImageField()

    class Meta:
        model = Artist
        fields = ["id", "name", "image"]


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = ["id", "name"]


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ["id", "name", "tracks"]


class ArtistImageDetailedAlbumField(serializers.Field):
    def get_attribute(self, instance):
        return instance

    def to_representation(self, instance):
        if instance.artist.image:
            return instance.artist.image.file.url

        return None


class DetailedAlbumSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.StringRelatedField()
    image = ArtistImageDetailedAlbumField()
    track_count = serializers.IntegerField()
    total_duration = serializers.IntegerField()
    min_duration = serializers.IntegerField()
    max_duration = serializers.IntegerField()

    class Meta:
        model = Album
        fields = [
            "id",
            "name",
            "artist",
            "track_count",
            "total_duration",
            "min_duration",
            "max_duration",
            "image",
        ]
