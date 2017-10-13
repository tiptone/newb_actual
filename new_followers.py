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
  bat = api.get_user('253608265')
  print "Watching User: " , bat.screen_name
  #print bat.followers_count
  s.enter(30, 1, do_something, (sc,))
  #api.update_status('test tweet') 
  for user in tweepy.Cursor(api.followers, screen_name="mzbat").items():
    print "Most recent: " , user.screen_name 
    print "Follower Count: " , bat.followers_count
    if (bat.followers_count == 200000) :
      api.update_status("@mzbat the 20K follower is " , user.screen_name )
    break
  
s.enter(30, 1, do_something, (s,))
s.run()
