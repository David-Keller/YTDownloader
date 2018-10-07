import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DEVELOPER_KEY = 'AIzaSyCaFhzv7VDOe1RsKrZq7jQyzIqOmlGafFY'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

import video

class Search:
    def __init__(self, gui):
        self.youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
        self.maxResults = 25
        self.gui = gui;
        videos = []
        for i in range(0, maxResults):
            videos.append(Video())
            
    def search(term):
        self.search_results = self.youtube.search().list(
        q=term,
        type='video',
        part='id,snippet',
        maxResults=self.maxResults
        ).execute()