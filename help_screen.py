# -*- coding: cp1252 -*-
#In diesem Modul befinden sich Methoden um das Hilfe-Menü anzuzeigen.
import pygame, constants;

##Kopiert aus credits_screen##
def renderBG(screen):
   img = pygame.transform.scale(pygame.image.load("models/game/background/StartBG_close.png"), (800, 400));
   img2 = pygame.transform.scale(pygame.image.load("models/game/background/WindowView.png"), (800, 400));
   screen.blit(img2, img2.get_rect());
   screen.blit(img, img.get_rect());


def createSurface():
   bg = pygame.Surface((constants.WIDTH, constants.HEIGHT));
   bg.fill((100,100, 100));
   bg.set_alpha(128);
   return bg;

def createText(text, size, frontColor, fontTopLeft, shaded):
   font = pygame.font.Font(constants.FONT_DIR, size);
   text, text2 = font.render(text, 1, (0,0,0)), font.render(text, 1, frontColor);
   rect, rect2 = text.get_rect(), text2.get_rect();
   rect.center, rect2.center = fontTopLeft, (fontTopLeft[0]-(size/15), fontTopLeft[1]-(size/15));
   if shaded:
      return [text, rect, text2, rect2];
   else:
      return [text2, rect2, text2, rect2];

def renderText(textArray, screen):
      screen.blit(textArray[0], textArray[1]);
      screen.blit(textArray[2], textArray[3]);


def renderHelp():
   screen = pygame.display.get_surface();
   title = createText("Hilfe:", 75, (245, 124, 0), (400, 50), True);

   color = (227, 181, 132);
   
   renderBG(screen);
   screen.blit(createSurface(), (0,0));
   renderText(title, screen);
   
   renderText(createText("[LEERTASTE] um zu springen", 25, color, (400, 100), True), screen);
   renderText(createText("[UP], [DOWN] um zwischen Powerups zu wechseln", 25, color, (400, 125), True), screen);
   renderText(createText("[ENTER] um ein Powerup zu nutzen", 25, color, (400, 150), True), screen);
   renderText(createText("[F] um zwischen Vollbild und Normal zu wechseln", 25, color, (400, 175), True), screen);
   renderText(createText("[M] um Musik aus-/anzuschalten (nur im Menü)", 25, color, (400, 200), True), screen);
   renderText(createText("[S] um Sounds aus-/anzuschalten (nur im Menü)", 25, color, (400, 225), True), screen);
   renderText(createText("[D] um die Difficulty zu ändern (nur im Startmenü)", 25, color, (400, 250), True), screen);
   renderText(createText("[T] um das Starttutorial zu aktivieren (nur im Startmenü)", 25, color, (400, 275), True), screen);
   renderText(createText("[ESC] um das Spiel zu pausieren", 25, color, (400, 300), True), screen);

   pygame.display.flip();
##Ende Kopiert aus credits_screen##
