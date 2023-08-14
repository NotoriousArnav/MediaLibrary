import uuid
import random
import string
from django.db import models
from django.utils.text import slugify

class Video(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    video_file = models.FileField(upload_to='videos/')
    upload_date = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField()
    slug = models.SlugField(unique=True, editable=False)  # Automatically populated

    def __str__(self):
        return f"{self.title}  {self.slug}"

    def save(self, *args, **kwargs):
        # Generate a unique slug based on the video's title
        base_slug = slugify(self.title)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        self.slug = f"{base_slug}-{random_string}"
        super().save(*args, **kwargs)

class Playlist(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    videos = models.ManyToManyField('Video')
    slug = models.SlugField(unique=True, editable=False)  # Automatically populated

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Generate a unique slug based on the playlist's title
        base_slug = slugify(self.title)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        self.slug = f"{base_slug}-{random_string}"
        super().save(*args, **kwargs)
