from rest_framework import serializers

from .models.artists import Artists


class ArtistsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artists
        fields = ["artistid", "name"]
