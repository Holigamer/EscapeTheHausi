#Dieses Modul beinhaltet Methoden um den Credits Bildschirm anzuzeigen.
import pygame, constants;

##Kopiert aus start_screen##
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
   rect.topleft, rect2.topleft = fontTopLeft, (fontTopLeft[0]-(size/15), fontTopLeft[1]-(size/15));
   if shaded:
      return [text, rect, text2, rect2, size/15];
   else:
      return [text2, rect2, text2, rect2, size/15];

def renderText(textArray, screen):
      screen.blit(textArray[0], textArray[1]);
      screen.blit(textArray[2], textArray[3]);
##Ende Kopiert aus start_screen##

def renderTextPos(textArray, posArray, screen):
   screen.blit(textArray[0], posArray);
   screen.blit(textArray[2], (posArray[0]-textArray[4], posArray[1]-textArray[4]));

def renderCredits():
   screen = pygame.display.get_surface();
   title = createText("Credits:", 75, (245, 124, 0), (300, 15), True);

   color = (227, 181, 132);

   AS = createText("Aleksander S.", 25, color, (200, 125), True);
   POAS = createText("Paul O. und Aleksander S.", 25, color, (200, 125), True);
   ES = createText("Eric Skiff (ericskiff.com)", 25, color, (200, 125), True);
   FONT = createText("Brady Brunch", 25, color, (200, 125), True)
   
   renderBG(screen);
   screen.blit(createSurface(), (0,0));
   renderText(title, screen);

   
   renderText(createText("Ersteller", 25, color, (200, 100), True), screen);
   renderTextPos(POAS, (400, 100), screen);
   renderText(createText("Programming", 25, color, (200, 125), True), screen);
   renderTextPos(AS, (400, 125), screen);
   renderText(createText("Hintergrund", 25, color, (200, 150), True), screen);
   renderTextPos(AS, (400, 150), screen);
   renderText(createText("Items", 25, color, (200, 175), True), screen);
   renderTextPos(POAS, (400, 175), screen);
   renderText(createText("Spieler", 25, color, (200, 200), True), screen);
   renderTextPos(AS, (400, 200), screen);
   renderText(createText("Figuren", 25, color, (200, 225), True), screen);
   renderTextPos(AS, (400, 225), screen);
   renderText(createText("Musik", 25, color, (200, 250), True), screen);
   renderTextPos(ES, (400, 250), screen);
   renderText(createText("Schrift", 25, color, (200, 275), True), screen);
   renderTextPos(FONT, (400, 275), screen);


   pygame.display.flip();
   
