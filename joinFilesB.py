filenames = [ 
'D:/Code/Python Code/HSA Project/CollectedTweets/dateSpecificTweetsMen/cristianoRonaldo.txt',
'D:/Code/Python Code/HSA Project/CollectedTweets/dateSpecificTweetsMen/kdTrey.txt',
'D:/Code/Python Code/HSA Project/CollectedTweets/dateSpecificTweetsMen/leBronJames.txt',
'D:/Code/Python Code/HSA Project/CollectedTweets/dateSpecificTweetsMen/sachinTendulkar.txt',
'D:/Code/Python Code/HSA Project/CollectedTweets/dateSpecificTweetsMen/wayneRooney.txt']
with open('D:/Code/Python Code/HSA Project/CollectedTweets/dateSpecificTweetsMen/allMensEnglishTweets.txt', "w", encoding = "utf8") as outfile:
    for fname in filenames:
        with open(fname, encoding = "utf8") as infile:
            for line in infile:
                outfile.write(line)