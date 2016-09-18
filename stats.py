#In diesem Modul werden sich Prozeduren, um Stats des Spieles zu speichern.
import ConfigParser, settings;

config = ConfigParser.ConfigParser();

def getHighestTime():
   config.read("data/stats.ini");
   if config.has_option('gamestats', 'besttime'+str(settings.difficulty)):
      return config.get('gamestats', 'besttime'+str(settings.difficulty));
   else:
      setHighestTime(0);
      return getHighestTime();

def setHighestTime(high):
   FILE = open("data/stats.ini", 'w');
   config.read("data/stats.ini");
   if not config.has_section('gamestats'):
      config.add_section('gamestats');
   if config.has_option('gamestats', 'besttime'+str(settings.difficulty)):
      if isHighScoredTime(high):
         config.set('gamestats', 'besttime'+str(settings.difficulty), str(high));
   else:
      config.set('gamestats', 'besttime'+str(settings.difficulty), str(high));
   config.write(FILE);
   FILE.close();

def isHighScoredTime(high):
   time = getHighestTime();
   return float(high) > float(time);

def hasPlayedBefore():
   config.read("data/stats.ini");
   if config.has_option('info', 'firsttime'):
      return config.getboolean('info', 'firsttime');
   else:
      setPlayedBefore(False);
      return hasPlayedBefore();
   
def setPlayedBefore(boolean):
   FILE = open("data/stats.ini", 'w');
   config.read("data/stats.ini");
   if not config.has_section('info'):
      config.add_section('info');
   config.set('info', 'firsttime', boolean);
   config.write(FILE);
   FILE.close();
