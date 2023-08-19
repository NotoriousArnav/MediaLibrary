from django.urls import path
from .views import *

urlpatterns = [
    path('videos/', VideoListAPI.as_view(), name='video-list-api'),
    path('videos/<slug:slug>/', VideoDetailAPI.as_view(), name='video-detail-api'),
    path('playlists/', PlaylistListAPI.as_view(), name='playlist-list-api'),
    path('playlists/<slug:slug>/', PlaylistDetailAPI.as_view(), name='playlist-detail-api'),
]
