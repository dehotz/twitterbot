
import tweepy
import time
import os
import random
from secret import *

#logging into twitter api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

message = "hmmm... @"

#for tweet in tweepy.Cursor(api.search, q='25073877', lang = 'en').items(1):
#25073877
for tweet in tweepy.Cursor(api.user_timeline, id='1231528764').items(1):
	try:
		os.chdir('donny')
		screen_name = tweet.user.screen_name
		stat_at = message + screen_name
		tweet_id = tweet.id
		random_num = random.randrange(1,13)
		random_num_checker = 0
		for image in os.listdir('.'):
			random_num_checker += 1
			if random_num_checker == random_num:
				api.update_with_media(image, status=stat_at, in_reply_to_status_id=tweet_id)
				time.sleep(10)
		
	except tweepy.TweepError as e:
		print(e.reason)
		time.sleep(3)
		continue
	except tweepy.RateLimitError:
		time.sleep(15*60)
	except StopIteration:
		break