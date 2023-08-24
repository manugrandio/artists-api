from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from artistsapi.artists import views as artists_views
from utils.passphrases import views as passphrase_views


urlpatterns = [
    path("artists/", artists_views.ArtistList.as_view()),
    path("artists/<int:pk>/albums/", artists_views.ArtistAlbumList.as_view()),
    path("albums/", artists_views.AlbumList.as_view()),
    path("albums-details/", artists_views.DetailedAlbumList.as_view()),
    path("passphrase/basic/", passphrase_views.BasicPassphrase.as_view()),
    path("passphrase/advanced/", passphrase_views.AdvancedPassphrase.as_view()),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)  # TODO: not suitable for production
