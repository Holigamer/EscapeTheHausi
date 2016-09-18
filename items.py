#In diesem Modul befinden sich Methoden, um Items zu generieren, sie anzuzeigen und ihnen Powerups zu geben.
import pygame, render, random, settings;
from constants import *;

###Kommentiert###
#Das jetzige Item, welches auf dem Bildschirm abgebildet wird.
curr_item = None;

#Anzahl an Items, welche der Spieler besitzt.
#Indexing: 0: CLOCKItems
itemsArray = [];
def fillArray():
    global itemsArray;
    itemsArray = [];
    if settings.difficulty == 0:
        for i in range(3):
            itemsArray.append(5);
    elif settings.difficulty == 1:
        for i in range(3):
            itemsArray.append(2);
    elif settings.difficulty == 2:
        for i in range(3):
            itemsArray.append(0);
            
fillArray();
#Das mit den Tasten genommene Item:
chosen_item = 0;

class item_type:
    CLOCK = 0;
    RIEGEL = 1;
    APFEL = 2;

class item_moving:
    #Variablen innerhalb der Item Klasse.
    #img -> Das Bild, welches abgebildet werden soll.
    #bb -> Die Bounding Box des Bildes
    #moveEach -> Um wieviele Pixel soll sich bei jedem Aufruf von move(self, screen) das Objekt bewegen?
    img, bb, moveEach, itm_type = None, None, 1, 0;

    #Setze die Variablen
    def __init__(self, path, move, itm_type):
        self.img = pygame.image.load(path);
        self.bb = self.img.get_rect();
        self.moveEach = move;
        self.itm_type = itm_type;

    #Bewege das Bild jeden Aufruf von render();
    def move(self, screen):
        global Y_ITM_FLOOR;
        #Subtrahiere die x Koordiante, um das Bild zu bewegen.
        self.bb[0] -= self.moveEach;
        #Setze die Y Koordiante auf die Y Konstante.
        self.bb[1] = Y_ITM_FLOOR;
        #Bilde das Bild auf dem Bildschirm ab.
        screen.blit(self.img, self.bb);

    #Teste, ob das Item innherhalb der Frame ist.
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
def handleEnter():
    global chosen_item, itemsArray, MIN_MOVEMENT_SPEED, PLAYER_X;
    if chosen_item == item_type.CLOCK:
        if isItemAt(0):
            if render.movement_speed > MIN_MOVEMENT_SPEED:
                render.movement_speed -=1;
                itemsArray[0] -=1;
    elif chosen_item == item_type.RIEGEL:
        if isItemAt(1):
            if render.fig.x < PLAYER_X:
                render.fig.x += 150;
                if render.fig.x > PLAYER_X:
                    render.fig.x = PLAYER_X;
                itemsArray[1] -=1;
    elif chosen_item == item_type.APFEL:
        if isItemAt(2):
            render.jumpsLeft += 5;
            itemsArray[2] -=1;
            
def isItemAt(index):
    global itemsArray;
    if index <= len(itemsArray)-1:
        if itemsArray[index] >=1:
            return True;
    return False;
###Ende Kommentiert###
###Kommentiert###
def choseDown():
    global chosen_item;
    if chosen_item == item_type.CLOCK:
        chosen_item = 1;
    elif chosen_item == item_type.RIEGEL:
        chosen_item = 2;
        
def choseUp():
    global chosen_item;
    if chosen_item == item_type.RIEGEL:
        chosen_item = 0;
    elif chosen_item == item_type.APFEL:
        chosen_item = 1;
###Ende Kommentiert###
 ###Kommentiert###       
def displayPossibleItems(screen):
    global chosen_item, WIDTH;
    background, mark = pygame.Surface((100, 75)), pygame.Surface((100, 25));
    background.fill((0,0,0));
    mark.fill((0,0,0));
    background.set_alpha(50);
    mark.set_alpha(50);
    screen.blit(background, (WIDTH-100, 0));
    for i in range(3):
        if chosen_item==i:
            screen.blit(mark, (WIDTH-100, i*25));
    for i in range(3):
        renderAmount(i, (WIDTH-95, i*25), screen);

def renderAmount(index, pos, screen):
    global itemsArray;
    font = pygame.font.Font(render.FONT_DIR, 20);
    typus = "";
    amount = 0;
    if index == item_type.CLOCK:
        typus = "Uhr";
        if len(itemsArray)>=1:
            amount = itemsArray[0];
    elif index == item_type.RIEGEL:
        typus = "Riegel";
        if len(itemsArray)>=2:
            amount = itemsArray[1];
    elif index == item_type.APFEL:
        typus = "Apfel";
        if len(itemsArray)>=3:
            amount = itemsArray[2];
    text = font.render("["+typus+"] * "+str(amount), 1, (255,255,255));
    screen.blit(text, pos);
###Ende Kommentiert###
###Kommentiert###
def moveItem(screen):
    global curr_item, itemsArray;
    if not curr_item == None:
        curr_item.moveEach = render.movement_speed;
        curr_item.move(screen);
        if not curr_item.isVisible():
            curr_item = None;
        if checkForXCol(render.fig) and checkForYCol(render.fig):
            itemsArray[curr_item.itm_type] +=1;
            curr_item = None;
    else:
        if settings.spawn_stuff:
            if random.randint(0, 300)==1:
                if random.randint(0, 2)==1:
                    curr_item = item_moving("models/items/Uhr.png", render.movement_speed, item_type.CLOCK);
                    curr_item.bb[0] = render.WIDTH-5;
                elif random.randint(0, 5)==1:
                    curr_item = item_moving("models/items/Riegel.png", render.movement_speed, item_type.RIEGEL);
                    curr_item.bb[0] = render.WIDTH-5;
                else:
                    curr_item = item_moving("models/items/Apfel.png", render.movement_speed, item_type.APFEL);
                    curr_item.bb[0] = render.WIDTH-5;
            
def checkForXCol(fig):
    global curr_item, RESIZE_PLAYER;
    if not curr_item == None:
        if  curr_item.bb[0] <= (fig.x+RESIZE_PLAYER[0]) and curr_item.bb[0]+curr_item.bb[2] >= fig.x:
            return True;
    return False;
        
def checkForYCol(fig):
    global curr_item;
    if not curr_item == None:
        if curr_item.bb[1]+curr_item.bb[3] > fig.y:
            return True;
    return False;
###Ende Kommentiert###

def resetItems():
    global curr_item, itemsArray, chosen_item;
    curr_item = None;
    itemsArray = [];
    fillArray();
    chosen_item = 0;
