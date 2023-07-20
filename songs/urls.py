from django.urls import path

from . import views
from .views import SongView

urlpatterns = [
    path("songs/", SongView.as_view()),
]
