import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class VideoData:
	def __init__(self, gui, youtube):
		self.link = "sample.com"
		self.title = "sample title"
		self.description = "sample"
		self.image = "kitten.jpg"
		self.youtube = youtube
		self.guiUpdate = None
		
	def setgui(guiUpdate):
		
	def setLink(self, link):
		self.link = link
		gui()
	def setTitle(self, title):
		self.title = title
		gui.update()
	def setDescription(self, description):
		self.description = description
		gui.update()
	def setImage(self, image):
		self.image = image
		gui.update()
		
	def update():
		
		