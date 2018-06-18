#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
# Import our Twitter credentials from credentials.py
from credentials import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#s = sched.scheduler(time.time, time.sleep)

class TweetListener(StreamListener):
  def on_status(self, status):
    print ("tweet " + str(status.created_at) +"\n")
    print (status.text + "\n")
    # You can dump your tweets into Json File, or load it to your database
    sn = status.user.screen_name
    m = "@%s https://motherboard.vice.com/en_us/article/43nk9b/cryptocurrency-are-not-crypto-bitcoin" % (sn)
    api.update_status(m, status.id)

stream = Stream(auth, TweetListener(), secure=True, )
#t = u"#crypto" # You can use different hashtags
#stream.filter(track=[t])
stream.filter(track=['#crypto', '#blockchain'])

