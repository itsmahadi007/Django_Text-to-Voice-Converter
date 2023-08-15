from django.urls import path, include
from rest_framework import routers

from apps.text_to_speech.views import txt_to_audio_view

route = routers.DefaultRouter()
# route.register("users", UserViewSet)
urlpatterns = [
    path("", include(route.urls)),

    path("txt_to_audio/", txt_to_audio_view),
]
