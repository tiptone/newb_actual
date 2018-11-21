#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import tweepy 
# Import our Twitter credentials from credentials.py
from credentials import *

import sched, time

import logging

logging.basicConfig(filename="/tmp/mzbat_last.log", 
                    level=logging.INFO,
                    format='%(asctime)s %(message)s') # include timestamp

global api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#s = sched.scheduler(time.time, time.sleep)
last = api.get_user('253608265').followers_count
counter = last 
users = tweepy.Cursor(api.followers, screen_name="mzbat").items()
while True:
    try:
      user = next(users)
    except tweepy.TweepError:
      time.sleep(60*3)
      user = next(users)
    except StopIteration:
      break
    print "Counter: " + str(counter) + " @" + user.screen_name
    logging.info("Counter: {} User: @{}".format(counter,user.screen_name))
    counter = counter -1
    if (counter == 19990):
      raise SystemExit
