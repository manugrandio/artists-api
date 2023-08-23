from rest_framework import serializers

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
