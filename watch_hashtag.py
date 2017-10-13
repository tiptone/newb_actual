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

class TweetListener(StreamListener):
  def on_status(self, status):
    print "tweet " + str(status.created_at) +"\n"
    print status.text + "\n"
    # You can dump your tweets into Json File, or load it to your database

stream = Stream(auth, TweetListener(), secure=True, )
t = u"#badgelife" # You can use different hashtags 
stream.filter(track=[t])
