from django.urls import path
from .views import *

urlpatterns = [
    path('videos/', VideoListView.as_view(), name='video-list'),
    path('videos/<slug:slug>/', VideoDetailView.as_view(), name='video-detail'),
    path('playlists/', PlaylistListView.as_view(), name='playlist-list'),
    path('playlists/<slug:slug>/', PlaylistDetailView.as_view(), name='playlist-detail'),    
]
