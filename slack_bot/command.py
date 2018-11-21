import datetime
from weather import Weather, Unit

class Command(object):
  def __init__(self):
    self.commands = { 
      "help" : self.help,
      "cookbook" : self.cookbook,
      "github" : self.github,
      "music" : self.music,
      "weather" : self.weather,
      "when" : self.when
    }
 
  def handle_command(self, user, command):
    response = "<@" + user + ">: "
     
    if command in self.commands:
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
