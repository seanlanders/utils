import sys, os
from datetime import datetime
from credentials import credentials 
from coordinates import coordinates as coords
from projectinfo import coordsName, projectName
import tweetstreamer as t

# parse coordinates + project name for filename

def getDates():
	currentMonth = str(datetime.now().month)
	currentYear = str(datetime.now().year)
	currentDay = str(datetime.now().day)
	return currentMonth, currentYear, currentDay

cwDir = os.getcwd()
workingDir = cwDir + "/logs" 
print(cwDir)
try:
	os.mkdir(workingDir)
	print("Made ",workingDir)
except:
	print("already made ",workingDir)

currentMonth, currentYear, currentDay = getDates()

filename = workingDir + "/%s-%s-%s-%s-%s.txt" % (projectName, coordsName, currentYear, currentMonth, currentDay)

print(getDates())
print(filename)

sys.stdout = open(filename, "a")

#streamdata = t.streamdata(t.credentials, t.nyc)
t.streamdata(credentials, coords[coordsName])