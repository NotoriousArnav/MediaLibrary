from rest_framework import generics
from django.shortcuts import get_object_or_404
from library.models import Video, Playlist
from .serializers import VideoSerializer, PlaylistSerializer

class VideoListAPI(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Video, slug=slug)

class PlaylistListAPI(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Playlist, slug=slug)

