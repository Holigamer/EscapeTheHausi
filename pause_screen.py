#Dieses Modul beinhaltet Methoden um den Pause Bildschirm anzuzeigen.
import pygame, constants;

#0 -> Back To Game Ausgewählt
#alles andere -> Leave The Game Ausgewählt
option = 0;

#Wenn True, wurden manche Elemente bereits einmal gerendert.
pre_render_complete = False;

def chooseNext():
   global option;
   if option == 0:
      option = 1;
   else:
      option = 0;
      
def createSurface():
   bg = pygame.Surface((800, 400));
   bg.fill((100,100, 100));
   bg.set_alpha(128);
   return bg;

def createText():
   font = pygame.font.Font(constants.FONT_DIR, 75);
   text, text2 = font.render("Spiel Pausiert", 1, (0,0,0)), font.render("Spiel Pausiert", 1, (245,124,0));
   rect, rect2 = text.get_rect(), text2.get_rect();
   rect.center, rect2.center = (400, 90), (395, 85);
   return [text, rect, text2, rect2];

def renderPause():
   global pre_render_complete;
   screen = pygame.display.get_surface();
   if not pre_render_complete:
      screen.blit(createSurface(), (0,0));
      screen.blit(createText()[0], createText()[1]);
      screen.blit(createText()[2], createText()[3]);
      pre_render_complete = True;
   if option == 0:
      backtogame = pygame.image.load("models/game/buttons/pause_btg_selected.png");
      leavethegame = pygame.image.load("models/game/buttons/pause_ltg.png");
   else:
      backtogame = pygame.image.load("models/game/buttons/pause_btg.png");
      leavethegame = pygame.image.load("models/game/buttons/pause_ltg_selected.png");
   screen.blit(backtogame, (250, 150));
   screen.blit(leavethegame, (250, 250));
   pygame.display.flip();

def resetRender():
   global pre_render_complete, option;
   pre_render_complete = False;
   option = 0;
   
