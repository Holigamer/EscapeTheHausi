import time, settings;
from constants import *;

#Spielstartzeit:
start_time = time.time();

#Spielzeit:
play_time = 0;

#Zeit vor der Letzen Pause
time_before_pause = 0;

#Letzes Modulo:
last_modulo_time = 1;

#Ist der Time Pausiert?
paused = True;

def pause():
   global play_time, time_before_pause, paused;
   if not paused:
      time_before_pause = play_time;
      paused = True;
      
def unpause():
   global start_time, paused;
   if paused:
      start_time = time.time();
      paused = False;

def updateTime():
   global start_time, play_time, paused, time_before_pause;
   if not paused:
      play_time = time.time()-start_time+time_before_pause;

def speedUP(input_speed):
    global SPEEDUP_DELAY_MODULO_EASY, SPEEDUP_DELAY_MODULO_NORMAL, SPEEDUP_DELAY_MODULO_HARD, last_modulo_time;
    modulo = SPEEDUP_DELAY_MODULO_EASY;
    
    if settings.difficulty == 0:
       modulo = SPEEDUP_DELAY_MODULO_EASY;
    elif settings.difficulty == 1:
       modulo = SPEEDUP_DELAY_MODULO_NORMAL;
    elif settings.difficulty == 2:
       modulo = SPEEDUP_DELAY_MODULO_HARD;
      
    if round(play_time) %modulo==0 and not last_modulo_time==round(play_time):
       last_modulo_time = round(play_time);
       return input_speed+1;
    return input_speed;

def reset():
   global play_time, start_time, last_modulo_time, time_before_pause, paused;
   play_time = 0;
   start_time = time.time();
   time_before_pause = 0;
   last_modulo_time = 1;
   paused = True;
   
       
