#!/usr/bin/python

# This sample executes a search request for the specified search term.
# Sample usage:
#   python search.py --q=surfing --max-results=10
# NOTE: To use the sample, you must provide a developer key obtained
#       in the Google APIs Console. Search for "REPLACE_ME" in this code
#       to find the correct place to provide that key..

import argparse
import os

from celery import shared_task
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from .models import Video


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEYS = os.environ.get("GOOGLE_DEVELOPER_KEYS").split("::")
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


@shared_task
def query_youtube_data_api():
    for developer_key in DEVELOPER_KEYS:
        try:
            youtube_search(developer_key)
        except HttpError as e:
            print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
            if e.resp.status == 403:
                continue
        else:
            break


def youtube_search(developer_key):
    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=developer_key)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q='Cricket',
        part='id,snippet',
        maxResults=1000
    ).execute()

    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            video_id = search_result['id']['videoId']
            published_at = search_result['snippet']['publishedAt']
            title = search_result['snippet']['title']
            description = search_result['snippet']['description']
            thumbnail_url = search_result['snippet']['thumbnails']['default']['url']

            video, created = Video.objects.get_or_create(
                id=video_id,
                published_at=published_at,
                title=title,
                description=description,
                thumbnail_url=thumbnail_url)
