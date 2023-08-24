from django.urls import include, path

from artistsapi.artists import views
from utils import passphrase_views


urlpatterns = [
    path("artists/", views.ArtistList.as_view()),
    path("artists/<int:pk>/albums/", views.ArtistAlbumList.as_view()),
    path("albums/", views.AlbumList.as_view()),
    path("albums-details/", views.DetailedAlbumList.as_view()),
    path("passphrase/basic/", passphrase_views.BasicPassphrase.as_view()),
    path("passphrase/advanced/", passphrase_views.AdvancedPassphrase.as_view()),
]
