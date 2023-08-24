from rest_framework import serializers
from rest_framework.fields import IntegerField

from .models import Artist, Album, Track


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "name"]


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = ["id", "name"]


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ["id", "name", "tracks"]


class DetailedAlbumSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.StringRelatedField()
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
        ]
