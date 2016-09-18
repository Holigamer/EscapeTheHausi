# -*- coding: cp1252 -*-
#Dieses Modul beinhaltet Methoden um den Ende Bildschirm anzuzeigen.
import pygame, counter, constants, random, stats, settings, main;

#Diese Variable bestimmt, welcher Text angezeigt wird.
text = "";
highscored = False;

def resetRender():
   global text, highscored;
   text = getTextMessageArray()[random.randint(0, len(getTextMessageArray())-1)];
   highscored = False;
   
def renderBG(screen):
   player = pygame.transform.scale(pygame.image.load("models/player/stand.png"), constants.RESIZE_PLAYER);
   bubble = pygame.transform.scale(pygame.image.load("models/game/parts/speechbubble.png"), (34*3, 16*3));
   img = pygame.transform.scale(pygame.image.load("models/game/background/GameBG_end.png"), (800, 400));
   img2 = pygame.transform.scale(pygame.image.load("models/game/background/WindowView.png"), (800, 400));
   screen.blit(img2, img2.get_rect());
   screen.blit(img, img.get_rect());
   screen.blit(player, (main.render.fig.x, main.render.fig.y));
 #  screen.blit(bubble, (constants.PLAYER_X+40, constants.Y_FLOOR+5));
      
def createSurface():
   bg = pygame.Surface((constants.WIDTH, constants.HEIGHT));
   bg.fill((100,100, 100));
   bg.set_alpha(128);
   return bg;

def createText(text, size, frontColor, fontCenter, shaded, underline, bold):
   font = pygame.font.Font(constants.FONT_DIR, size);
   font.set_underline(underline);
   font.set_bold(underline);
   text, text2 = font.render(text, 1, (0,0,0)), font.render(text, 1, frontColor);
   rect, rect2 = text.get_rect(), text2.get_rect();
   rect.center, rect2.center = fontCenter, (fontCenter[0]-(size/15), fontCenter[1]-(size/15));
   if shaded:
      return [text, rect, text2, rect2];
   else:
      return [text2, rect2, text2, rect2];

def getTextMessageArray():
   if settings.difficulty == 0:
      if int(counter.play_time) < 10:
         return ["Och komm...", "Nutze doch das Hilfemenü.", "Es ist immer zu früh, um aufzugeben!"];
      elif int(counter.play_time) >10 and int(counter.play_time) < 150:
         return ["Mit Easy, war das nicht schwehr...", "Magst du es hier?", "Im Schmerz von gestern liegt die Kraft von heute."];
      elif int(counter.play_time) > 150:
         return ["Lol, das schafft man nicht mehr so oft.", "Suchtgefahr? Oder nicht?", "Auf einfache Wege schickt man nur die Schwachen."];
   elif settings.difficulty == 1:
      if int(counter.play_time) < 10:
         return ["Du kannst das besser!", "Übung macht den Meister."];
      elif int(counter.play_time) >10 and int(counter.play_time) < 150:
         return ["Schade", "Je schwieriger ein Sieg, desto größer die Freude am Gewinnen."];
      elif int(counter.play_time) > 150:
         return ["War das ein Lag?", "Wer etwas will, findet Wege."];
   elif settings.difficulty == 2:
      if int(counter.play_time) < 10:
         return ["Dein erstes Mal?", "Hard ist halt hart...", "Mach weiter!"];
      elif int(counter.play_time) >10 and int(counter.play_time) < 150:
         return ["Deine Zeit war: "+str(round(counter.play_time, 2)), "Renn weiter", "Willst du nun aufgeben?"];
      elif int(counter.play_time) > 150:
         return ["Es wäre besser, wenn du aufhörst :D"];
      
resetRender();

def renderEndMessage(color, fontCenter, screen):
   global text;
   font = createText(text, 30, (217, 30, 30), (400,80), True, False, False);
   renderText(font, screen);

def renderText(textArray, screen):
      screen.blit(textArray[0], textArray[1]);
      screen.blit(textArray[2], textArray[3]);

def renderEnd():
    global pre_render_complete, highscored;
    screen = pygame.display.get_surface();
     #  if not pre_render_complete:
    pygame.display.set_icon(pygame.image.load("models/game/icon2.png"));
    renderBG(screen);
    
    screen.blit(createSurface(), (0,0));
    renderText(createText("Game Over", 75, (245,124,0), (400, 40), True, False, False), screen);
    renderEndMessage((194,73,33), (400,80), screen);
    renderText(createText("Gespielte Zeit: "+str(round(counter.play_time, 2)), 25, (245,124,0), (400, 125), True, False, False),screen);
         
    ##Run Stats##
    if stats.isHighScoredTime(float(round(counter.play_time, 2))) or highscored:
       highscored = True;
       stats.setHighestTime(float(round(counter.play_time, 2)));
       renderText(createText("Neuer Rekord: "+str(stats.getHighestTime()), 25, (0, 150, 0), (400, 150), True, True, True), screen);
    else:
       renderText(createText("Beste Zeit:  "+str(stats.getHighestTime()), 25, (245,124,0), (400, 150), True, False, False), screen);
    leavethegame = pygame.image.load("models/game/buttons/pause_ltg_selected.png");
    rect = leavethegame.get_rect();
    rect.center = (400, 250);
    screen.blit(leavethegame, rect);
    pygame.display.flip();

   
