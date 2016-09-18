# -*- coding: cp1252 -*-
#Dieses Modul beinhaltet Prozeduren, um die Spielmechaniken zu erklären (für Einsteiger)
import pygame, constants, imp;

explains = imp.load_source('explains', 'lib/explains.py');

#Die ID des jetzigen Panels
curr_panel = 0;

def onButtonEvent(event):
   global curr_panel;
   if event.key==pygame.K_RIGHT or event.key==pygame.K_RETURN:
      curr_panel +=1;
      if explains.get_option(curr_panel) == True:
         reset();
         return True;
   elif event.key==pygame.K_LEFT:
      curr_panel -=1;
      if not explains.get_option(curr_panel):
         curr_panel +=1;
   return False;

def renderText(screen):
   global curr_panel;
   font, newBeginning, strings = pygame.font.Font(constants.FONT_DIR, 25), 25, explains.get_option(curr_panel)[2].split('%new%');

   if len(strings) >3:
      print "Ein Fehler ist beim rendern der explain_screen Texte: Der Text kann maximal 3 mal gesplittet werden! Zu viel um: "+str(len(strings)-3);
   else:
      for string in strings:
         text = font.render(string, 1, (255, 255, 255));
         rect = text.get_rect();
         rect.center = (constants.WIDTH/2, constants.HEIGHT-100+newBeginning);
         screen.blit(text, rect);
         newBeginning += 25;
         
def renderTextBackground(screen):
   surface = pygame.Surface((constants.WIDTH, 100));
   surface.fill((0,0,0));
   screen.blit(surface, (0, constants.HEIGHT-100));
         
def renderHead(screen):
   global curr_panel;
   option = explains.get_option(curr_panel)[0];
   img = pygame.transform.scale(pygame.image.load("models/game/faces/face_"+str(option)+".png"), (16*7, 15*7));
   screen.blit(img, (50, constants.HEIGHT-150));

def renderIMG(screen):
   global curr_panel;
   option = explains.get_option(curr_panel)[1];
   if not option == "none":
      img = pygame.transform.scale(pygame.image.load(option), (500, 250));
      screen.blit(img, (150, 25));
      pygame.draw.rect(screen, (145, 100, 10), [150,25,500,250],10);
      
def renderExplain():
   screen = pygame.display.get_surface();
   screen.fill((50,50,50));

   renderTextBackground(screen);
   renderText(screen);
   renderIMG(screen);
   renderHead(screen);

   pygame.display.flip();

def reset():
   global curr_panel;
   curr_panel = 0;
