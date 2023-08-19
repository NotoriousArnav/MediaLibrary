from django.views.generic import ListView, DetailView
from .models import Playlist
from .models import Video

class PlaylistListView(ListView):
    model = Playlist
    template_name = 'playlist/playlist_list.html'
    context_object_name = 'playlists'
    queryset = Playlist.objects.all()  # Customize the queryset as needed

class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = 'playlist/playlist_detail.html'
    context_object_name = 'playlist'

class VideoListView(ListView):
    model = Video
    template_name = 'video/video_list.html'
    context_object_name = 'videos'
    queryset = Video.objects.all()  # Customize the queryset as needed

class VideoDetailView(DetailView):
    model = Video
    template_name = 'video/video_detail.html'
    context_object_name = 'video'

    def get_objects(self, queryset=None):
        slug = self.kwargs.get('slug')
        uuid = self.kwargs.get('uuid')

        if slugs:
            return get_object_or_404(Video, slug=slug)
        elif uuid:
            return get_object_or_404(Video, uuid=uuid)
        else:
            pass
