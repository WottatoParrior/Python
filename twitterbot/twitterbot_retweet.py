import tweepy
from time import sleep
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search,  
						   q='#ocean',).items(10):
	try:
		print('Tweet by : @' + tweet.user.screen_name)
		tweet.retweet()
		print('retweeted the tweet')
		sleep(10)
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break
