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
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

s = sched.scheduler(time.time, time.sleep)
last_count = api.get_user('253608265').followers_count

def do_something(sc): 
  global last_count
  if (last_count > api.get_user('253608265').followers_count):
    last_count = api.get_user('253608265').followers_count
    print "Decrementing last_count"
  bat = api.get_user('253608265')
  print "Watching User: " , bat.screen_name
  #print bat.followers_count
  print "Last count: " , last_count
  s.enter(60, 1, do_something, (sc,))
  #api.update_status('test tweet') 
  for user in tweepy.Cursor(api.followers, screen_name="mzbat").items():
    if (bat.followers_count % 5 == 0 ) and (last_count != bat.followers_count):
      print "Modulo 5"
      print "Most recent: " , user.screen_name
      print "Follower Count: " , bat.followers_count
      api.update_status('@mzbat Just followed by %s and the follower count is %s' % (user.screen_name,bat.followers_count))
      last_count = bat.followers_count
    elif (bat.followers_count == 200000) :
      print "20K"
      print "Most recent: " , user.screen_name
      print "Follower Count: " , bat.followers_count
      api.update_status("@mzbat the 20K follower is %s" % user.screen_name)
      last_count = bat.followers_count
    elif (bat.followers_count > last_count):
      print "Gained a follower: " , user.screen_name
      print "Follower Count: " , bat.followers_count
    else: 
      print "ho hum, nothing happened"
      print "Most recent: " , user.screen_name
      print "Follower Count: " , bat.followers_count
    break
  
s.enter(5, 1, do_something, (s,))
s.run()
