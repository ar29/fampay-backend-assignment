from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
import django_filters.rest_framework
from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Video
from .serializers import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows videos to be viewed.
    """
    queryset = Video.objects.all().order_by('-published_at')
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'description']
    ordering_fields = ['published_at', 'title']
    ordering = ['-published_at']
    serializer_class = VideoSerializer
