Geolocative tweet streamer

Needs two files:
1) credentials.py
	should include Twitter credentials in a dict variable
	named 'credentials'
	keys are:
		consumer_key
		consumer_secret
		access_token
		access_token_secret
	to get credentials, create an app:
		https://developer.twitter.com/en/docs/apps/overview

2) coordinates.py
	should include geolocative coordinates in a dict variable
		key is a location name
		value should include four latlong coordinates
		location value listed as S, W, N, E
	(this defines the boundary box)
	
	
projectinfo.py is provided for ease of customization -- projectname, whatc coordinates should be scraped, where bins should live, etc.
coordinates.py contains a few possible boundary boxes to scrape

wrapperstreamer.py scrapes tweets from a given set of coordinates (specified by projectinfo.py, referring to coordinates.py)
It creates logfiles formatted as follows:

"<projectname>-<coordinates>-<year>-<month>-<date>-.txt"

parsestreamer.py 
	takes the raw logs created by wrapperstreamer.py and turns them into a JSON object for ease of handling
	
tweetNLTK.py
	uses Natural Language Tool Kit to begin to analyze the tweet logs -- find the words most used in the tweets
		create bins (directories) based on most used words
		create logs of tweets that use those words and drop them into the bins
