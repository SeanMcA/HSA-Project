from os import listdir
from os.path import isfile, join

mypath = 'D:/Code/Python Code/HSA Project/CollectedTweets/dateSpecificTweetsWomen'
filenames = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#print(filenames)

with open('D:/Code/Python Code/HSA Project/CollectedTweets/dateSpecificTweetsWomen/allWomensTweets.txt', "w", encoding = "utf8") as outfile:
    for fname in filenames:
        with open(mypath +'/'+ fname, encoding = "utf8") as infile:
            for line in infile:
                outfile.write(line)