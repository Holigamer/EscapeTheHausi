# -*- coding: cp1252 -*-
#Dieses Modul beinhaltet Methoden um den Start Bildschirm anzuzeigen.
import pygame, time, random, constants, settings, imp, stats;

#Animiere den Mund des Spielers. Hierzu wird dieselbe Spielerklasse benutzt, wie auch im render.py Modul.
figure = imp.load_source('figure', 'lib/figure.py');

pics, path = [],  "models/player";
for i in range(10):
   pics.append(pygame.transform.scale(pygame.image.load(path+"/stand.png"),constants.RESIZE_PLAYER));
for i in range(14):
   pics.append(pygame.transform.scale(pygame.image.load(path+"/stand2.png"),constants.RESIZE_PLAYER));
fig = figure.figure(pics);

#Die hier angegebene Zahl zeigt die ausgewählte Option an.
#Index: 0: Spielen, 1: Credits, 2: Verlassen
sel_option = 0;

#Easteregg
curr_teacher = None;

class teacher:
   img, time = None, 0;

def renderBG(screen):
   bubble = pygame.transform.scale(pygame.image.load("models/game/parts/speechbubble.png"), (34*3, 16*3));
   img = pygame.transform.scale(pygame.image.load("models/game/background/StartBG_close.png"), (800, 400));
   img2 = pygame.transform.scale(pygame.image.load("models/game/background/WindowView.png"), (800, 400));
   screen.blit(img2, img2.get_rect());
   screen.blit(img, img.get_rect());
   fig.move(screen, True);
   screen.blit(bubble, (constants.PLAYER_X+40, constants.Y_FLOOR+5));


def createSurface():
   bg = pygame.Surface((constants.WIDTH, constants.HEIGHT));
   bg.fill((100,100, 100));
   bg.set_alpha(128);
   return bg;

def createText(text, size, frontColor, frontCenter, shaded):
   font = pygame.font.Font(constants.FONT_DIR, size);
   text, text2 = font.render(text, 1, (0,0,0)), font.render(text, 1, frontColor);
   rect, rect2 = text.get_rect(), text2.get_rect();
   rect.center, rect2.center = frontCenter, (frontCenter[0]-(size/15), frontCenter[1]-(size/15));
   if shaded:
      return [text, rect, text2, rect2, (size/15)];
   else:
      return [text2, rect2, text2, rect2, (size/15)];

def renderText(textArray, screen):
      screen.blit(textArray[0], textArray[1]);
      screen.blit(textArray[2], textArray[3]);

def renderTextPos(textArray, pos,  screen):
      screen.blit(textArray[0], (pos[0], pos[1]));
      screen.blit(textArray[2],  (pos[0]-textArray[4], pos[1]-textArray[4]));

def renderButtons(screen):
   screen.blit(pygame.image.load("models/game/buttons/start_stg"+getOption(0)+".png"), (100, 150));
   screen.blit(pygame.image.load("models/game/buttons/start_help"+getOption(1)+".png"), (100, 250));
   screen.blit(pygame.image.load("models/game/buttons/start_credits"+getOption(2)+".png"), (440, 150));
   screen.blit(pygame.image.load("models/game/buttons/start_ltg"+getOption(3)+".png"), (440, 250));

def getOption(nr):
   global sel_option;
   if nr == sel_option:
      return "_selected";
   else:
      return "";

def renderSounds(screen):
   if settings.music_enabled:
      screen.blit(pygame.image.load("models/game/parts/note_on.png"), (750, 5));
   else:
      screen.blit(pygame.image.load("models/game/parts/note_off.png"), (750, 5));
   if settings.sounds_enabled:
      screen.blit(pygame.image.load("models/game/parts/speaker_on.png"), (775, 5));
   else:
      screen.blit(pygame.image.load("models/game/parts/speaker_off.png"), (775, 5));
      
def onButtonEvent(event):
   global sel_option;
   if event.key == pygame.K_DOWN:
      if sel_option == 0 or sel_option == 2:
         sel_option +=1;
         playSelectSound();
   elif event.key == pygame.K_UP:
      if sel_option == 1 or sel_option == 3:
         sel_option -=1;
         playSelectSound();
   elif event.key == pygame.K_RIGHT:
      if sel_option == 0:
         sel_option = 2;
         playSelectSound();
      elif sel_option == 1:
         sel_option = 3;
         playSelectSound();
   elif event.key == pygame.K_LEFT:
      if sel_option == 2:
         sel_option = 0;
         playSelectSound();
      elif sel_option == 3:
         sel_option = 1;
         playSelectSound();

def playSelectSound():
   if settings.sounds_enabled:
      sound = pygame.mixer.Sound("models/game/sounds/select.wav");
      sound.set_volume(0.04);
      sound.play();

def renderDifficulty(screen):
      renderTextPos(createText("Difficulty: ",  25, (245,124,0), (350, 125), True), (350, 125), screen);
      if settings.difficulty == 0:
         renderTextPos(createText("Easy",  25, (0,150,0), (450, 125), True), (440, 125), screen);
      elif settings.difficulty == 1:
         renderTextPos(createText("Normal",  25, (242,130,56), (450, 125), True), (440, 125),screen);
      elif settings.difficulty == 2:
         renderTextPos(createText("Hard",  25, (150,0,0), (450, 125), True), (440, 125), screen);

def renderTutorial(screen):
   #settings.play_tutorial or
    if not stats.hasPlayedBefore():
       screen.blit(pygame.image.load("models/game/parts/tutorial_on.png"), (10, 5));
    else:
       screen.blit(pygame.image.load("models/game/parts/tutorial_off.png"), (10, 5));

def renderStart():
   screen = pygame.display.get_surface();

   title = createText("Escape The Hausi", 75, (245,124,0), (400,50), True);
   subtitle = createText("Informatikarbeit Diffkurs 8. Klasse", 25, (245,124,0), (400, 100), True);
   hInfo = createText("[Pfeiltasten], [Enter] und [ESC] um zu navigieren", 25, (255,255,255), (400, 360), False);
   renderBG(screen);
   randomlySpawnTeacher(screen);
   screen.blit(createSurface(), (0,0));
   renderText(title, screen);
   renderText(subtitle, screen);
   renderText(hInfo, screen);
   renderDifficulty(screen);
   renderButtons(screen);
   renderSounds(screen);
   renderTutorial(screen);
   pygame.display.flip();

def randomlySpawnTeacher(screen):
   global curr_teacher;
   currTime = time.time();
   if curr_teacher == None:
      if random.randint(0, 100) == 1:
         curr_teacher = teacher();
         curr_teacher.img = pygame.transform.scale(pygame.image.load("models/game/teacher/Herr_Brand.png"), (40, 60));
         curr_teacher.time = currTime+5+random.randint(0,5);
      elif random.randint(0, 100)==2:
         curr_teacher = teacher();
         curr_teacher.img = pygame.transform.scale(pygame.image.load("models/game/teacher/Herr_Kern.png"), (40, 60));
         curr_teacher.time = currTime+5+random.randint(0,5);
   else:
      screen.blit(curr_teacher.img, (750, 159));
      if currTime >= curr_teacher.time:
         curr_teacher = None;

def resetRender():
   global sel_option;
   sel_option = 0;
   
