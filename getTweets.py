#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import os

#Variables that contain the user credentials to access Twitter
ACCESS_TOKEN = "177891021-rsIf4Mcnnwkcx092vfSrvJ6ylTG3xvNe0wFkkoLO"
ACCESS_SECRET = "5klR3976OZb24wInOElnGOkmFxb36ZWrrh5vscvLzwcN8"
CONSUMER_KEY = "D1OwPAqtnQF7Vi4Al6fSK2vBA"
CONSUMER_SECRET = "65kltc1dWZrG44IGUASJrELvtWGURBtxxfBY8li0zOAksSIbk6"


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200, encoding='utf8')
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print ("getting tweets before %s" % oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest, encoding='utf8')
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print ("...%s tweets downloaded so far" % len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.created_at, tweet.text] for tweet in alltweets]#remove tweet.created-at to get just text.
	
	#write the csv
	dirPath = os.path.dirname(os.path.realpath(__file__)) 	
	with open(dirPath  + '\\CollectedTweets\\%s_tweets.csv' % screen_name, 'w', encoding='utf8') as f:
		writer = csv.writer(f)
		writer.writerow(["text"])#can remove this line of code
		writer.writerows(outtweets)
	
	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("danicapatrick")
