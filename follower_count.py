#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import tweepy 
# Import our Twitter credentials from credentials.py
from credentials import *

import sched, time

global api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

s = sched.scheduler(time.time, time.sleep)

def do_something(sc): 
  user = api.get_user('253608265')
  print user.screen_name
  print user.followers_count
  s.enter(30, 1, do_something, (sc,))
  api.update_status('test tweet') 

s.enter(30, 1, do_something, (s,))
s.run()
