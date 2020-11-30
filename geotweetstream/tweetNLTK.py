import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from nltk import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

from projectinfo import corpusDir

corpusJson = "out.json"
stopWords = set(stopwords.words("english"))
stopPunct = ["@", ".", "#", "!", ",", "?", "I", ";", ":", "(",")"]

corpus = ""

ps = PorterStemmer()
lem = WordNetLemmatizer()

# Do I need this w/stopPunct?  OR do I still need stopPunct with this?


tokenizer = RegexpTokenizer(r"\w+")


def readJson(corpusJson):
	return json.loads(open(corpusJson, "r").read())

def stringTweets(corpusDict):
	# Load dicts into string for tokenization
	corpus = ""
	for key in corpusDict.keys():
		corpus += corpusDict[key] + " "
	return corpus

def tokenizeTweet(corpus):
	# tokenize a string
	tokenizedCorpus = tokenizer.tokenize(corpus)
	return tokenizedCorpus

def cleanCorpus(corpus):
	filteredCorpus = []
	for word in tokenizedCorpus:
		if word not in stopWords:
			if word not in stopPunct:
				filteredCorpus.append(word)
	return filteredCorpus

def stemTweet(tweet):
	stemmedWord = ps.stem(tweet)
	return stemmedWord

def lemmatizeTweet(tweet):
	lemmatizedWord = lem.lemmatize(tweet,"v")
	return lemmatizedWord

def getFDist(corpus, number):
	# number should be int type
	fdist = FreqDist(corpus)
	mostCommon = fdist.most_common(number)
	return mostCommon

def searchTweets(searchfor, corpusDict):
	results = {}
	for word in searchfor:
		results[word] = []
		for entry in corpusDict:
			if word in corpusDict[entry]:
				results.append(corpusDict[entry])
	return results

def makeDir(dirlist, dirloc):
	for wordBin in dirlist:
		makedirName = dirloc + "/" + wordBin
		os.makedir(makedirName)
	return True

if __name__ == '__main__':

	dirloc = os.getcwd()

	corpusDict = readJson(corpusJson)
	corpus = stringTweets(corpusDict)
	tokenizedCorpus = tokenizeTweet(corpus)
	filteredCorpus = cleanCorpus(tokenizedCorpus)

	stemmedCorpus = []
	lemmatizedCorpus = []
	for tweet in filteredCorpus:
		stemmedCorpus.append(stemTweet(tweet))
		lemmatizedCorpus.append(lemmatizeTweet(tweet))

	corpusFDist = getFDist(filteredCorpus, 100)

#	print(len(corpusFDist))
#	print(corpusFDist[0][0])

	fdistEntries = 3
	topTokens = []
	notTweet = 0

	testFDist = 3

	for i in range(fdistEntries):
		topTokens.append(corpusFDist[i][0])

	topTokens = [corpusFDist[5][0]]

	keeperTweets = {}
	for key in corpusDict.keys():
		tokenizeTemp = tokenizeTweet(corpusDict[key])
		for topWord in topTokens:
			for token in tokenizeTemp:
				#print(token,topWord)
				if topWord in token:
					keeperTweets[key] = corpusDict[key]
				else:
					notTweet += 1
	print(len(keeperTweets), str(notTweet))
	tweetKeys = keeperTweets.keys()
	#print(keeperTweets[tweetKeys[0]])
	for key in keeperTweets.keys():
		print(keeperTweets[key])

	makeDir(topTokens, dirloc)

	"""
		for topWord in range(len(topTokens)):
			print(topWord)
			for i in range(len(tokenizeTemp)):
				if topWord in tokenizeTemp[i]:
					print("true")		
			print(tokenizeTemp)"""
#	corpusVars = [filteredCorpus, stemmedCorpus, lemmatizedCorpus]
#	items = 100
#	for variant in corpusVars:
#		print(getFDist(variant, items))


#	searchfor = "the city"

#	print(searchTweets(searchfor, corpusDict))