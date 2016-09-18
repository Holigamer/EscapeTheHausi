# -*- coding: cp1252 -*-
#Dieses Modul beihnaltet alle Methoden, um Grafiken/Farben im Spiel zu rendern
import pygame, random, main, counter, sys, settings, items;
from constants import *;

##From http://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path##
import imp;

figure = imp.load_source('figure', 'lib/figure.py');
##End From http://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path##

#intern_object represents the object, which the player is in
intern_object = None;

#Übrig gebliebene Sprünge im Spiel.
jumpsLeft = START_JUMPS;


#Checke, ob das Spiel nicht von alleine gestartet wird.
###Kommentiert###
if not __name__ == "__main__":
    pygame.init();
    pygame.display.set_icon(pygame.image.load("models/game/icon.png"));
    pygame.display.set_mode((WIDTH, HEIGHT));
###Ende Kommentiert###

###Kommentiert###
class scrollable_background:
    #Alle Variablen erstmals auf Standart setzen
    img_start, img_repeat, img_last, bb, moveEach, first, last, confirmedLast = None, None, None, None, 1, True, False, False;
    
    #Definiere die Variablen mit Hilfe von Parametern
    def __init__(self, path_first, path_repeat, path_end, move):
        global WIDTH, HEIGHT;
        self.img_start = pygame.transform.scale(pygame.image.load(path_first),(WIDTH, HEIGHT));
        self.img_repeat = pygame.transform.scale(pygame.image.load(path_repeat),(WIDTH, HEIGHT));
        self.img_last = pygame.transform.scale(pygame.image.load(path_end),(WIDTH, HEIGHT));
        self.bb = self.img_repeat.get_rect();
        self.moveEach = move;

    def move(self, screen):
        global WIDTH, HEIGHT, movement_speed;
        #Subtrahiere die X Koordinaten des Bildes.
        self.bb[0] -= self.moveEach;
        #Bilde das Bild mit der gegebenen BoundingBox auf dem Bildschirm
        if self.first:
            screen.blit(self.img_start, self.bb);
        else:
            if self.confirmedLast:
                screen.blit(self.img_last, self.bb);
            else:
                screen.blit(self.img_repeat, self.bb);
        #Erzeuge ein zweites Bild, falls die X Koordinate des ersten Bildes kleiner gleich 0 ist.
        if self.bb[0] <=0:
            #Bilde ein weiteres Bild nach dem Ersten ab. Gucke ob es das Last-Image sein soll
            if self.last:
                screen.blit(self.img_last, [self.bb[0]+WIDTH,self.bb[1]]);
            else:
                screen.blit(self.img_repeat, [self.bb[0]+WIDTH,self.bb[1]]);
        #Setze alles zurück, wenn die X Koordinate kleiner gleich der Negativen Länge des Bildschirmes ist.
        #So muss man nicht die obere Methode in die Unendlichkeit ausführen.
        if self.bb[0] <= -WIDTH:
            self.first = False;
            self.bb[0] = 0;
            if self.last:
                movement_speed = 0;
                self.confirmedLast = True;
        #Falls die Methode irgendwann mal andersherum genutzt werden sollte, wird auch
        #hier der Prozess zurückgetzt.
        if self.bb[0] > WIDTH:
            self.bb[0] = 0;
###Ende Kommentiert###

###Kommentiert###
class object_moving:
    #Variablen innerhalb der Objekt Klasse.
    #img -> Das Bild, welches abgebildet werden soll.
    #bb -> Die Bounding Box des Bildes
    #moveEach -> Um wieviele Pixel soll sich bei jedem Aufruf von move(self, screen) das Objekt bewegen?
    img, bb, moveEach = None, None, 1;

    #Setze die Variablen
    def __init__(self, path, move):
        global WIDTH, HEIGHT;
        self.img = pygame.transform.scale(pygame.image.load(path) ,(100, 100));
        self.bb = self.img.get_rect();
        self.moveEach = move;


    #Bewege das Bild jeden Aufruf von render();
    def move(self, screen):
        global Y_OBJ_FLOOR;
        #Subtrahiere die x Koordiante, um das Bild zu bewegen.
        self.bb[0] -= self.moveEach;
        #Setze die Y Koordiante auf die Y Konstante.
        self.bb[1] = Y_OBJ_FLOOR;
        #Bilde das Bild auf dem Bildschirm ab.
        screen.blit(self.img, self.bb);

    #Teste, ob das Objekt innherhalb der Frame ist.
    def isVisible(self):
        global WIDTH, HEIGHT;
        if self.bb[0] < 0:
            return False;
        if self.bb[0] > WIDTH:
            return False;
        if self.bb[1] < 0:
            return False;
        if self.bb[1] > HEIGHT:
            return False;
        return True;
###Ende Kommentiert###

###Kommentiert###    
pics, path = [],  "models/player";
for i in range(1,5):   
    pics.append(pygame.transform.scale(pygame.image.load(path+"/Move"+str(i)+".png"),RESIZE_PLAYER));
