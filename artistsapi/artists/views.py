from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from .serializers import ArtistSerializer
from .models import Artist


class ArtistList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
