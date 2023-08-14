from django.urls import path
from .views import *

urlpatterns = [
    path('videos/', VideoListAPI.as_view(), name='video-list'),
    path('videos/<slug:slug>/', VideoDetailAPI.as_view(), name='video-detail'),
    path('playlists/', PlaylistListAPI.as_view(), name='playlist-list'),
    path('playlists/<slug:slug>/', PlaylistDetailAPI.as_view(), name='playlist-detail'),
]
