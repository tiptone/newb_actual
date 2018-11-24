import datetime
from weather import Weather, Unit
import tweepy
# Import our credentials from credentials.py
import sys
sys.path.append('../')
from credentials import *

# set up twitter interface
global api
auth = tweepy.OAuthHandler(fub_consumer_key, fub_consumer_secret)
auth.set_access_token(fub_access_key, fub_access_secret)
api = tweepy.API(auth)
global user_id

class Command(object):
  def __init__(self):
    self.commands = { 
      "help" : self.help,
      "cookbook" : self.cookbook,
      "follow" : self.follow,
      "github" : self.github,
      "music" : self.music,
      "tweet" : self.tweet,
      "unfollow" : self.unfollow, 
      "weather" : self.weather,
      "when" : self.when
    }
 
  def handle_command(self, user, command):
    response = "<@" + user + ">: "
     
    if (command.split(None, 1)[0] ==  'tweet'):
      self.commands['tweet'](command.split(None, 1)[1])
      response += "Sending tweet: " + command.split(None, 1)[1]
    elif (command.split(None, 1)[0] ==  'follow'):
      user_id = command.split(None, 1)[1]
      print user_id
      result = self.commands['follow'](user_id)
      response += result 
    elif (command.split(None, 1)[0] ==  'unfollow'):
      user_id = command.split(None, 1)[1]
      result = self.commands['unfollow'](user_id)
      response += result 
    elif command in self.commands:
      response += self.commands[command]()
    else:
      response += "Sorry I don't understand the command: " + command + ". " + self.help()
         
    return response
         
  def cookbook(self):
    return "https://github.com/DEAD10C5/1337-Noms-The-Hacker-Cookbook"
  def github(self):
    return "https://github.com/theDevilsVoice/newb_actual/tree/master/slack_bot"
  def music(self):
    return "https://www.reverbnation.com/angusmohr/song/14449187-andy-renwicks-favourite-ferret"
  def tweet(self, my_tweet):
    try: 
      api.update_status(my_tweet)
    except tweepy.TweepError as e:
      print e
      #continue
      return ('Something went wrong, tweet not sent.')
    return ('Tweet sent.')
  def weather(self):
    weather = Weather(unit=Unit.FAHRENHEIT)
    lookup = weather.lookup(2400352)
    condition = lookup.condition
    #for forecast in forecasts:
    #  print(forecast.text)
    #  print(forecast.date)
    #  print(forecast.high)
    #  print(forecast.low)
    response = "Currently: " + str(condition.temp) + " and " + str(condition.text) + " in beautiful Estes Park, CO"
    return response
  def when(self):
    delta = datetime.datetime(2019, 4, 26) - datetime.datetime.now()
    response = "Countdown to RussCon 2019: " + str(delta) + "\r\n"
    return response
     
  def help(self):
    response = "Currently I support the following commands:\r\n"
         
    for command in self.commands:
      response += command + "\r\n"
             
    return response

  def follow(self, user_id):
    try:
      api.create_friendship(user_id)
    except tweepy.TweepError as e:
      print e
      return "Failure"
    return "Success"
  def unfollow(self,user_id):
    try:
      api.destroy_friendship(user_id)
    except tweepy.TweepError as e:
      print e
      return "Failure"
    return "Success"
