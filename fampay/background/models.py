from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField()
    description = models.CharField()
    publishing_datetime = models.DateTimeField()
    thumbnail_url = models.CharField()
