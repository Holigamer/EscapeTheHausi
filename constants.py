# -*- coding: utf-8 -*-
#Dieses Modul wird ein paar konstante Werte für das Spiel beinhalten.

#Die Dimensionen des Bildschirmes
WIDTH = 800;
HEIGHT = 400;

#Gravitationsvariable für z.B. jump() Prozeduren.
GRAVITY = 1.8;

#Die Y Koordinate, bei welcher der Spieler sich 'auf dem Boden' befindet.
Y_FLOOR = 100;

#Die Y Koordinate, bei welcher sich Objekte 'auf dem Boden' befinden.
Y_OBJ_FLOOR = 250;

#Die Y Koordinate, auf welcher Items generiert werden.
Y_ITM_FLOOR = 25;

#Frames Per Second Delay Var
FPS = 60;

#Die Resize Größe vom Spieler:
#140, 260
RESIZE_PLAYER = (140, 260);

#Die Player X Coordinate
PLAYER_X = 350;

#Der Ort, wo sich die Spielfont befindet:
FONT_DIR = "models/game/font.ttf";

#Im Abstand von wievielen Sekunden wird das Spiel schneller (Am besten volle Zahl).
SPEEDUP_DELAY_MODULO_EASY = 5;
SPEEDUP_DELAY_MODULO_NORMAL = 2;
SPEEDUP_DELAY_MODULO_HARD = 1;

#Wieviele Sprünge hat man am Anfang:
START_JUMPS = 50;

#Minimale Bewegungsgeschwindigkeit
MIN_MOVEMENT_SPEED = 5;

#Die Farben Klasse
class colors: 
   BLACK = (0,0,0);
