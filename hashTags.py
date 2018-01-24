import re
import os

dirPath = os.path.dirname(os.path.realpath(__file__)) 
filePath = dirPath + "\\CleanedTweets\\cristianoronaldoCleaned.txt"

global my_dict
my_hashtags = {}

global my_atRefs
my_atRefs = {}

def find_hashtags(word):
	if( word[:1] == '#' ):
		#print(word)
		if(word in my_hashtags):
			my_hashtags[word] = my_hashtags[word] + 1
		else:
			my_hashtags[word]=1
			
def find_atReferences(word):
	if( word[:1] == '@' ):
		#print(word)
		if(word in my_atRefs):
			my_atRefs[word] = my_atRefs[word] + 1
		else:
			my_atRefs[word]=1			

for line in open(filePath, encoding = "utf8"):
		split_line = line.split()
		[find_hashtags(word) for word in split_line]
		[find_atReferences(word) for word in split_line]
		
print('\nHashTags counts:\n')
		
for key in my_hashtags:
     print(key, my_hashtags[key])

print('\n@ references counts:\n')
for key in my_atRefs:
     print(key, my_atRefs[key])	 



