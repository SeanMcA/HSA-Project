import os
import sys
import fileinput
import re
import string
import unicodedata
from unicodedata import category


		
def strip_date_time(line):	
	if(line[:1] == '2'):
		lineCut = line[20:]
		return lineCut
	else:
		return line
		
# define punctuation to be removed - not removing @ ' or # 	could we add in 🔜?
punctuations = '''!()-[]{};:"\,<>./?$%^&*_~🔜'''

def removePunctuation(line):
	no_punct = ""
	for char in line:
	   if char not in punctuations:
		   no_punct = no_punct + char
	return no_punct
	
	

	
def remove_https_from(word):
	if(word[:5] =='https'):
		return ''
	else:
		return word
		
def remove_empty_lines(line):
	if(word[:5] =='\\n\\r'):
		return ''
		
def remove_control_characters(word):
    return "".join(ch for ch in word if unicodedata.category(ch)[0]!="C")
	
def remove_non_prinatble(word):
	printable = set(string.printable)
	no_punct = ""
	for char in word:
	   if char in printable:
		   no_punct = no_punct + char
	return no_punct
		
		
def getCounts(file):
	global hashtagCount
	global httpsCount
	global retweetCount
	global tweets
	tweets = 0
	with open(file, encoding = "utf8") as f:
		contents = f.read()
		hashtagCount = contents.count("#")	
		httpsCount = contents.count('https')
		retweetCount = contents.count('RT')
	for line in open(file, encoding = "utf8"):
		if(line[:1] == '2'):
			tweets += 1
		

	
def replacement(name):
	dirPath = os.path.dirname(os.path.realpath(__file__))
	filePath = dirPath + "\\CollectedTweets\\" + name + ".txt"
	changedFile = dirPath + "\\CleanedTweets\\" + name + "Cleaned.txt"
	
	getCounts(filePath)
	
	o = open(changedFile, "w", encoding = "utf8")#file containing the changed text  .
			# a opens the file in 'append' mode so you don't delete all the information.
			# w opens th e file in write mode which clears the contents of the file each time.
	o.write('Hashtags: ' + str(hashtagCount) + '\n')
	o.write('https: ' + str(httpsCount) + '\n')
	o.write('Tweets: ' + str(tweets) + '\n')
	o.write('Retweets: ' + str(retweetCount) + '\n\n')
	
	for line in open(filePath, encoding = "utf8"):#this is the original file.
		line = strip_date_time(line)
		line = removePunctuation(line)
		split_line = line.split() #split the line into individual words.
		new_split_line1 = [remove_https_from(word) for word in split_line]
		new_split_line2 = [remove_control_characters(word) for word in new_split_line1]
		new_split_line3 = [remove_non_prinatble(word) for word in new_split_line2]
		new_line = ' '.join(new_split_line3)
		o.write(new_line + '\n')
	o.close()


if __name__ == '__main__':
	fileToBeCleaned = 'waynerooney'
	replacement(fileToBeCleaned)