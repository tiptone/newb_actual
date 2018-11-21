import datetime

class Command(object):
  def __init__(self):
    self.commands = { 
      "help" : self.help,
      "cookbook" : self.cookbook,
      "github" : self.github,
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
    return "https://github.com/theDevilsVoice/newb_actual"

  def when(self):
    delta = datetime.datetime(2019, 4, 26) - datetime.datetime.now()
    response = "Countdown to RussCon 2019: " + str(delta) + "\r\n"
    return response
     
  def help(self):
    response = "Currently I support the following commands:\r\n"
         
    for command in self.commands:
      response += command + "\r\n"
             
    return response
