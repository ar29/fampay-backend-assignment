from django.db import models

# Create your models here.


class Video(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_at = models.DateTimeField()
    thumbnail_url = models.CharField(max_length=255)
