from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from .serializers import ArtistSerializer, AlbumSerializer
from .models import Artist, Album


class ArtistList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ArtistAlbumList(mixins.ListModelMixin, generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        request = self.request
        pk = self.kwargs["pk"]
        return Artist.objects.get(pk=pk).albums

    def list(self, request, pk):
        queryset = self.get_queryset()
        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AlbumList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Album.objects.prefetch_related("tracks")
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
