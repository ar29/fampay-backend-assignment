from rest_framework import serializers

from .models import Video


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = [
            'id',
            'title',
            'description',
            'published_at',
            'thumbnail_url']
