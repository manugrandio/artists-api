from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from .serializers import ArtistsSerializer
from .models.artists import Artists


class ArtistList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Artists.objects.all()
    serializer_class = ArtistsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
