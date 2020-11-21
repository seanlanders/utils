import json

from nltk.tokenize import sent_tokenize

from projectinfo import corpusDir

json = "out.json"


rs = json.load(open(json, "r"))


print(len(rs))