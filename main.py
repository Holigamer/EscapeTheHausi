# -*- coding: cp1252 -*-
#Dies ist das Hauptmodul, welches das Programm starten wird.
import pygame, sys, counter, render, pause_screen, start_screen, credits_screen, help_screen, end_screen, explain_screen, settings, items, time, stats;
from constants import *;
from functions import *;

pygame.init();
pygame.display.set_caption("Escape The Hausi");

class gamestate:
    PLAY = 0;
    PAUSED = 1;
    START = 2;
    END = 3;
    CREDITS = 4;
    HELP = 5;
    EXPLAIN = 6;

#Wenn dies True ist, wird das Pausenmenü blockiert. (Hilfreich für die render annimation beim Tod)

block_pause = False;

#Solange diese auf True ist, wird das Spiel laufen.
isRunning = True;

#Gamestate Variable. Diese Varaible entscheidet, wie der Bildschirm dargestellt wird.
GAMEMODE = gamestate.START;


def listenForKeys():
    global isRunning, GAMEMODE, block_pause;
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           isRunning = False;
        if event.type == pygame.KEYDOWN:
            #START
            if GAMEMODE == gamestate.START:
                start_screen.onButtonEvent(event);
            #EXPLAIN
            elif GAMEMODE == gamestate.EXPLAIN:
                 if explain_screen.onButtonEvent(event):
                     startGame();
            #Sounds
            if event.key == pygame.K_s:
                if GAMEMODE == gamestate.START or GAMEMODE == gamestate.CREDITS or GAMEMODE == gamestate.HELP:
                    settings.sounds_enabled = not settings.sounds_enabled;
            #Music
            if event.key == pygame.K_m:
                 if GAMEMODE == gamestate.START or GAMEMODE == gamestate.CREDITS or GAMEMODE == gamestate.HELP:
                    settings.music_enabled = not settings.music_enabled;
                    if settings.music_enabled:
                        pygame.mixer.music.unpause();
                    else:
                        pygame.mixer.music.pause();
            ##Leertaste
            if event.key == pygame.K_SPACE:
                if GAMEMODE == gamestate.PLAY:
                    render.fig.jump();
            ##Escape
            elif event.key == pygame.K_ESCAPE:
                if GAMEMODE == gamestate.PLAY and not block_pause:
                    if settings.music_enabled:
                        pygame.mixer.music.pause();
                    GAMEMODE = gamestate.PAUSED;
                    counter.pause();
                elif GAMEMODE == gamestate.PAUSED:
                    pauseToGame();
                elif GAMEMODE == gamestate.CREDITS or GAMEMODE == gamestate.HELP:
                    GAMEMODE = gamestate.START;
            ##Down
            elif event.key == pygame.K_DOWN:
                if GAMEMODE == gamestate.PAUSED:
                    pause_screen.chooseNext();
                elif GAMEMODE == gamestate.PLAY:
                    items.choseDown();
            ##Up
            elif event.key == pygame.K_UP:
                if GAMEMODE == gamestate.PAUSED:
                    pause_screen.chooseNext();
                elif GAMEMODE == gamestate.PLAY:
                    items.choseUp();
            ##Return
            elif event.key == pygame.K_RETURN:
                ##Pause Screen Keys##
                if GAMEMODE == gamestate.PAUSED:
                    if pause_screen.option == 0:
                        pauseToGame();
                    else:
                        toMenu();
                ##Start Screen Keys##
                elif GAMEMODE == gamestate.START:
                    if start_screen.sel_option == 0:
                        if stats.hasPlayedBefore():
                            startGame();
                        else:
                            stats.setPlayedBefore(True);
                            GAMEMODE = gamestate.EXPLAIN;
                    elif start_screen.sel_option == 1:
                        GAMEMODE = gamestate.HELP;
                    elif start_screen.sel_option == 2:
                        GAMEMODE = gamestate.CREDITS;
                    elif start_screen.sel_option == 3:
                        isRunning = False;
                ##End Screen Key##
                elif GAMEMODE == gamestate.END:
                    toMenu();
                ##Ingame Keys##
                elif GAMEMODE == gamestate.PLAY:
                    items.handleEnter();
            ##F
            elif event.key == pygame.K_f:
                toggle_fullscreen();
            ##D
            elif event.key == pygame.K_d:
                if GAMEMODE == gamestate.START:
                    settings.difficulty +=1;
                    if settings.difficulty >2:
                        settings.difficulty = 0;
            ##T
            elif event.key == pygame.K_t:
                if GAMEMODE == gamestate.START:
                    stats.setPlayedBefore(not stats.hasPlayedBefore());

