from django.urls import include, path

from artistsapi.artists import views as artists_views
from utils.passphrases import views as passphrase_views


urlpatterns = [
    path("artists/", artists_views.ArtistList.as_view()),
    path("artists/<int:pk>/albums/", artists_views.ArtistAlbumList.as_view()),
    path("albums/", artists_views.AlbumList.as_view()),
    path("albums-details/", artists_views.DetailedAlbumList.as_view()),
    path("passphrase/basic/", passphrase_views.BasicPassphrase.as_view()),
    path("passphrase/advanced/", passphrase_views.AdvancedPassphrase.as_view()),
]
