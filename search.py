import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DEVELOPER_KEY = 'AIzaSyCaFhzv7VDOe1RsKrZq7jQyzIqOmlGafFY'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

from video import *

class Search:
    def __init__(self, guiUpdate):
        self.youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
        self.maxResults = 25
        self.guiUpdate = guiUpdate;
        self.videos = []
        for i in range(0, self.maxResults):
            self.videos.append(VideoData(guiUpdate, self.youtube))
            
    def search(term):
        self.search_results = self.youtube.search().list(
        q=term,
        type='video',
        part='id,snippet',
        maxResults=self.maxResults
        ).execute()
        for index in range(0, self.maxResults):
            self.videos[index].setLink(