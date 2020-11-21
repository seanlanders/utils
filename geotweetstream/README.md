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
2) coordinates.py
	should include geolocative coordinates in a dict variable
		key is a location name
		value should include four latlong coordinates
		location value listed as S, W, N, E
	(this defines the boundary box)
