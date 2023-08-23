from django.urls import include, path

from artistsapi.artists import views

urlpatterns = [
    path("artists/", views.ArtistList.as_view()),
]