def startGame():
    global GAMEMODE, block_pause;
    if settings.music_enabled:
        pygame.mixer.music.load("models/game/ambient/game-ambient-2.wav");
        pygame.mixer.music.set_volume(0.4);
        pygame.mixer.music.play(-1, 0.0);
    GAMEMODE = gamestate.PLAY;
    settings.spawn_stuff = True;
    block_pause = False;
    items.fillArray();
    counter.unpause();
    start_screen.resetRender();

def pauseToGame():
    global GAMEMODE;
    GAMEMODE = gamestate.PLAY;
    counter.unpause();
    pause_screen.resetRender();
    if settings.music_enabled:
        pygame.mixer.music.unpause();
        

def toMenu():
    global GAMEMODE;
    pause_screen.resetRender();
    render.resetVars();
    counter.reset();
    items.resetItems();
    GAMEMODE = gamestate.START;
    if settings.music_enabled:
        pygame.mixer.music.load("models/game/ambient/theme.wav");
        pygame.mixer.music.set_volume(0.4);
        pygame.mixer.music.play(-1, 0.0);
 
        
def testForEnd():
    global GAMEMODE, block_pause;
    if not render.fig.isVisible():
        if GAMEMODE == gamestate.PLAY:
            block_pause = True;
            settings.spawn_stuff = False;
            render.movement_speed = 5;
            render.objects = [];
            render.background1.moveEach = 0;
            render.background2.last = True;
            render.fig.x = PLAYER_X;
            render.fig.canJump = False;
            counter.pause();
            items.resetItems();
            if settings.music_enabled:
                pygame.mixer.music.load("models/game/ambient/end.wav");
                pygame.mixer.music.set_volume(0.2);
                pygame.mixer.music.play(-1, 0.0);

def start():
   global GAMEMODE, isRunning;
   while isRunning:
        testForEnd();
        if GAMEMODE == gamestate.PLAY:
           #Zeit
           counter.updateTime();
           render.movement_speed = counter.speedUP(render.movement_speed);
           #Bild
           render.render();
           #Endtest:
           if render.movement_speed <=0:
               GAMEMODE = gamestate.END;
               end_screen.resetRender();
        elif GAMEMODE == gamestate.START:
             start_screen.renderStart();
        elif GAMEMODE == gamestate.PAUSED:
            pause_screen.renderPause();
        elif GAMEMODE == gamestate.END:
            end_screen.renderEnd();
        elif GAMEMODE == gamestate.CREDITS:
            credits_screen.renderCredits();
        elif GAMEMODE == gamestate.HELP:
            help_screen.renderHelp();
        elif GAMEMODE == gamestate.EXPLAIN:
            explain_screen.renderExplain();
        #Tasten (werden immer gecheckt, egal welcher gamestate)
        listenForKeys();
   #Ende
   if settings.music_enabled:
       pygame.mixer.music.stop();
   pygame.quit();
   sys.exit();

#Starte nur als on Standing Programm
if __name__ == "__main__":
    showLogo();
    pygame.mixer.music.load("models/game/ambient/theme.wav");
    pygame.mixer.music.play(-1, 0.0);
    pygame.mixer.music.set_volume(0.4);
    if not settings.music_enabled:
        pygame.mixer.music.pause();
    start();

