from rest_framework import mixins
from rest_framework import exceptions
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from .serializers import ArtistSerializer, AlbumSerializer, DetailedAlbumSerializer
from .models import Artist, Album


class ArtistList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Artist.objects.prefetch_related("image").all()
    serializer_class = ArtistSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ArtistAlbumList(mixins.ListModelMixin, generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AlbumSerializer

    def get_queryset(self):
        artist_pk = self.kwargs["pk"]
        try:
            return Artist.objects.get_artist_albums(artist_pk)
        except Artist.DoesNotExist:
            raise exceptions.NotFound

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AlbumList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Album.objects.prefetch_related("tracks")
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class DetailedAlbumList(mixins.ListModelMixin, generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DetailedAlbumSerializer

    def get_queryset(self):
        return Album.objects.get_detailed_albums()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
