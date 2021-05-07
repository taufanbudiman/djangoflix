from django.db import models


# Create your models here
class Video(models.Model):
    """this is a model for videos."""

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=255)

    class Meta:
        """Meta definition for video."""

        verbose_name = 'video'
        verbose_name_plural = 'videos'

    def __str__(self):
        """Unicode representation of video."""
        return self.title
