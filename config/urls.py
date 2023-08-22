from django.urls import include, path

from rest_framework import routers

from artistsapi.artists import views

router = routers.DefaultRouter()
router.register(r"artists", views.ArtistsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
