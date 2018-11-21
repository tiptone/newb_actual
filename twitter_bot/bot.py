
# -*- coding: utf-8 -*-
#

# Import our Twitter credentials from credentials.py
from credentials import *

# this is our bot class and methods
from twitter_bot import TwitterBot

import tweepy 
import sched, time
import random
import logging

# Doing some logging to a file
logging.basicConfig(filename="/tmp/followers.log", level=logging.INFO,
                format='%(asctime)s %(message)s') # include timestamp
logger = logging.getLogger(__name__)

global api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

twitter_handle='@thedevilsvoice'

if __name__ == "__main__":
  twi = TwitterBot()



