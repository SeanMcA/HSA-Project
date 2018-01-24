import re
import os

dirPath = os.path.dirname(os.path.realpath(__file__)) 
filePath = dirPath + "\\CleanedTweets\\cristianoronaldoCleaned.txt"


def find_hashtags(line):
	if( [ t for t in line.split() if t.startswith('#') ] != []):
		print([ t for t in line.split() if t.startswith('#') ])

for line in open(filePath, encoding = "utf8"):
		line = find_hashtags(line)



