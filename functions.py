import pygame, time;
from constants import *;

isFullscreen = False;
 
def toggle_fullscreen():
    global isFullscreen;
    screen = pygame.display.get_surface();
    tmp = screen.convert();
    pygame.display.quit();
    pygame.display.init();
    isFullscreen = not isFullscreen;
    if isFullscreen:
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN);
        pygame.mouse.set_visible(False);
    else:
        screen = pygame.display.set_mode((WIDTH, HEIGHT));
        pygame.mouse.set_visible(True);

    screen.blit(tmp,(0,0));
    pygame.display.set_caption("Escape The Hausi"); 
    
    return screen;

def showLogo():
    global WIDTH, HEIGHT;
    screen = pygame.display.get_surface();
    img = pygame.transform.scale(pygame.image.load("Holigamer_Developement_Logo.png"), (570/2, 682/2)).convert(); 
    img.set_alpha(0);
    rect = img.get_rect();
    rect.center = (WIDTH/2, HEIGHT/2);
    for i in range(0, 100):
        screen.fill((0,0,0));
        img.set_alpha(img.get_alpha()+2);
        screen.blit(img, rect);
        pygame.display.flip();
    time.sleep(2);
    for i in range(0, 100):
        screen.fill((0,0,0));
        img.set_alpha(img.get_alpha()-2);
        screen.blit(img, rect);
        pygame.display.flip();
