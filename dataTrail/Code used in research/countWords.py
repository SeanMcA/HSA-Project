import re
import os

def remove_non_prinatble(word):
	printable = set(string.printable) # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
	no_punct = ""
	for char in word:
	   if char in printable:
		   no_punct = no_punct + char
	return no_punct


def getCounts(file):
	global teamCount
	global playerCount
	global gameCount
	global womenCount
	global girlCount
	global femaleCount
	global menCount
	global maleCount
	global boyCount
	global familyCount
	global loveCount
	global happyCount
	global bestCount
	global yearCount
	global goodCount
	global firstCount
	global todayCount
	global winCount
	global congratCount
	
	
	with open(file, encoding = "utf8") as f:
		contents = f.read().lower()
		teamCount = contents.count('team')		
		playerCount = contents.count('player')
		gameCount = contents.count('game')
		womenCount = contents.count('women') + contents.count('woman') 
		femaleCount = contents.count('female')
		girlCount = contents.count('girl')		
		menCount = contents.count(' men') + contents.count(' man ')
		maleCount = contents.count(' male')
		boyCount = contents.count(' boy')
		familyCount = contents.count('family')
		loveCount = contents.count('love')
		happyCount = contents.count('happy')
		bestCount = contents.count('best')
		yearCount = contents.count('year')
		goodCount = contents.count('good')
		firstCount = contents.count('first')
		todayCount = contents.count('today')
		winCount = contents.count(' win')
		congratCount = contents.count('congrat')
		
		
		

def replacement(name):
	dirPath = os.path.dirname(os.path.realpath(__file__))
	filePath = dirPath + "\\CleanedTweets\\" + name + ".txt"
	changedFile = dirPath + "\\CleanedTweets\\" + name + "_Words.txt"
	
	getCounts(filePath)
	
	o = open(changedFile, "w", encoding = "utf8")#file containing the changed text  .
			# a opens the file in 'append' mode so you don't delete all the information.
			# w opens the file in write mode which clears the contents of the file each time.
	o.write('team: ' + str(teamCount) + '\n')
	o.write('player: ' + str(playerCount) + '\n')
	o.write('game: ' + str(gameCount) + '\n\n')
	o.write('women: ' + str(womenCount) + '\n')
	o.write('female: ' + str(femaleCount) + '\n')
	o.write('girl: ' + str(girlCount) + '\n')
	o.write('men: ' + str(menCount) + '\n')
	o.write('male: ' + str(maleCount) + '\n')
	o.write('boy: ' + str(boyCount) + '\n\n')
	o.write('family: ' + str(familyCount) + '\n')
	o.write('love: ' + str(loveCount) + '\n')
	o.write('happy: ' + str(happyCount) + '\n')
	o.write('best: ' + str(bestCount) + '\n')
	o.write('year: ' + str(yearCount) + '\n')
	o.write('good: ' + str(goodCount) + '\n')
	o.write('first: ' + str(firstCount) + '\n')
	o.write('today: ' + str(todayCount) + '\n')
	o.write('win: ' + str(winCount) + '\n')
	o.write('congrat: ' + str(congratCount) + '\n')
	
	
	
if __name__ == '__main__':
	fileToBeCleaned = 'danicapatrickCleaned'
	replacement(fileToBeCleaned)
	
	
	
	