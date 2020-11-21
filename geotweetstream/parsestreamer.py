import json
import os, glob
import preprocessor as p
#from wrapperstreamer import getDates
from projectinfo import coordsName, projectName

p.set_options(p.OPT.URL, p.OPT.EMOJI)

tweetLogs = "./logs/labsynthe-timessquare-2020-11.txt"
tweetCorpus = "./corpus/labsynthe-timessquare-2011-11.txt"

cwDir = os.getcwd()
corpusDir = cwDir + "/corpus"
print(cwDir)
try:
	os.mkdir(corpusDir)
	print("Made ",corpusDir)
except:
	print("already made ",corpusDir)


"""for x in range(len(tweets)):
	try:
		json_load = json.loads(tweets[x])
		texts = json_load['text']
		#coded = texts.decode('utf-8')
		#cleaned = p.clean(coded)
		cleaned = p.clean(texts)
		s = cleaned.encode('utf-8')
		print(s)
	except:
		pass"""


def showTweets(tweets):
	for tweet in tweets:
		try:
			json_load = json.loads(tweet)
			for key in json_load.keys():
				texts = json_load[key]
				#coded = texts.decode('utf-8')
				#cleaned = p.clean(coded)
				print(key, ": ",texts)
		except:
			pass

def showText(tweet):
	json_load = json.loads(tweet)
	text = json_load['text']
	return text

if __name__ == "__main__":
	with open(tweetLogs, "r") as f:
		tweets=f.readlines()

	print(len(tweets))
	print(tweets[0])
	corpus = ""
	corpusError = 0
	for tweet in tweets:
		try:
			corpus += showText(tweet)
		except:
			corpusError +=1
	with open(tweetCorpus, "w") as f:
		f.write(corpus)
		#for i in range(len(corpus)):
		#	lineWrite = corpus[i] + "\r\r"
		#	f.write(lineWrite)
		f.close()
	print("Written to",tweetCorpus,"., # Tweets:",len(tweets),",Errors:",corpusError)