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
    queryset = Video.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'description']
    search_fields = ['$title', '$description']
    ordering_fields = ['published_at', 'title']
    ordering = ['-published_at']
    serializer_class = VideoSerializer

    def get_queryset(self):
        queryset = Video.objects.all()
        title = self.request.query_params.get('title')
        description = self.request.query_params.get('description')

        if title is not None and title != "":
            queryset = queryset.filter(title__contains=title)

        if description is not None and description != "":
            queryset = queryset.filter(description__contains=description)
        return queryset
