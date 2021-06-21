from django.db import models

# Create your models here.


class Video(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255, db_index=True)
    description = models.CharField(max_length=1024, db_index=True)
    published_at = models.DateTimeField(db_index=True)
    thumbnail_url = models.CharField(max_length=255)
