# -*- coding: utf-8 -*-
#
import tweepy 

# Import our Twitter credentials from credentials.py
from credentials import *

import sched, time
import random

global api

class TwitterBot(object):
  """docstring for TwitterBot"""
  def __init__(self):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    twitter_handle='@thedevilsvoice'

  def unfollow_back_who_not_folow_me(self):
    # function to unfollow users that don't follow you back.
    print('Starting to unfollow users...')
    # makes a new list of users who don't follow you back.
    non_mutuals = set(self.following) - set(self.followers)
    total_followed = 0
    for f in non_mutuals:
      try:
        # unfollows non follower.
        self.api.destroy_friendship(f)
        total_followed += 1
        if total_followed % 10 == 0:
          print(str(total_followed) + ' unfollowed so far.')
        if total_followed==self.MAX_UNFOLLOW:
          print('unfollow 100 users now, exiting it')
          exit()

        print('Unfollowed user. Sleeping 15 seconds.')
        sleep(15)
      except (tweepy.RateLimitError, tweepy.TweepError) as e:
         self.error_handling(e)
    print(total_followed)

    def follower_count(self): 
      global last_count
      # lost a follower
      if (last_count > api.get_user('253608265').followers_count):
        last_count = api.get_user('253608265').followers_count
        print "Setting last_count to %i" , last_count
        logging.info("Lost follower(s). Setting to {}".format(last_count))
      bat = api.get_user('253608265')
      print "Watching User: " , bat.screen_name
      logging.info("Watching User: {} ".format(bat.screen_name))
      #print bat.followers_count
      print "Last count: " , last_count
      logging.info("Last count: {}".format(last_count)) 
      s.enter(60, 1, do_something, (sc,))
      for user in tweepy.Cursor(api.followers, screen_name="mzbat").items():
        if (bat.followers_count % 5 == 0 ) and (last_count != bat.followers_count):
          print "Most recent: " , user.screen_name
          logging.info("Most recent: {}".format(user.screen_name))
          print "Follower Count: " , bat.followers_count
          logging.info("Follower Count: {}".format(bat.followers_count))
          print "Modulo 5"
          logging.info("Modulo 5")
          api.update_status('@mzbat Just followed by %s and the follower count is %s' % (user.screen_name,bat.followers_count))
          last_count = bat.followers_count
        elif (bat.followers_count == 200000) :
          print "Most recent: " , user.screen_name
          logging.info("Most recent: {}".format(user.screen_name))
          print "Follower Count: " , bat.followers_count
          logging.info("Follower Count: {}".format(bat.followers_count))
          print "20K"
          logging.info("20K")
          api.update_status("@mzbat the 20K follower is %s" % user.screen_name)
          last_count = bat.followers_count
        elif (bat.followers_count > last_count):
          print "Most recent: " , user.screen_name
          logging.info("Most recent: {}".format(user.screen_name))
          print "Follower Count: " , bat.followers_count
          logging.info("Follower Count: {}".format(bat.followers_count))
          print "Gained a follower: " , user.screen_name
          logging.info("Gained a follower {}".format(user.screen_name))
          #last_count = bat.followers_count
        else: 
          print "Most recent: " , user.screen_name
          logging.info("Most recent: {}".format(user.screen_name))
          print "Follower Count: " , bat.followers_count
          logging.info("Follower Count: {}".format(bat.followers_count))
          print "ho hum, nothing happened"
          logging.info("ho hum, nothing happened")
        break


def list_followers(self):
  list = open('/tmp/twitter_followers.txt','w')  
  if(api.verify_credentials):
    print  ('We are logged in')
    logger.info ('We are logged in')
  user = tweepy.Cursor(api.followers, screen_name=twitter_handle).items()
  while True:
    try:
      u = next(user)
      list.write(u.screen_name +' \n')
      print ("adding: ", u.screen_name)
      #fllw = tweepy.Cursor(api.exists_friendship(twitter_handle,u.screen_name))
      #print ("fllws: ",fllw)
    except (tweepy.RateLimitError, tweepy.TweepError) as e:
      self.error_handling(e)
      u = next(user)
      list.write(u.screen_name +' \n')
  list.close()  



  @staticmethod
  def error_handling(e):
    error = type(e)
      if error == tweepy.RateLimitError:
        print("You've hit a limit! Sleeping for 30 minutes.")
        sleep(60 * 30)
      elif error == tweepy.TweepError:
        print('Uh oh. Could not complete task. Sleeping 10 seconds.')
        sleep(20)
      else:
        print('Uh oh. Could not get exception type. Sleeping 10 minutes')
          sleep(60*10)

