from rest_framework import viewsets
from rest_framework import permissions

from .serializers import ArtistsSerializer
from .models.artists import Artists


class ArtistsViewSet(viewsets.ModelViewSet):
    queryset = Artists.objects.all()
    serializer_class = ArtistsSerializer
