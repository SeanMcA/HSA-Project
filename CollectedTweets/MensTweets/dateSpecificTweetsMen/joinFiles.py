filenames = [ 
'D:/Code/Python Code/CleaningTweets/dateSpecificTweetsMen/cristianoRonaldo.txt',
'D:/Code/Python Code/CleaningTweets/dateSpecificTweetsMen/kdTrey.txt',
'D:/Code/Python Code/CleaningTweets/dateSpecificTweetsMen/leBronJames.txt',
'D:/Code/Python Code/CleaningTweets/dateSpecificTweetsMen/sachinTendulkar.txt',
'D:/Code/Python Code/CleaningTweets/dateSpecificTweetsMen/wayneRooney.txt']
with open('D:/Code/Python Code/CleaningTweets/dateSpecificTweetsMen/allMensEnglishTweets.txt', "w", encoding = "utf8") as outfile:
    for fname in filenames:
        with open(fname, encoding = "utf8") as infile:
            for line in infile:
                outfile.write(line)