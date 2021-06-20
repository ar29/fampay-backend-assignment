from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import Video
from .serializers import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows videos to be viewed.
    """
    queryset = Video.objects.all().order_by('-published_at')
    serializer_class = VideoSerializer
