from django.urls import include, path

from artistsapi.artists import views


urlpatterns = [
    path("artists/", views.ArtistList.as_view()),
    path("artists/<int:pk>/albums/", views.ArtistAlbumList.as_view()),
    path("albums/", views.AlbumList.as_view()),
    path("albums-details/", views.DetailedAlbumList.as_view()),
]
