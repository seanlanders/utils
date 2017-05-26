import os

# os.walk down a directory structure; creates a txt that is a searchable index

def dirwri(writeto, dir):
	f = open(writeto, "a")
	for root, dirs, files in os.walk(dir):
		for name in files:
			f.write(os.path.join(root,name) + "\n")
	f.close()

# uses a txt as a searchable index; creates a list of all applicable filetypes

def finty(readfrom, ext):
	logged = []
	f = open(readfrom, "r")
	files = f.readlines()
	for line in files:
		buffertext = line.strip('\n')
		buffertext = buffertext.split('.')
		if buffertext[(len(buffertext)-1)] == ext:
			print line
			logged.append(line.strip('\n'))
	f.close()
	return logged