fig = figure.figure(pics);

background1 = scrollable_background("models/game/background/WindowView.png", "models/game/background/WindowView.png", "models/game/background/WindowView.png", 3);
background2 = scrollable_background("models/game/background/StartBG_open.png", "models/game/background/GameBG.png", "models/game/background/GameBG_end.png",7);
###Ende Kommentiert###

###Kommentiert###
objects = [];


#Bilde alle Objekte ab.
def renderObjects(screen):
    global WIDTH;
    if settings.spawn_stuff:
        if random.randint(0,100) == 1:
            obj = object_moving("models/objects/ranzen.png", 7);
            obj.bb[0] = WIDTH -5;
            objects.append(obj);
    if not intern_object == None:
        intern_object.moveEach = movement_speed;
        intern_object.move(screen);
    for object1 in objects:
        if object1.isVisible():
            if not object1 == intern_object:
                object1.moveEach = movement_speed;
                object1.move(screen);
        else:
            objects.remove(object1);
###Ende Kommentiert###
###Kommentiert###
#Teste, ob der gegebene Spielerparameter mit seiner Bounding Box ein Objekt berührt.
def checkForXCol(fig):
    global RESIZE_PLAYER, intern_object;
    pXMin, pXMax = fig.x, fig.x+RESIZE_PLAYER[0];
    intern_object = None;
    for object1 in objects:
        xMin, xMax = object1.bb[0], object1.bb[0]+object1.bb[2];
        if xMin <= pXMax and xMax >=pXMin:
             intern_object = object1;
             return True;
    return False;
        
def checkForYCol(fig):
    global RESIZE_PLAYER;
    pY = fig.y+RESIZE_PLAYER[1];
    for object1 in objects:
        if object1.bb[1] > pY:
            return True;
    return False;
###Ende Kommentiert###
###Kommentiert###
clock = pygame.time.Clock();
movement_speed = 5;
###Ende Kommentiert###

###Kommentiert###
def showTime(screen):
    global FONT_DIR;
    font = pygame.font.Font(FONT_DIR, 20);
    screen.blit(font.render("Gespielte Zeit: "+str(round(counter.play_time, 2)), 1, (0,0,0)), (5,5));
###Ende Kommentiert###
    
#fps_font = pygame.font.SysFont('monospace', 20, True);
    
#def debugFPS(screen):
#    global WIDTH, fps_font, clock;
#    fps = clock.get_fps();
#    fpslabel = fps_font.render(str(round(fps)), True, (255, 255, 255));
#    rec = fpslabel.get_rect(top=5, right=WIDTH - 5);
#    screen.blit(fpslabel, rec);

def renderJumps(screen):
    global FONT_DIR, jumpsLeft;
    font = pygame.font.Font(FONT_DIR, 20);
    if jumpsLeft <1:
        text = font.render("Keine Sprünge verblieben!", 1, (100,0,0));
    else:
        text = font.render("Sprünge verblieben: "+str(jumpsLeft), 1, (0,0,0));
    screen.blit(text, (5,20));

def render():
    global fig, FPS;
    pygame.display.set_icon(pygame.image.load("models/game/icon.png"));
    palette = colors();
    ###Kommentiert###
    clock.tick(FPS);
    screen = pygame.display.get_surface();
    screen.fill(palette.BLACK);
    
    ###Kommentiert###
    background1.move(screen);
    background2.moveEach = movement_speed;
    background2.move(screen);
    ###Ende Kommentiert###

    if checkForXCol(fig) and not checkForYCol(fig):
       fig.x -=movement_speed;
    fig.move(screen, False);
    
    #Bewegliche Objekte#
    renderObjects(screen);
    items.moveItem(screen);
    items.displayPossibleItems(screen);
    #Ende Bewegliche Objekte#
    
    showTime(screen);
    renderJumps(screen);
    #debugFPS(screen);
    pygame.display.flip();

def resetVars():
    global sett, fps_font, movement_speed, clock, pics, path, fig, background1, background2, objects, intern_object, jumpsLeft, START_JUMPS, RESIZE_PLAYER;
    sett = False;
    fps_font =  pygame.font.SysFont('monospace', 20, True);
    movement_speed = 5;
    clock = pygame.time.Clock();
    pics, path = [],  "models/player";
    for i in range(1,5):   
        pics.append(pygame.transform.scale(pygame.image.load(path+"/Move"+str(i)+".png"),RESIZE_PLAYER));
    fig = figure.figure(pics);
    background1 = scrollable_background("models/game/background/WindowView.png", "models/game/background/WindowView.png", "models/game/background/WindowView.png", 3);
    background2 = scrollable_background("models/game/background/StartBG_open.png", "models/game/background/GameBG.png", "models/game/background/GameBG_end.png", 7);
    objects = [];
    intern_object = None;
    jumpsLeft = START_JUMPS;
        
