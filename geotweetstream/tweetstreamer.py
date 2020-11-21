# Program that prints tweet's text -- and only text -- from a geo-tagged location - printing them out in real time.
# Junius Heights: -96.7645407,32.7994839,-96.7495215,32.8123166
# Edith A. O'Donnell: -96.7489412803,32.9848248197,-96.7462433197,32.9875227803 
import json
import sys
import time
import datetime
import preprocessor as p
#from preprocessor.api import clean, tokenize, parse

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

# Reminder - location is South, West, North, East. 

class StdOutListener(StreamListener):

	def on_data(self, data):
		print(data)
		"""
		json_load = json.loads(data)
		texts = json_load['text']
		#coded = texts.decode('utf-8')
		#cleaned = p.clean(coded)
		cleaned = p.clean(texts)
		s = cleaned.encode('utf-8')
		print(s)
		"""
		sys.stdout.flush()
		return True

	def on_error(self, status):
		print(status)


def authorize(credentials):
	auth = OAuthHandler(credentials["consumer_key"], credentials["consumer_secret"])
	auth.set_access_token(credentials["access_token"], credentials["access_token_secret"])
	return auth

def streamdata(credentials, location):
	l = StdOutListener()
	auth = authorize(credentials)
	stream = Stream(auth, l)
	stream.filter(locations=location)
