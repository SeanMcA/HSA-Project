import re
import os

dirPath = os.path.dirname(os.path.realpath(__file__)) 
filePath = dirPath + "\\CleanedTweets\\allWomensTweetsCleanedNoHT.txt"
outputFilePath = dirPath + "\\CleanedTweets\\WOmensCleanedTweetsHashtagsAndRefsNoSM.txt"

global my_dict
my_hashtags = {}

global my_atRefs
my_atRefs = {}

global my_wordCount
my_wordCount = {}

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

def count_all_words(word):
	if(word in my_wordCount):
		my_wordCount[word] = my_wordCount[word] + 1
	else:
		my_wordCount[word]=1
			
			
for line in open(filePath, encoding = "utf8"):
		split_line = line.split()
		[find_hashtags(word) for word in split_line]
		[find_atReferences(word) for word in split_line]
		[count_all_words(word) for word in split_line]

#Print the hashtags and refs		
print('\nHashTags counts:\n')
o = open(outputFilePath, "w", encoding = "utf8")		
#for key in my_hashtags:
for key, value in sorted(my_hashtags.items(), key=lambda kv: (-kv[1], kv[0])):
	o.write(key + ' - ' + str(value) + '\n')
     #print(key, my_hashtags[key])

print('\n@ references counts:\n')
#for key in my_atRefs:
for key, value in sorted(my_atRefs.items(), key=lambda kv: (-kv[1], kv[0])):
	o.write(key + ' - ' + str(value) + '\n')
     #print(key, my_atRefs[key])	

print('\nWord counts:\n')
#for key in my_wordCount:
for key, value in sorted(my_wordCount.items(), key=lambda kv: (-kv[1], kv[0])):
	o.write(key + ' - ' + str(value) + '\n')
     #print(key, my_wordCount[key])	 



